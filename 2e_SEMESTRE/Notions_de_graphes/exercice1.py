"""
    Cours : Notion de graphe
    Exercice : Promotion du tourisme local
"""
import numpy as np
import queue

# Le plan P1 est constitué de 12 villes et 7 lignes LGV
matrixAdj_P1 = np.array([[0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
plan_P1 = [[12, 7],
           [5, 2, 3, 4, 5, 6] + 5 * [None],
           [1, 1] + 9 * [None],
           [1, 1] + 9 * [None],
           [2, 1, 8] + 8 * [None],
           [2, 1, 7] + 8 * [None],
           [1, 1] + 9 * [None],
           [1, 5] + 9 * [None],
           [1, 4] + 9 * [None],
           [0] + 10 * [None],
           [0] + 10 * [None],
           [0] + 10 * [None],
           [0] + 10 * [None], ]


def matrice_from_plan(plan):
    """ Q2 : Écrire une fonction plan_from_matrice(matrixAdj) qui renvoie le tableau de tableaux correspondant à la
    matrice d'adjacence matrixAdj"""
    nbVilles = plan[0][0]  # Taille matrice d'adjacence
    matrice = np.zeros((nbVilles, nbVilles))
    for i in range(1, nbVilles + 1):  # parcourt des n villes du plan
        nbVoisins = plan[i][0]
        voisins = plan[i][1:nbVoisins + 1]  # tableau des villes voisines
        for j in voisins:
            matrice[i - 1, j - 1] = 1  # indique que les villes i, j sont adjacentes
    return matrice


def plan_from_matrice(matrixAdj):
    """ Q3 : Réciproquement, écrire une fonction matrice_from_plan(plan) qui renvoie la matrice d'adjacence
    correspondant à plan."""
    nbVilles = len(matrixAdj)
    m = np.sum(matrixAdj) // 2  # Il y a deux fois plus de 1 que de chemins
    plan = [[nbVilles, m]]  # Initialisation du plan
    for i in range(nbVilles):
        # Liste des voisins de la ville i
        voisins = [(j + 1) for j in range(nbVilles) if matrixAdj[i, j] == 1]
        # Création du plan pour la ville i
        plan_i = [len(voisins)] + voisins + (nbVilles - len(voisins)) * [None]
        # Ajout au plan principal
        plan.append(plan_i)  # Ajout au plan
    return plan


def est_adjacent(plan, i, j):
    """ Q4 : Écrire une fonction est_adjacent(plan, i, j) qui renvoie True si x_i et x_j sont adjacents, et False
    sinon."""
    liste_voisins = plan[i][1:]  # On retire le nombre de villes de la liste
    return j in liste_voisins


def parcoursProfondeur(plan, i):
    """ Q5 : Écrire une fonction parcours(plan, i) qui renvoie la liste de toutes les villes accessibles à partir de
    la ville x_i pour le plan donné. """
    parcourues = []
    pile = queue.Queue()
    pile.put(i)
    while pile.qsize():
        j = pile.get()  # On extrait le 1er élément à droite
        if j not in parcourues:
            parcourues.append(j)
            nbVoisins = plan[j][0]
            nouveaux_voisins = [k for k in plan[j][1:nbVoisins + 1] if k not in parcourues]
            for v in nouveaux_voisins:
                pile.put(v)
    return parcourues


def parcoursLargeur(plan, i):
    parcourues = []
    file = queue.LifoQueue()
    file.put(i)
    while file.qsize():
        j = file.get()  # on extrait le dernier élément à gauche
        if j not in parcourues:
            parcourues.append(j)
            nouveaux_voisins = [k for k in plan[j][1:plan[j][0] + 1] if k not in parcourues]
            for v in nouveaux_voisins:
                file.put(v)
    return parcourues


def existe_chemin(plan, i, j):
    """ Q6 : À partir de la fonction précédente, coder  une fonction existe_chemin(plan, i, j) qui renvoie True si un
    chemin relie x_i et x_j et False sinon."""
    if i == j:
        return False
    parcourues = []
    pile = queue.Queue()
    pile.put(i)
    while pile.qsize():
        new = pile.get()
        if new == j:
            return True
        if new not in parcourues:
            parcourues.append(new)
            nouveaux_voisins = [k for k in plan[new][1:plan[new][0] + 1] if k not in parcourues]
            for v in nouveaux_voisins:
                pile.put(v)
    return False


def trouve_chemin(plan, i, j):
    """ Q7 : À partir de la fonction précédente, coder une fonction trouve_chemin(plan, i, j) qui, dans le cas où un
    chemin de longueur k relie les villes x_i et x_j, renvoie une liste de longueur k+1 contenant les villes par
    lesquelles passent le chemin."""
    pile = queue.Queue()
    pile.put((i, [i]))
    while pile.qsize():
        (new, chemin) = pile.get()
        if new == j:
            return chemin
        voisins = [k for k in plan[new][1:plan[new][0] + 1] if k not in chemin]
        for v in voisins:
            new_chemin = chemin + [v]
            pile.put((v, new_chemin))


def nouvelle_ligne(plan, i, j):
    """ Q8 : Écrire une procédure nouvelle_ligne(plan, i, j) qui modifie plan en ajoutant un chemin entre les villes x_j
     et x_i. On veillera à éviter les redondances."""
    if (i != j) and not (est_adjacent(plan, i, j)):
        plan[0][1] += 1  # Nombre global de lignes augmente

        # Ajout de nouveau voisin pour i
        plan[i][plan[i][0] + 1] = j
        plan[i][0] += 1

        # ajout de nouveau voisin pour j
        plan[j][plan[j][0] + 1] = i
        plan[j][0] += 1


def reseau_total(plan):
    """ Q9 : Écrire une procédure reseau_total(plan) qui affiche la liste des lignes existante (exactement une seule 
    fois)."""
    nbVilles, nbChemins = plan[0]
    print(f"Le réseau comprend {nbChemins} lignes LGV: ")
    for i in range(1, nbVilles + 1):
        nbVoisins = plan[i][0]
        for j in range(1, nbVoisins + 1):
            if plan[i][j] > i:  # Garantit qu'on évite les doublons
                print(f"({i} - {plan[i][j]}) ", end='')  # Permet d'éviter le retour à la ligne


if __name__ == '__main__':
    plan_P2 = []
    for i in range(0, len(plan_P1)):
        plan_P2.append(plan_P1[i].copy())

    nouvelle_ligne(plan_P2, 3, 4)
    nouvelle_ligne(plan_P2, 8, 9)
    nouvelle_ligne(plan_P2, 8, 10)
    nouvelle_ligne(plan_P2, 7, 10)
    nouvelle_ligne(plan_P2, 5, 11)
    nouvelle_ligne(plan_P2, 6, 11)
    nouvelle_ligne(plan_P2, 6, 12)

    reseau_total(plan_P1)
