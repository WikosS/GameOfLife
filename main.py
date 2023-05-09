from random import randint

def Genere_Grille(nb_lignes, nb_colonnes, Tab):
    """ Fonction Genere_Grille :
        Génère une grille aléatoire représsentée par un tableau.
        Le tableau généré ne doit contenir que des 0 ou des 1.
        0 correspond à une cellule morte et 1 à une cellule vivante.
        Paramètres : - nb_lignes - Entier - IN - Nombre de lignes de la grille
                     - nb_colonnes - Entier - IN - Nombre de colonnes de la grille
                     - Tab - Tableau d'entiers - OUT - Tableau contenant des 0 et des 1
        Valeur de retour : Aucune
        Préconditions : - nb_lignes est un entier strictement positif
                        - nb_colonnes est un entier strictement positif
                        - Le tableau Tab a déjà été initialisé et correctement dimensionné
                        (nb_lignesxnb_colonnes)
        Postconditions : - nb_lignes et nb_colonnes ne sont pas modifiées
                         - Tab contient des 0 et des 1 générés aléatoirement"""
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            Tab[i][j] = randint(0, 1)
Genere_Grille(3,5, [2,4])

def est_vivante(Tab, l, c):
    """ Fonction est_vivante :
        Détermine si une cellule de la grille est vivante, c'est à dire
        si la case associée sur la grille contient un 1.
        Paramètres : - Tab - Tableau d'entiers - IN - La grille de cellules
                     - l - Entier - IN - L'indice de ligne de la cellule à tester dans Tab (commence à 0)
                     - c - Entier - IN - L'indice de colonne de la cellule à tester (commence à 0)
        Valeur de retour : Booléen - True si la cellule Tab[l][c] est vivante, False sinon
        Préconditions : - Tab contient la grille des cellules : c'est un tableau à deux dimensions
                        contenant des 0 et des 1
                        - l est un entier compris entre 0 et le nombre de lignes de Tab
                        - c est un entier compris entre 0 et len(Tab[0]) - 1 le nombre de colonnes de Tab
        Postconditions : - Tab, l et c ne sont pas modifiées par la fonction
                         - La valeur de retour de la fonction est True si la cellule Tab[l][c] est vivante,
                         False sinon"""
    assert type(l) == int and type(c) == int and l >= 0 and c >= 0
    if Tab[c][l] == 0:
        return False
    return True



def Compte_Cellules_Vivantes_Voisines(Tab, l, c, nb_lignes, nb_colonnes):
    """ Fonction Compte_Cellules_Vivantes_Voisines :
        Pour une cellule donnée, compte le nombre de cellules vivantes parmi ses 8 voisines
        Paramètres : - Tab - Tableau d'entiers - IN - La grille de cellules
                     - l - Entier - IN - L'indice de ligne de la cellule à tester dans Tab (commence à 0)
                     - c - Entier - IN - L'indice de colonne de la cellule à tester (commence à 0)
                     - nb_lignes - Entier - IN - Nombre de lignes de la grille
                     (sert à s'assurer qu'on ne dépasse pas de la grille)
                     - nb_colonnes - Entier - IN - Nombre de colonnes de la grille
                       (sert à s'assurer qu'on ne dépasse pas de la grille)
        Valeur de retour : Entier - Le nombre de cellules vivantes parmi les voisines de la cellule donnée
        Préconditions : - Tab contient la grille des cellules : c'est un tableau à deux dimensions
                        contenant des 0 et des 1. Il possède nb_lignes lignes et nb_colonnes colonnes
                        - l est un entier compris entre 0 et le nombre de lignes de Tab
                        - c est un entier compris entre 0 et len(Tab[0]) - 1 le nombre de colonnes de Tab
                        - nb_lignes est un entier strictement positif
                        - nb_colonnes est un entier strictement positif
        Postconditions : - Aucun paramètre n'est modifié par la fonction
                         - La valeur de retour de la fonction est le nombre de cellules vivantes parmi
                           les voisines de la cellule considérée"""
    assert type(l) == int and type(c) == int and type(nb_lignes) == int and type(nb_colonnes) == int
    total = 0

    #Genere la liste des case adjacente
    voisin = []
    x = -1
    y = -1
    for i in range(3):
        for i in range(3):
            if nb_colonnes > l+x >= 0  and nb_lignes > c+y >= 0 and not x == y == 0: # vérifie que les coordonée du voisin soit valide
                voisin.append([l+x, c+y]) # puis l'ajoute a la liste
            x += 1
        x = -1
        y += 1
    for i in voisin:
        if est_vivante(Tab, i[0], i[1]): #vérifie si le voisin actuelle est mort ou pas
            total += 1
    return total




def Calcule_nouvelle_iteration(Tab, nb_lignes, nb_colonnes):
    """ Fonction Calcule_nouvelle_iteration :
        Détermine l'état de toutes les cellules à l'itération suivante
        Paramètres : - Tab - Tableau d'entiers - IN/OUT - La grille de cellules
                     - nb_lignes - Entier - IN - Nombre de lignes de la grille
                     - nb_colonnes - Entier - IN - Nombre de colonnes de la grille
        Valeur de retour : Aucune
        Préconditions : - Tab contient la grille des cellules : c'est un tableau à deux dimensions
                        contenant des 0 et des 1. Il possède nb_lignes lignes et nb_colonnes colonnes
                        - nb_lignes est un entier strictement positif
                        - nb_colonnes est un entier strictement positif
        Postconditions : - nb_lignes et nb_colonnes ne sont pas modifiées
                         - Tab est mis à jour avec le nouvel état des cellules"""
    OldTab = Tab[:] # Sauvegarde la grille actuelle en la copiant ds un nouveau tableau
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            if not est_vivante(Tab, j, i):
                if Compte_Cellules_Vivantes_Voisines(Tab, j, i , nb_lignes, nb_colonnes) == 3:
                    Tab[j][i] = 1
            else:
                if not Compte_Cellules_Vivantes_Voisines(Tab, j, i , nb_lignes, nb_colonnes) == 2 or Compte_Cellules_Vivantes_Voisines(Tab, j, i , nb_lignes, nb_colonnes) == 3:
                    Tab[j][i] = 0
