from menu import *


if __name__ == '__main__':

    menu = Menu()

    while menu.est_en_cours():
        menu.statut()
        menu.parse()
