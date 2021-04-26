from tetravex import *
import os
from time import sleep


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

class Environnement:
    def __init__(self, tetra:Grille):
        self.tab = []
        self.tetra = tetra
        self.solution = []

    def ajouter_clause(self, clause:list):
        self.tab.append(clause)

    def print(self):
        for clause_i in self.tab:
            print(clause_i)

    def unicite_coord(self):
        for piece_i in range(self.tetra.cote ** 2):
            coord_x = []
            coord_y = []
            for coord_i in range(self.tetra.cote):
                coord_x.append(self.tetra.tab[piece_i].bool_x[coord_i])
                coord_y.append(self.tetra.tab[piece_i].bool_y[coord_i])
                for coord_i_n in range(coord_i + 1, self.tetra.cote):
                    coord_x_neg = []
                    coord_y_neg = []
                    coord_x_neg.append(-(self.tetra.tab[piece_i].bool_x[coord_i]))
                    coord_x_neg.append(-(self.tetra.tab[piece_i].bool_x[coord_i_n]))
                    coord_y_neg.append(-(self.tetra.tab[piece_i].bool_y[coord_i]))
                    coord_y_neg.append(-(self.tetra.tab[piece_i].bool_y[coord_i_n]))

                    self.ajouter_clause(coord_x_neg)
                    self.ajouter_clause(coord_y_neg)
            self.ajouter_clause(coord_x)
            self.ajouter_clause(coord_y)

    def anti_superposition(self):
        for piece_i in range(self.tetra.cote ** 2):
            for piece_i_p in range(piece_i + 1, self.tetra.cote ** 2):
                for i in range(self.tetra.cote):
                    for j in range(self.tetra.cote):
                        clause_x = []
                        clause_y = []

                        clause_x.append(-(self.tetra.tab[piece_i].bool_x[i]))
                        clause_x.append(-(self.tetra.tab[piece_i_p].bool_x[i]))
                        clause_y.append(-(self.tetra.tab[piece_i].bool_y[i]))
                        clause_y.append(-(self.tetra.tab[piece_i_p].bool_y[i]))

                        clause_x.append(-(self.tetra.tab[piece_i].bool_y[j]))
                        clause_x.append(-(self.tetra.tab[piece_i_p].bool_y[j]))
                        clause_y.append(-(self.tetra.tab[piece_i].bool_x[j]))
                        clause_y.append(-(self.tetra.tab[piece_i_p].bool_x[j]))

                        self.ajouter_clause(clause_x)
                        self.ajouter_clause(clause_y)

    def logique_numerique(self):
        for piece_i in range(self.tetra.cote ** 2):
            for cote_i in range(0, 4):
                piece_emboitables = []
                for piece_j in range(self.tetra.cote ** 2):
                    if piece_i == piece_j:
                        continue
                    if self.tetra.tab[piece_i].nombres[cote_i] == self.tetra.tab[piece_j].nombres[(cote_i + 2) % 4]:
                        piece_emboitables.append(self.tetra.tab[piece_j])
                if len(piece_emboitables) == 0:
                    clause = []
                    if cote_i == 0:
                        clause.append(self.tetra.tab[piece_i].bool_y[self.tetra.cote - 1])
                    elif cote_i == 1:
                        clause.append(self.tetra.tab[piece_i].bool_x[self.tetra.cote - 1])
                    elif cote_i == 2:
                        clause.append(self.tetra.tab[piece_i].bool_y[0])
                    else:
                        clause.append(self.tetra.tab[piece_i].bool_x[0])
                    self.ajouter_clause(clause)
                else:
                    if (cote_i == 0) or (cote_i == 1):
                        delta = 1
                        start = 0
                        end = self.tetra.cote - 1
                    else:
                        delta = -1
                        start = 1
                        end = self.tetra.cote
                    for i in range(start, end):
                        for j in range(0, self.tetra.cote):
                            clause = []
                            if cote_i % 2 == 0:
                                for piece_e in piece_emboitables:
                                    clause.append([piece_e.bool_y[i + delta], piece_e.bool_x[j]])
                                clause = combinaison_tab(clause)
                                for combi_i in clause:
                                    if cote_i == 0:
                                        combi_i.append(self.tetra.tab[piece_i].bool_y[self.tetra.cote - 1])
                                    else:
                                        combi_i.append(self.tetra.tab[piece_i].bool_y[0])
                                    combi_i.append(-self.tetra.tab[piece_i].bool_y[i])
                                    combi_i.append(-self.tetra.tab[piece_i].bool_x[j])
                            else:
                                for piece_e in piece_emboitables:
                                    clause.append([piece_e.bool_x[i + delta], piece_e.bool_y[j]])
                                clause = combinaison_tab(clause)
                                for combi_i in clause:
                                    if cote_i == 0:
                                        combi_i.append(self.tetra.tab[piece_i].bool_x[self.tetra.cote - 1])
                                    else:
                                        combi_i.append(self.tetra.tab[piece_i].bool_x[0])
                                    combi_i.append(-self.tetra.tab[piece_i].bool_x[i])
                                    combi_i.append(-self.tetra.tab[piece_i].bool_y[j])
                            for clause_i in clause:
                                self.ajouter_clause(clause_i)

    def remplir(self):
        self.unicite_coord()
        self.anti_superposition()
        self.logique_numerique()

    def creer_dimacs(self):
        f = open(f'dimacs/{self.tetra.fich[8:-6]}.cnf', "w")
        f.write(f'p cnf {(self.tetra.cote ** 2) *  (self.tetra.cote * 2)} {len(self.tab)}\n')
        for clause_i in self.tab:
            for var_i in clause_i:
                f.write(str(var_i)+" ")
            f.write("0\n")
        f.close()

    def sat_solver(self):
        os.system(f'''sat4j dimacs/{self.tetra.fich[8:-6]}.cnf > dimacs/{self.tetra.fich[8:-6]}.output''')
        f = open(f"dimacs/{self.tetra.fich[8:-6]}.output", "r")
        output = f.readlines()
        f.close()
        satis_cond = [satis for satis in output if satis[0] == 's'][0][2:-1]
        if satis_cond == "SATISFIABLE":
            valeurs = [int(val_i) for val_i in [valeurs for valeurs in output if valeurs[0] == 'v'][0][2:-3].split(" ")]
            valeurs = [valeurs[x:x+self.tetra.cote * 2] for x in range(0, len(valeurs), self.tetra.cote * 2)]
            for piece_i in range(self.tetra.cote ** 2):
                self.solution.append(indice_tab(valeurs[piece_i], self.tetra.cote))
        else:
            print("La grille chargee est insatisfaisable.")

    def resoudre(self):
        if len(self.solution) == 0:
            self.remplir()
            self.creer_dimacs()
            self.sat_solver()
        os.system("clear")
        self.tetra.print("pretty")
        for piece_i in range(self.tetra.cote ** 2):
            self.tetra.echanger(piece_i, self.solution[piece_i])
            sleep(1.5)
            os.system("clear")
            self.tetra.print("pretty")