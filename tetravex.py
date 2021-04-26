def erreur_fatale(msg: str):
    print(f'[ERREUR FATALE] {msg}')
    exit(-1)


class Piece:
    def __init__(self, numeros: list, ex_bool: int, cote: int):
        self.vide = False
        self.nombres = numeros
        self.bool_x = []
        for x_i in range(cote):
            self.bool_x.append(ex_bool)
            ex_bool += 1
        self.bool_y = []
        for y_i in range(cote):
            self.bool_y.append(ex_bool)
            ex_bool += 1

    def detruire(self):
        self.vide = True

    def print(self):
        print(self.nombres)

    def debug(self):
        print("\tbool_x : ", end="")
        print(*self.bool_x)
        print("\tbool_y : ", end="")
        print(*self.bool_y)


class Grille:
    def __init__(self, cote:int = 0):
        self.cote = cote
        self.tab = []
        self.solved = []
        for piece_i in range(self.cote ** 2):
            self.solved.append(0)
        self.fich = ""

    def gen_alea(self):
        print("TO DO")
        # TO DO LATER

    def charger_fich(self, fich: str):
        self.fich = fich
        f = open(fich, "r")
        nombres = [[int(n) for n in line.split(' ')] for line in f.readlines()]
        f.close()
        self.cote = (nombres.pop(0))[0]
        self.solved = []
        for piece_i in range(self.cote ** 2):
            self.solved.append(0)
        if len(nombres) != (self.cote ** 2):
            erreur_fatale(f'Nombre de pieces invalide dans le fichier "{fich}"')
        act_bool = 1
        for piece_i in range(self.cote ** 2):
            if len(nombres[piece_i]) != 4:
                erreur_fatale(f'Piece {piece_i} invalide dans le fichier "{fich}"')
            self.tab.append(Piece(nombres[piece_i], act_bool, self.cote))
            act_bool += (2 * self.cote)

    def echanger(self, piece_1: int, piece_2: int):
        piece_temp = self.solved[piece_2]
        self.solved[piece_2] = self.tab[piece_1]
        self.tab[piece_1] = piece_temp

    def print(self, arg: str = ""):
        if arg == "":
            for piece_i in range(self.cote ** 2):
                (self.tab[piece_i]).print()
        elif arg == "pretty":
            print("Pieces a disposition :")
            for ligne_i in range(self.cote):
                ligne_top = ""
                ligne_mid = ""
                ligne_bot = ""
                for piece_i in range(self.cote):
                    piece_actuelle = self.tab[ligne_i * self.cote + piece_i]
                    if type(piece_actuelle) != int:
                        ligne_top += f'■ {piece_actuelle.nombres[0]} ■ '
                        ligne_mid += f'{piece_actuelle.nombres[3]}   {piece_actuelle.nombres[1]} '
                        ligne_bot += f'■ {piece_actuelle.nombres[2]} ■ '
                    else:
                        ligne_top += "      "
                        ligne_mid += "  ●   "
                        ligne_bot += "      "
                print(ligne_top)
                print(ligne_mid)
                print(ligne_bot)
            print("\n\nGrille :\n")
            for ligne_i in range(self.cote):
                ligne_top = ""
                ligne_mid = ""
                ligne_bot = ""
                for piece_i in range(self.cote):
                    piece_actuelle = self.solved[ligne_i * self.cote + piece_i]
                    if type(piece_actuelle) != int:
                        ligne_top += f'■ {piece_actuelle.nombres[0]} ■ '
                        ligne_mid += f'{piece_actuelle.nombres[3]}   {piece_actuelle.nombres[1]} '
                        ligne_bot += f'■ {piece_actuelle.nombres[2]} ■ '
                    else:
                        ligne_top += "      "
                        ligne_mid += "  ●   "
                        ligne_bot += "      "
                print(ligne_top)
                print(ligne_mid)
                print(ligne_bot)
                print()
        else:
            erreur_fatale("Argument invalide")

    def debug(self):
        for piece_i in range(self.cote ** 2):
            print(f'Piece {piece_i}')
            (self.tab[piece_i]).debug()
