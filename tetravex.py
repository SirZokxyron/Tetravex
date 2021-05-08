from random import randint
from datetime import datetime as dt
from requests import get as web


class Piece:
    # Une instance de cette classe represente une piece d'une grille de Tetravex
    # Parametres : - nombre_l : les nombres autour de la piece au format [Nord, Est, Sud, Ouest]
    #              - ex_bool  : le booleen courant
    #              - cote     : la taille d'un cote de la grille
    #              - vide     : si la piece est vide ou non
    def __init__(self, id: int = 0, nombre_l: list = [], cote: int = 0):
        # Vrai si la piece est vide, Faux sinon
        if nombre_l == []:
            self.vide = True
        else:
            self.vide = False
        # ID unique pour chaque piece
        self.id = id
        # Contient la taille du cote de la grille a laquelle la piece appartient
        self.cote = cote
        # Contient les nombres autours de la piece [Nord, Est, Sud, Ouest]
        self.nombres = nombre_l
        # Contiendra les booleens de la coordonnee x de la piece [x0,..., xi,..., xn]
        self.bool_x = [0] * cote
        # Contiendra les booleens de la coordonnee y de la piece [y0,..., yi,..., yn]
        self.bool_y = [0] * cote

    ######################################
    ###          GENERATION            ###
    ######################################

    # Rempli les booleens d'une piece
    def remplir_bool(self, bool_courant: int) -> int:
        # Remplissage du tableau des booleens de la coordonnee x
        for x_i in range(self.cote):
            self.bool_x[x_i] = bool_courant
            bool_courant += 1

        # Remplissage du tableau des booleens de la coordonnee y
        for y_i in range(self.cote):
            self.bool_y[y_i] = bool_courant
            bool_courant += 1

        # On renvoie le bool_courant pour les prochaines pieces
        return bool_courant

    ######################################
    ###           AFFICHAGE            ###
    ######################################

    # Affiche les booleens d'une piece
    def debug(self):
        if not self.vide:
            print("\tbool_x : ", end="")
            print(*self.bool_x)
            print("\tbool_y : ", end="")
            print(*self.bool_y)

    # Renvoie un tuple pour afficher la piece
    def print(self) -> tuple:
        if self.vide:
            return "      ", "  ●   ", "      "
        else:
            return f'■ {self.nombres[0]} ■ ', f'{self.nombres[3]}   {self.nombres[1]} ', f'■ {self.nombres[2]} ■ '


class Grille:
    # Une instance de cette classe represente une grille de Tetravex
    def __init__(self):
        # Contient les logs de chaque action effectuée
        self.logs = ""
        # Contient la taille du cote de la grille
        self.cote = 0
        # Contient le tableau de pieces disponible
        self.pieces_dispo = []
        # Contient le tableau ordonne des pieces pour la resolution
        self.grille_finale = []
        # Contient le fichier duquel la grille a ete chargee
        self.fich = ""

    ######################################
    ###          GENERATION            ###
    ######################################

    # Fonction qui charge une grille depuis un fichier donne
    def charger_fich(self, fich: str):
        try:
            # On recupere le fichier passe en parametre
            self.fich = fich

            # On recupere le contenu du fichier
            f = open(fich, "r")
            nombres = [[int(n) for n in line.split(' ')] for line in f.readlines()]
            f.close()

            # On rempli le cote de la grille
            self.cote = (nombres.pop(0))[0]

            # On genere autant de piece vide qu'il faut pour la solution
            self.grille_finale = [Piece() for nombre_piece in range(self.cote ** 2)]

            bool_courant = 1
            # Pour chaque piece lue dans le fichier
            for piece_i in range(self.cote ** 2):
                # On ajoute la piece au tableau de piece disponible
                self.pieces_dispo.append(Piece(piece_i, nombres[piece_i], self.cote))

                # On rempli ses tableaux de coordonnees booleennes
                bool_courant = self.pieces_dispo[piece_i].remplir_bool(bool_courant)
        except Exception as err:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] {type(err).__name__}.\n'
            return
        self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Le fichier {self.fich} a bien ete charge.\n'

    # Fonction qui genere aleatoirement une grille en fonction d'une taille de cote donne
    def gen_alea(self, cote: int = 3):
        # On recupere la taille d'un cote de la grille
        self.cote = cote

        # On met a jour le potentiel nom de fichier
        self.fich = f'samples/{cote}x{cote}_alea_{dt.now().strftime("%H_%M_%S")}.tetra'

        # On genere (cote ** 2) piece aleatoirement avec des nombres entre 0 et 9
        self.pieces_dispo = [Piece(nombre_piece, [randint(0, 9) for i in range(4)], self.cote) for nombre_piece in
                             range(self.cote ** 2)]

        # On rempli les booleens des pieces generees
        bool_courant = 1
        for piece_i in self.pieces_dispo:
            bool_courant = piece_i.remplir_bool(bool_courant)

        # On genere autant de piece vide qu'il faut pour la solution
        self.grille_finale = [Piece() for nombre_piece in range(self.cote ** 2)]

        self.logs = f'[{dt.now().strftime("%H:%M:%S")}] La grille a bien ete generee aleatoirement.\n'

    # Fonction qui charge une partie valide depuis le site gamegix.com
    def gen_from_site(self, cote: int = 3):
        if cote < 2 or cote > 5:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Cote de grille invalide pour un telechargement.\n'
            return
        page = web(f'https://gamegix.com/tetravex/game?size={cote}')
        page = page.text
        page = page[page.find('class="tile"'):page.find('Select board size')]

        self.cote = cote
        self.fich = f'samples/{cote}x{cote}_web_{dt.now().strftime("%H_%M_%S")}.tetra'
        self.grille_finale = [Piece() for nombre_piece in range(self.cote ** 2)]

        nombres = []
        for piece_i in range(self.cote ** 2):
            valeurs = [0] * 4
            page = page[page.find("side left"):]
            page = page[page.find(">"):]
            valeurs[3] = page[1]
            page = page[page.find("side top"):]
            page = page[page.find(">"):]
            valeurs[0] = page[1]
            page = page[page.find("side right"):]
            page = page[page.find(">"):]
            valeurs[1] = page[1]
            page = page[page.find("side bottom"):]
            page = page[page.find(">"):]
            valeurs[2] = page[1]
            nombres.append(valeurs)

        bool_courant = 1
        for piece_i in range(self.cote ** 2):
            # On ajoute la piece au tableau de piece disponible
            self.pieces_dispo.append(Piece(piece_i, nombres[piece_i], self.cote))

            # On rempli ses tableaux de coordonnees booleennes
            bool_courant = self.pieces_dispo[piece_i].remplir_bool(bool_courant)
        self.logs = f'[{dt.now().strftime("%H:%M:%S")}] La grille a bien ete telecharge.\n'

    ######################################
    ###          SUPPRESSION           ###
    ######################################

    # Fonction qui supprime la grille courante
    def suppr(self):
        self.cote = 0
        self.pieces_dispo = []
        self.grille_finale = []
        self.fich = ""
        self.logs = f'[{dt.now().strftime("%H:%M:%S")}] La grille courante a ete supprime.\n'

    # Fonction qui re-initialise la grille courante
    def reset(self):
        for piece_i in range(self.cote ** 2):
            if not self.grille_finale[piece_i].vide:
                self.echanger(self.grille_finale[piece_i].id, piece_i)

    ######################################
    ###          SAUVEGARDE            ###
    ######################################

    # Fonction qui sauvegarde la grille courante dans un fichier donne
    def save_fich(self):
        if self.cote == 0:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Impossible de sauvegarder une grille vide.\n'
            return
        f = open(self.fich, "w")
        f.write(f'{self.cote}\n')
        for piece_i in self.pieces_dispo:
            for cote_i in range(4):
                f.write(f'{piece_i.nombres[cote_i]} ')
            f.write("\n")
        f.close()
        self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Grille sauvegardee avec succes sous le nom de {self.fich}.\n'

    ######################################
    ###          RESOLUTION            ###
    ######################################

    # Fonction qui echange la position de deux pieces
    # pieces_disponibles[piece_1] <- pieces_solutions[piece_2]
    # pieces_solutions[piece_2]   <- pieces_disponibles[piece_1]
    def echanger(self, piece_1: int, piece_2: int):
        try:
            self.pieces_dispo[piece_1], self.grille_finale[piece_2] = self.grille_finale[piece_2], self.pieces_dispo[piece_1]
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Piece {piece_1} en position {piece_2}.\n'
        except Exception as err:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] {type(err).__name__}.\n'
            return