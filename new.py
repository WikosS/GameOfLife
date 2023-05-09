from random import randint

def Genere_Grille(nb_lignes, nb_colonnes, Tab):
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            Tab[i][j] = randint(0, 1)



def est_vivante(Tab, l, c):
    if Tab[l][c] == 1:
        return True
    return False



def Compte_Cellules_Vivantes_Voisines(Tab, l, c, nb_lignes, nb_colonnes):
    total = 0
    for i in range(max(0, l-1), min(nb_lignes, l+2)):
        for j in range(max(0, c-1), min(nb_colonnes, c+2)):
            if not (i, j) == (l, c):
                if est_vivante(Tab, i, j):
                    total += 1
    return total

def Calcule_nouvelle_iteration(Tab, nb_lignes, nb_colonnes):
    to_die = []
    to_live = []
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            cur_voisin = Compte_Cellules_Vivantes_Voisines(Tab, i, j , nb_lignes, nb_colonnes)
            if not est_vivante(Tab, i, j):
                if cur_voisin == 3:
                    to_live.append([i,j])
            elif est_vivante(Tab, i , j):
                if cur_voisin < 2 or cur_voisin > 3:
                    to_die.append([i,j])
    for k in to_die:
        Tab[k[0]][k[1]] = 0
    for e in to_live:
        Tab[e[0]][e[1]] = 1

