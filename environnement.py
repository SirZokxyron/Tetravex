from tetravex import *
import os
from time import sleep


# Fonction recursive qui renvoie toutes les combinaisons d'une liste de liste
# Specification : List List -> List List
# Exemple : [[a, b], [c, d]] -> [[a, c], [a, d], [b, c], [b, d]]
def combinaison_tab(tab:list) -> list:
    if len(tab) == 0:
        return [[]]
    elif len(tab) == 1:
        return [[tab[0][0]], [tab[0][1]]]
    v1 = tab.pop(0)
    new_tab = [[v1[0]] for i in range(2 ** (len(tab)))]
    new_tab += [[v1[1]] for i in range(2 ** (len(tab)))]
    n = len(tab)
    rec_tab = combinaison_tab(tab)
    for v_i in range(len(new_tab)):
        new_tab[v_i] += rec_tab[v_i % (2 ** n)]
    return new_tab


# Fonction qui renvoie l'indice dans le tableau indique par les booleens positifs
# Exemples : [-x0, x1, y0, -y1] -> 3
#            [x0, -x1, -x2, -y0, -y1, y2] -> 0
#            [-x0, x1, -x2, y0, -y1, -y2] -> 7
def indice_tab(coord:list, cote:int) -> int:
    pos = 0
    for val_i in range(cote):
        if coord[val_i] > 0:
            pos += val_i
            break
    for val_i in range(cote, cote * 2):
        if coord[val_i] > 0:
            pos += cote * (cote - (val_i % cote) - 1)
            break
    return pos


class Environnement(Grille):
    # Une instance de cette classe represente un environnement de clauses d'une grille de Tetravex
    def __init__(self):
        Grille.__init__(self)
        # Contient les clauses
        self.clauses = []
        # Contient les positions auxquelles doivent se placer les pieces pour resoudre la grille
        self.solution = []
        # Tuple qui indique quelles regles ont ete appliquees
        self.regles = (False, False, False)
        # Booleen qui indique si le fichier .cnf a ete cree
        self.dimacs = False
        # Booleen qui indique si le fichier .output a ete cree
        self.output = False
        # Booleen qui indique si la grille est resolvable d'après le SATSolver
        self.valide = False

    ######################################
    ###       GENERATION CLAUSE        ###
    ######################################

    def ajouter_clause(self, clause:list):
        self.clauses.append(clause)

    def unicite_coord(self):
        a, b, c = self.regles
        if a:
            self.logs = f'''[{dt.now().strftime("%H:%M:%S")}] La regle d'unicite de coordonnees a deja ete appliquee.\n'''
            return
        for piece_i in range(self.cote ** 2):
            coord_x = []
            coord_y = []
            for coord_i in range(self.cote):
                coord_x.append(self.pieces_dispo[piece_i].bool_x[coord_i])
                coord_y.append(self.pieces_dispo[piece_i].bool_y[coord_i])
                for coord_i_n in range(coord_i + 1, self.cote):
                    coord_x_neg = []
                    coord_y_neg = []
                    coord_x_neg.append(-(self.pieces_dispo[piece_i].bool_x[coord_i]))
                    coord_x_neg.append(-(self.pieces_dispo[piece_i].bool_x[coord_i_n]))
                    coord_y_neg.append(-(self.pieces_dispo[piece_i].bool_y[coord_i]))
                    coord_y_neg.append(-(self.pieces_dispo[piece_i].bool_y[coord_i_n]))

                    self.ajouter_clause(coord_x_neg)
                    self.ajouter_clause(coord_y_neg)
            self.ajouter_clause(coord_x)
            self.ajouter_clause(coord_y)
        self.logs = f'''[{dt.now().strftime("%H:%M:%S")}] La regle d'unicite de coordonnees a ete appliquee avec succes.\n'''
        self.regles = (True, b, c)

    def anti_superposition(self):
        a, b, c = self.regles
        if b:
            self.logs = f'''[{dt.now().strftime("%H:%M:%S")}] La regle d'anti superposition a deja ete appliquee.\n'''
            return
        for piece_i in range(self.cote ** 2):
            for piece_i_p in range(piece_i + 1, self.cote ** 2):
                for i in range(self.cote):
                    for j in range(self.cote):
                        clause_x = [-(self.pieces_dispo[piece_i].bool_x[i]), -(self.pieces_dispo[piece_i_p].bool_x[i]),
                                    -(self.pieces_dispo[piece_i].bool_y[j]), -(self.pieces_dispo[piece_i_p].bool_y[j])]
                        self.ajouter_clause(clause_x)
        self.logs = f'''[{dt.now().strftime("%H:%M:%S")}] La regle d'anti superposition a ete appliquee avec succes.\n'''
        self.regles = (a, True, c)

    def logique_numerique(self):
        a, b, c = self.regles
        if c:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] La regle de logique numerique a deja ete appliquee.\n'
            return
        for piece_i in range(self.cote ** 2):
            for cote_i in range(0, 4):
                piece_emboitables = []
                for piece_j in range(self.cote ** 2):
                    if piece_i == piece_j:
                        continue
                    if self.pieces_dispo[piece_i].nombres[cote_i] == self.pieces_dispo[piece_j].nombres[(cote_i + 2) % 4]:
                        piece_emboitables.append(self.pieces_dispo[piece_j])
                if len(piece_emboitables) == 0:
                    clause = []
                    if cote_i == 0:
                        clause.append(self.pieces_dispo[piece_i].bool_y[self.cote - 1])
                    elif cote_i == 1:
                        clause.append(self.pieces_dispo[piece_i].bool_x[self.cote - 1])
                    elif cote_i == 2:
                        clause.append(self.pieces_dispo[piece_i].bool_y[0])
                    else:
                        clause.append(self.pieces_dispo[piece_i].bool_x[0])
                    self.ajouter_clause(clause)
                else:
                    if (cote_i == 0) or (cote_i == 1):
                        delta = 1
                        start = 0
                        end = self.cote - 1
                    else:
                        delta = -1
                        start = 1
                        end = self.cote
                    for i in range(start, end):
                        for j in range(0, self.cote):
                            clause = []
                            if cote_i % 2 == 0:
                                for piece_e in piece_emboitables:
                                    clause.append([piece_e.bool_y[i + delta], piece_e.bool_x[j]])
                                clause = combinaison_tab(clause)
                                for combi_i in clause:
                                    if cote_i == 0:
                                        combi_i.append(self.pieces_dispo[piece_i].bool_y[self.cote - 1])
                                    else:
                                        combi_i.append(self.pieces_dispo[piece_i].bool_y[0])
                                    combi_i.append(-self.pieces_dispo[piece_i].bool_y[i])
                                    combi_i.append(-self.pieces_dispo[piece_i].bool_x[j])
                            else:
                                for piece_e in piece_emboitables:
                                    clause.append([piece_e.bool_x[i + delta], piece_e.bool_y[j]])
                                clause = combinaison_tab(clause)
                                for combi_i in clause:
                                    if cote_i == 0:
                                        combi_i.append(self.pieces_dispo[piece_i].bool_x[self.cote - 1])
                                    else:
                                        combi_i.append(self.pieces_dispo[piece_i].bool_x[0])
                                    combi_i.append(-self.pieces_dispo[piece_i].bool_x[i])
                                    combi_i.append(-self.pieces_dispo[piece_i].bool_y[j])
                            for clause_i in clause:
                                self.ajouter_clause(clause_i)
        self.logs = f'[{dt.now().strftime("%H:%M:%S")}] La regle de logique numerique a ete appliquee avec succes.\n'
        self.regles = (a, b, True)

    ######################################
    ###    GENERATION DIMACS & SAT     ###
    ######################################

    def creer_dimacs(self):
        if len(self.clauses) == 0:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Impossible de resoudre une grille sans clauses.\n'
            return
        if self.dimacs:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Le fichier .cnf est deja existant.\n'
            return
        f = open(f'dimacs/{self.fich[8:-6]}.cnf', "w")
        f.write(f'p cnf {(self.cote ** 2) *  (self.cote * 2)} {len(self.clauses)}\n')
        for clause_i in self.clauses:
            for var_i in clause_i:
                f.write(str(var_i)+" ")
            f.write("0\n")
        f.close()
        self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Fichier .cnf genere avec succes.\n'
        self.dimacs = True

    def sat_solveur(self):
        if not self.dimacs:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Le fichier .cnf est manquant pour generer le fichier .output.\n'
            return
        if self.output:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Le fichier .output est deja existant.\n'
            return
        os.system(f'''sat4j dimacs/{self.fich[8:-6]}.cnf > dimacs/{self.fich[8:-6]}.output''')
        f = open(f"dimacs/{self.fich[8:-6]}.output", "r")
        output = f.readlines()
        f.close()
        satis_cond = [satis for satis in output if satis[0] == 's'][0][2:-1]
        if satis_cond == "SATISFIABLE":
            valeurs = [int(val_i) for val_i in [valeurs for valeurs in output if valeurs[0] == 'v'][0][2:-3].split(" ")]
            valeurs = [valeurs[x:x+self.cote * 2] for x in range(0, len(valeurs), self.cote * 2)]
            for piece_i in range(self.cote ** 2):
                self.solution.append(indice_tab(valeurs[piece_i], self.cote))
            self.valide = True
        self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Fichier .output genere avec succes.\n'
        self.output = True

    ######################################
    ###          SUPPRESSION           ###
    ######################################

    def reset(self):
        Grille.reset(self)
        self.clauses = []
        self.solution = []
        self.regles = (False, False, False)
        self.dimacs = False
        self.output = False

    def suppr(self):
        Grille.suppr(self)
        self.reset()