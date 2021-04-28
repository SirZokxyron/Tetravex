from environnement import *


class Menu:
    def __init__(self):
        self.en_cours = True
        self.fich = "aucun"
        self.env = 0
        self.command = ""
        self.cmds = {
            "help" : "affiches toutes les commandes disponibles.",
            "clear": "supprime le contenu a l'ecran.",
            "charger" : "charge la grille du fichier .tetra fourni.",
            "reset" : "reinitialise la grille et les clauses.",
            "debug" : "affiche les booleens de la grille chargee.",
            "print" : "affiche les cases de la grille.",
            "resoudre" : "resoud la grille chargee.",
            "quitter" : "quitter le programme."
        }

    def statut(self):
        print(f"Fichier courant : {self.fich}")

    def parse(self):
        self.command = input("> ")
        if self.command in self.cmds:
            print()
            eval(f'self.{self.command}()')
        else:
            print(f'''\nLa commande "{self.command}" n'existe pas.\nUtilisez "help" pour acceder a la liste des commandes.\n''')

    def help(self):
        for cle_i in self.cmds:
            print(cle_i, ":", self.cmds[cle_i])
        print()

    def clear(self):
        os.system("clear")

    def charger(self):
        print("Fichier disponibles :")
        os.system("for fich in $(ls samples); do echo $fich; done")
        self.fich = input("\n\tFichier a charger : ")
        print()
        grille = Grille()
        try:
            grille.charger_fich(f'samples/{self.fich}')
        except FileNotFoundError:
            print(f'''\tLe fichier "{self.fich}" n'existe pas ou les permissions sont insuffisantes.\n''')
        self.env = Environnement(grille)

    def reset(self):
        if self.fich == "aucun":
            print("\tAucun fichier n'est charge.\n")
        else:
            grille = Grille()
            grille.charger_fich(f'samples/{self.fich}')
            self.env = Environnement(grille)

    def debug(self):
        if self.fich == "aucun":
            print("\tAucun fichier n'est charge.\n")
        else:
            self.env.tetra.debug()

    def print(self):
        if self.fich == "aucun":
            print("\tAucun fichier n'est charge.\n")
        else:
            self.env.tetra.print("pretty")

    def resoudre(self):
        if self.fich == "aucun":
            print("\tAucun fichier n'est charge.\n")
        else:
            self.env.resoudre()

    def est_en_cours(self):
        return self.en_cours

    def quitter(self):
        self.en_cours = False
