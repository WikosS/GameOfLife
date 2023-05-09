from tkinter import *
from tkinter import messagebox
from new import *


class Case(Button):
    def __init__(self, parent, x, y):
        super().__init__(parent)
        self.parent = parent # Widget parent de la case
        self.x = x # Numéro de colonne
        self.y = y # Numéro de ligne
        self.etat = 0 # État de la cellule : 0 = morte, 1 = vivante

    def get_etat(self):
        # Renvoie l'état de la case
        return self.etat

    def set_etat(self, nouvel_etat):
        # Met à jour l'état de la case
        self.etat = nouvel_etat

    def inverse_etat(self):
        # Inverse l'état de la case
        global App

        if self.etat == 0:
            self.config(bg = "white")
            self.etat = 1
        elif self.etat == 1:
            self.config(bg = 'black')
            self.etat = 0

        App.update_tab_etats(self.y, self.x)

    def update_couleur(self):
        # Met à jour la couleur de la case en fonction de son état
        if self.etat == 0:
            self.config(bg = 'black')
        elif self.etat == 1:
            self.config(bg = 'white')


class Appli(Tk):
    def __init__(self, nb_lignes, nb_colonnes):
        super().__init__()
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.Tab_Etats = [[0 for i in range(nb_colonnes)] for j in range(nb_lignes)] # Tableaux d'états (0 ou 1)
        self.Tab_Cases = [] # Tableau de cases
        self.initGUI()

    def initGUI(self):
        self.title("Jeu de la vie")
        self.geometry("600x600")

        # Ajout des frames (des containers à boutons)
        self.frame_boutons_iteration = Frame(self)
        self.frame_boutons_iteration.pack(side = BOTTOM)

        self.frame_boutons_configuration = Frame(self, pady = 10)
        self.frame_boutons_configuration.pack(side = BOTTOM)

        # Ajout des boutons dans les frames
        self.bouton_tout_noir = Button(self.frame_boutons_configuration, text="Damier Noir", width=20, command = self.damier_noir)
        #self.bouton_tout_noir.config(marginx = 200)
        self.bouton_tout_noir.pack(side=LEFT)
        self.bouton_aleatoire = Button(self.frame_boutons_configuration, text="Damier Aléatoire", width=20, command = self.damier_aleatoire)
        #self.bouton_aleatoire.config(padx = 200)
        self.bouton_aleatoire.pack(side=LEFT)
        self.bouton_tout_blanc = Button(self.frame_boutons_configuration, text="Damier Blanc", width=20, command = self.damier_blanc)
        #self.bouton_tout_blanc.config(padx = 200)
        self.bouton_tout_blanc.pack(side=LEFT)

        self.bouton_iteration = Button(self.frame_boutons_iteration, text="Nouvelle itération", width=20, command = self.calcule_iteration)
        self.bouton_iteration.pack(side=LEFT)
        self.bouton_iteration_auto = Button(self.frame_boutons_iteration, text="Défilement automatique", width=20, command = self.calcule_iteration_auto)
        self.bouton_iteration_auto.pack(side=LEFT)

    def get_Tab_Etats(self):
        # Renvoie Tab_Etats
        return self.Tab_Etats

    def damier_noir(self):
        self.Tab_Etats = [[0 for i in range(self.nb_colonnes)] for j in range(self.nb_lignes)] # Tableaux d'états (0 ou 1)
        self.update_IHM(self.nb_lignes, self.nb_colonnes)

    def damier_aleatoire(self):
        Genere_Grille(self.nb_lignes, self.nb_colonnes, self.Tab_Etats)
        self.update_IHM(self.nb_lignes, self.nb_colonnes)

    def damier_blanc(self):
        self.Tab_Etats = [[1 for i in range(self.nb_colonnes)] for j in range(self.nb_lignes)] # Tableaux d'états (0 ou 1)
        self.update_IHM(self.nb_lignes, self.nb_colonnes)

    def calcule_iteration(self):
        Calcule_nouvelle_iteration(self.Tab_Etats, self.nb_lignes, self.nb_colonnes)
        self.update_IHM(self.nb_lignes, self.nb_colonnes)

    def calcule_iteration_auto(self):
        Calcule_nouvelle_iteration(self.Tab_Etats, self.nb_lignes, self.nb_colonnes)
        self.update_IHM(self.nb_lignes, self.nb_colonnes)
        # Griser tous les boutons pour interdire à l'utilisateur de cliquer partout
        self.bouton_tout_noir.config(state = DISABLED)
        self.bouton_aleatoire.config(state = DISABLED)
        self.bouton_tout_blanc.config(state = DISABLED)
        self.bouton_iteration.config(state = DISABLED)
        self.bouton_iteration_auto.config(state = DISABLED)
        # Rappel automatique de la méthode toutes les 1000 millisecondes (toutes les secondes, quoi)
        self.after(1000, self.calcule_iteration_auto)

    def update_tab_etats(self, l, c):
        # Met à jour Tab_Etats en fonction de l'état de la cellule ligne l colonne c
        if self.Tab_Cases[NB_COLONNES*l + c].get_etat() == 0:
            self.Tab_Etats[l][c] = 0
        elif self.Tab_Cases[NB_COLONNES*l + c].get_etat() == 1:
            self.Tab_Etats[l][c] = 1

    def update_IHM(self, nb_lignes, nb_colonnes):
        # Met à jour l'état de toutes les cellules de la grille
        for case in self.Tab_Cases:
            if self.Tab_Etats[case.y][case.x] == 0:
                case.set_etat(0)
            elif self.Tab_Etats[case.y][case.x] == 1:
                case.set_etat(1)

            # Met à jour la couleur de la case correspondante
            case.update_couleur()



if __name__ == "__main__":
    NB_COLONNES = 25
    NB_LIGNES = 20
    COTE = 20

    App = Appli(NB_LIGNES, NB_COLONNES)
    App.resizable(width=False,height=False)

    frame_cases = Frame(App)
    frame_cases.place(x=10, y=10, width = 580, height = 500)

    # Initialisation des tableaux
    #Tab_Etats = [[0 for i in range(App.nb_colonnes)] for j in range(App.nb_lignes)] # Tableaux d'états (0 ou 1)
    #Tab_Cases = [] # Tableau de cases

    # Tirage aléatoire des cellules vivantes
    Genere_Grille(App.nb_lignes, App.nb_colonnes, App.get_Tab_Etats())

    # Création des cases représentant les cellules
    for i in range(App.nb_lignes):
        for j in range(App.nb_colonnes):
            case = Case(frame_cases, j, i)
            if App.get_Tab_Etats()[i][j] == 0:
                case.config(height = 1, width = 2, bg = "black", fg = "green", image=None, command=case.inverse_etat)
                # L'état par défaut de la case est 0 (cellule morte), il n'y a donc pas de maj à faire
            else:
                case.config(height = 1, width = 2, bg = "white", fg = "green", image=None, command=case.inverse_etat)
                case.set_etat(1) # Maj de l'état de la cellule : passage à vivante
            App.Tab_Cases.append(case)
            #case.grid(row=i, column=j)
            case.place(x=COTE*j, y = COTE*i, height = COTE, width = COTE)

    App.mainloop()