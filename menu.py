from environnement import *
import tkinter as tk


class Menu(Environnement):
    def __init__(self):
        Environnement.__init__(self)
        # Creation de la fenetre
        self.root = tk.Tk()
        self.root.title("Resolveur Tetravex")
        self.root.geometry("900x400")
        # Barre de menu
        self.menu_bar = tk.Menu(self.root)
        # Option "Grille" de la barre de menu
        self.grille_menu = tk.Menu(self.menu_bar, tearoff=1)
        self.grille_menu.add_command(label="Ouvrir fichier", command=self.menu_ouvrir_grille)
        self.grille_menu.add_command(label="Sauvegarder fichier", command=self.menu_sauvegarder_grille)
        self.grille_menu.add_command(label="Generer aleatoirement", command=self.menu_gen_alea)
        self.grille_menu.add_command(label="Charger depuis internet", command=self.menu_web_dl)
        self.grille_menu.add_command(label="Reinitialiser", command=self.menu_reinitialiser)
        # Sous option "Regles" de l'option "Solveur" de la barre de menu
        self.regles_menu = tk.Menu(self.menu_bar, tearoff=1)
        self.regles_menu.add_command(label="Unicite de coordonnees", command=self.menu_unicite)
        self.regles_menu.add_command(label="Anti superposition", command=self.menu_anti_superposition)
        self.regles_menu.add_command(label="Logique numerique", command=self.menu_logique_numerique)
        self.regles_menu.add_command(label="Toutes", command=self.menu_toute)
        # Option "Solveur" de la barre de menu
        self.solveur_menu = tk.Menu(self.menu_bar, tearoff=1)
        self.solveur_menu.add_cascade(label="Regles", menu=self.regles_menu)
        self.solveur_menu.add_command(label="Generer .cnf", command=self.menu_creer_dimacs)
        self.solveur_menu.add_command(label="Generer .output", command=self.menu_creer_output)
        # Option "Affichage" de la barre de menu
        self.affichage_menu = tk.Menu(self.menu_bar, tearoff=1)
        self.affichage_menu.add_command(label="Fichier .cnf", command=self.menu_afficher_cnf)
        self.affichage_menu.add_command(label="Fichier .output", command=self.menu_afficher_output)
        # Ajout des options a la barre de menu
        self.menu_bar.add_cascade(label="Grille", menu=self.grille_menu)
        self.menu_bar.add_cascade(label="Solveur", menu=self.solveur_menu)
        self.menu_bar.add_cascade(label="Affichage", menu=self.affichage_menu)
        self.menu_bar.add_command(label="Logs", command=self.menu_logs)
        self.menu_bar.add_command(label="Resoudre", command=self.menu_resoudre)
        self.menu_bar.add_command(label="Resoudre Tout", command=self.menu_resoudre_tout)
        # Ajout de la barre de menu
        self.root.config(menu=self.menu_bar)
        # Creation de la grille
        self.text_grille = tk.StringVar()
        self.text_grille.set(self.print())
        self.label_grille = tk.Label(self.root, textvariable=self.text_grille, font=("Courier", 25))
        self.label_grille.pack(expand="YES")
        # Initialisation des logs
        self.text_log = ""
        # Boucle principal de la fenetre
        self.root.mainloop()

    ######################################
    ###         UPDATE & PRINT         ###
    ######################################

    def print(self) -> str:
        if self.cote == 0:
            return ""
        affichage = ""
        for ligne_i in range(self.cote):
            ligne_top = ""
            ligne_mid = ""
            ligne_bot = ""
            for piece_i in range(self.cote):
                piece_actuelle = self.pieces_dispo[ligne_i * self.cote + piece_i]
                buffer_top, buffer_mid, buffer_bot = piece_actuelle.print()
                ligne_top += buffer_top
                ligne_mid += buffer_mid
                ligne_bot += buffer_bot
            ligne_top += "      "
            ligne_mid += "      "
            ligne_bot += "      "
            for piece_i in range(self.cote):
                piece_actuelle = self.grille_finale[ligne_i * self.cote + piece_i]
                buffer_top, buffer_mid, buffer_bot = piece_actuelle.print()
                ligne_top += buffer_top
                ligne_mid += buffer_mid
                ligne_bot += buffer_bot
            affichage += f'{ligne_top}\n{ligne_mid}\n{ligne_bot}\n'
        return affichage

    def update_grille(self):
        self.text_grille.set(self.print())

    def update_logs(self):
        if self.text_log != "":
            self.text_log.insert(tk.INSERT, self.logs)
            self.logs = ""

    ######################################
    ###             USER               ###
    ######################################

    def demande_user(self):
        # Creation du pop up
        self.user_input = 3
        self.pop_up = tk.Tk()
        self.pop_up.geometry("200x75")
        frame = tk.Frame(self.pop_up)
        self.input_box = tk.Entry(frame)
        self.input_box.pack()
        self.input_box.focus_set()
        bouton_valider = tk.Button(frame, text="Valider", command=self.fin_demande_user)
        bouton_valider.pack(pady=5)
        frame.pack(expand="YES")
        self.pop_up.mainloop()

    def fin_demande_user(self):
        if self.input_box.get() == "":
            self.user_input = 3
        else:
            self.user_input = self.input_box.get()
        self.pop_up.quit()
        self.pop_up.destroy()

    ######################################
    ###             MENU 1             ###
    ######################################

    def menu_ouvrir_grille(self):
        self.suppr()
        self.demande_user()
        self.charger_fich(self.user_input)
        self.update_grille()
        self.update_logs()

    def menu_sauvegarder_grille(self):
        self.save_fich()
        self.update_logs()

    def menu_gen_alea(self):
        self.suppr()
        self.demande_user()
        try:
            self.gen_alea(int(self.user_input))
        except Exception as err:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] {type(err).__name__}.\n'
        self.update_grille()
        self.update_logs()

    def menu_web_dl(self):
        self.suppr()
        self.demande_user()
        try:
            self.gen_from_site(int(self.user_input))
        except Exception as err:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] {type(err).__name__}.\n'
        self.update_grille()
        self.update_logs()

    def menu_reinitialiser(self):
        self.reset()
        self.update_grille()
        self.logs = f'[{dt.now().strftime("%H:%M:%S")}] La grille courante a ete reinitialiser.\n'
        self.update_logs()

    ######################################
    ###             MENU 2             ###
    ######################################

    def menu_unicite(self):
        unicite, superposition, logique = self.regles
        if unicite == False:
            self.unicite_coord()
        self.update_logs()

    def menu_anti_superposition(self):
        unicite, superposition, logique = self.regles
        if superposition == False:
            self.anti_superposition()
        self.update_logs()

    def menu_logique_numerique(self):
        unicite, superposition, logique = self.regles
        if logique == False:
            self.logique_numerique()
        self.update_logs()

    def menu_toute(self):
        self.menu_unicite()
        self.menu_anti_superposition()
        self.menu_logique_numerique()

    def menu_creer_dimacs(self):
        if self.dimacs == False:
            self.creer_dimacs()
        self.update_logs()

    def menu_creer_output(self):
        if self.output == False:
            self.sat_solveur()
        self.update_logs()

    ######################################
    ###             MENU 3             ###
    ######################################

    def menu_afficher_cnf(self):
        if not self.dimacs:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Le fichier .cnf serait vide.\n'
            self.update_logs()
            return
        fenetre_cnf = tk.Tk()
        fenetre_cnf.geometry("500x500")
        text_cnf = tk.Text(fenetre_cnf, width=180, heigh=380, font=("Courier", 11))
        f = open(f'dimacs/{self.fich[8:-6]}.cnf', "r")
        text = f.read()
        text_cnf.insert(tk.INSERT, text)
        text_cnf.pack(expand="YES")
        fenetre_cnf.mainloop()

    def menu_afficher_output(self):
        if not self.output:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Le fichier .output est vide.\n'
            self.update_logs()
            return
        fenetre_output = tk.Tk()
        fenetre_output.geometry("500x500")
        text_output = tk.Text(fenetre_output, width=180, heigh=380, font=("Courier", 11))
        f = open(f'dimacs/{self.fich[8:-6]}.output', "r")
        text = f.read()
        text_output.insert(tk.INSERT, text)
        text_output.pack(expand="YES")
        fenetre_output.mainloop()

    ######################################
    ###          MENU AUTRES           ###
    ######################################

    def menu_logs(self):
        # Creation de la fenetre de logs
        self.fenetre_logs = tk.Tk()
        self.fenetre_logs.geometry("500x500")
        self.text_log = tk.Text(self.fenetre_logs, width=180, heigh=380, font=("Courier", 11))
        self.text_log.insert(tk.INSERT, self.logs)
        self.text_log.pack(expand="YES")
        self.fenetre_logs.mainloop()

    # Fonction qui resoud la grille clique par clique
    def menu_resoudre(self):
        if len(self.pieces_dispo) == 0:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Impossible de resoudre une grille vide.\n'
            return
        if self.dimacs == False:
            self.menu_creer_dimacs()
        if self.output == False:
            self.menu_creer_output()

        if self.dimacs and self.output and self.valide:
            for piece_i in range(self.cote ** 2):
                if self.pieces_dispo[piece_i].vide:
                    continue
                self.echanger(piece_i, self.solution[piece_i])
                self.update_grille()
                self.update_logs()
                break
        else:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] La grille est insatisfaisable.\n'
            self.update_logs()

    def menu_resoudre_tout(self):
        if len(self.pieces_dispo) == 0:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] Impossible de resoudre une grille vide.\n'
            return
        if self.dimacs == False:
            self.menu_creer_dimacs()
        if self.output == False:
            self.menu_creer_output()

        if self.valide:
            for piece_i in range(self.cote ** 2):
                if self.pieces_dispo[piece_i].vide:
                    continue
                self.echanger(piece_i, self.solution[piece_i])
                self.update_logs()
            self.update_grille()
        else:
            self.logs = f'[{dt.now().strftime("%H:%M:%S")}] La grille est insatisfaisable.\n'
            self.update_logs()
