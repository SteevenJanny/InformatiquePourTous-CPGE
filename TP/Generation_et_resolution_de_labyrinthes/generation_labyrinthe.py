"""
    TP : Génération et résolution de labyrinthes
"""

import numpy as np
import turtle as tt
import random as rd
import matplotlib.pyplot as plt


def set_initial_grid(H, L):
    """" Q1 : Ecrire une fonction set_initial_grid(largeur, hauteur) qui génère un tableau initial rempli de zéros à
    l'exception de deux cases contenant 1, et représentant l'entrée et la sortie du labyrinthe. On les placera
    arbitrairement sur le bord, en veillant à ce qu'elles ne soient adjacentes à une pièce et non à un mur."""
    assert (H % 2 == 1 and L % 2 == 1)  # on vérifie que H et L sont impairs
    assert (H >= 3 and L >= 3)  # On veut un labyrinthe non trivial (de plus d'une case)
    grid = np.zeros((H, L))  # génération du tableau de 0
    grid[0, 1], grid[-1, -2] = 1, 1  # on place l'entrée et la sortie
    return grid


def check_voisinage(lab, pos):
    """ Q2 : Ecrire une fonction check_voisinage(labyrinthe, position) qui, à partir de l'array représentant labyrinthe
    et du couple d'indices position permettant de repérer la case courante dans labyrinthe renvoie la liste des
    positions des cases inexplorées adjacentes."""
    H, L = lab.shape  # récupère les dimensions du labyrinthe
    X, Y = pos
    positions_possibles = []
    #  Les positions possibles doivent être inexplorées et à l'intérieur du labyrinthe :
    deplacements = [[-2, 0], [2, 0], [0, 2], [0, -2]]
    for (dx, dy) in deplacements:
        if 0 <= X + dx < H and 0 <= Y + dy < L:
            if lab[X + dx, Y + dy] == 0:
                positions_possibles.append(pos + np.array((dx, dy)))
    return positions_possibles


def explore(lab, pos, active_trace=False):
    """ Q3 : Implémenter une fonction explore(labyrinthe,position) qui à partir d'une case courante du tableau
     labyrinthe repérée par ses indices contenus dans le tuple position, renvoie le labyrinthe généré selon la
     procédure de parcours en profondeur."""
    for i in range(3):  # 3 positions adjacentes inexplorées maximum
        positions_possibles = check_voisinage(lab, pos)
        if len(positions_possibles) == 0: break  # on est dans une impasse !
        new_pos = rd.choice(positions_possibles)  # choix au hasard d'une case
        lab[new_pos[0], new_pos[1]] = 1  # on la marque comme explorée
        pos_mur = (new_pos + pos) // 2  # on casse le mur entre l'ancienne ...
        lab[pos_mur[0], pos_mur[1]] = 1  # ... et la nouvelle case
        if active_trace:
            trace(pos, new_pos)
        lab = explore(lab, new_pos)  # on continue l'exploration à partir de la nouvelle case
    return lab


def init_kruskal(H, L):
    """ Q4 : Écrire une fonction d'initialisation init_kruskal(largeur, hauteur) qui renvoie le tableau initial de
     Kruskal décrit au paragraphe précédent. Comme toutes les pièces sont initialement isolées, chaque case du tableau
     associée à une pièce doit contenir une valeur unique et strictement positive."""
    grid_init = set_initial_grid(H, L)
    cle = 2
    for i in range(1, H, 2):
        for j in range(1, L, 2):
            grid_init[i, j] = cle
            cle += 1
    return grid_init


def check_directions_kruskal(labyrinthe, position):
    """ Q5 : Écrire une fonction check_directions_kruskal(labyrinthe,position) qui, à partir du tableau labyrinthe et
     de la position du mur position, renvoie 1 si les cases à gauche et à droite sont des chemins non-connectés, 2 si
     les cases en haut et en bas sont des chemins non-connectés et 0 sinon."""
    i, j = position
    if i % 2 == 1:  # gauche / droite
        gauche, droite = labyrinthe[i, j + 1], labyrinthe[i, j - 1]
        return 1 if gauche != droite else 0
    else:  # haut / bas
        haut, bas = labyrinthe[i + 1, j], labyrinthe[i - 1, j]
        return 2 if haut != bas else 0


def find_replace(labyrinthe, oldval, newval):
    """ Q6 : Implémenter une fonction find_replace(labyrinthe, oldval, newval) qui remplace dans le tableau labyrinthe
     toutes les valeurs égales à oldval par newval."""
    H, L = labyrinthe.shape
    for i in range(H):
        for j in range(L):
            if labyrinthe[i, j] == oldval:
                labyrinthe[i, j] = newval
    return labyrinthe


def genere_kruskal(H, L, active_trace=False):
    """ Q7 : Implémenter une fonction genere_Kruskal(hauteur, largeur) qui génère un labyrinthe par l'algorithme de Kruskal.
    On pourra utiliser random.shuffle qui mélange les termes d'une liste."""
    lab = init_kruskal(H, L)
    # on génère les indices des murs susceptibles d'être abattus, en version courte :
    murs = [(i, j) for i in range(1, H - 1) for j in range(1 + i % 2, L - 1, 2)]
    rd.shuffle(murs)  # mélange les termes de la liste "murs"
    for i, j in murs:
        if check_directions_kruskal(lab, (i, j)) == 1:
            lab[i, j] = lab[i, j + 1]
            lab = find_replace(lab, lab[i, j - 1], lab[i, j + 1])
            if active_trace:
                trace([i, j - 1], [i, j + 1])
        elif check_directions_kruskal(lab, (i, j)) == 2:
            lab[i, j] = lab[i + 1, j]
            lab = find_replace(lab, lab[i - 1, j], lab[i + 1, j])
            if active_trace:
                trace([i - 1, j], [i + 1, j])
    return find_replace(lab, np.max(lab), 1)  # on ne veut que des 0 et des 1


def trace(initcase, nextcase, size=5, offset=1):
    """ Q8 : Implémenter une fonction trace(initcase, nextcase) qui trace le chemin droit reliant la case de position initcase
     à la case de position nextcase, à l'aide des fonctions du module turtle."""
    initcase = size * np.array(initcase) + offset * np.array([-100, -100])
    nextcase = size * np.array(nextcase) + offset * np.array([-100, -100])
    tt.bgcolor("black")
    tt.pencolor("white")
    tt.pensize(size)
    tt.speed(10)
    tt.pu()
    tt.goto((initcase[1], -initcase[0]))
    tt.pd()
    tt.goto((nextcase[1], -nextcase[0]))


def check_voisinage_solve(lab, pos):
    positions_possibles = []
    if pos[0] > 1 and lab[pos[0] - 1, pos[1]] == 1:  # on doit vérifier pos[0]>1 à l'entrée
        positions_possibles.append(pos + np.array([-1, 0]))
    if lab[pos[0] + 1, pos[1]] == 1:
        positions_possibles.append(pos + np.array([1, 0]))
    if lab[pos[0], pos[1] + 1] == 1:
        positions_possibles.append(pos + np.array([0, 1]))
    if lab[pos[0], pos[1] - 1] == 1:
        positions_possibles.append(pos + np.array([0, -1]))
    return positions_possibles


def solve(lab, pos, sortie, active_plot=True):
    """ Q10 : En vous inspirant de la section 1.1, écrire une fonction récursive solve(lab, pos, sortie) qui cherche un
     chemin reliant la position courante pos dans le labyrinthe lab à la position sortie"""
    lab[pos[0], pos[1]] = 3  # a priori, le chemin courant est le bon
    if tuple(pos) == tuple(sortie):
        succes = True
        return lab, succes
    for i in range(3):
        if active_plot:
            plot_grid(lab)
        positions_possibles = check_voisinage_solve(lab, pos)
        if len(positions_possibles) == 0:  # on est dans une impasse
            succes = False  # on n'a donc pas réussi à trouver la sortie...
            lab[pos[0], pos[1]] = 2  # on marque ce chemin comme étant une impasse
            break
        new_pos = rd.choice(positions_possibles)  # positions_possibles[0] fonctionne
        lab, succes = solve(lab, new_pos, sortie)
        if succes:  # si l'exploration à la ligne précédente aboutit...
            break  # ... on s'arrête !
        else:
            lab[new_pos[0], new_pos[1]] = 2  # sinon, ce chemin mène à une impasse.
    return lab, succes


def plot_grid(labyrinthe):
    """ Q11 : Afficher la solution du labyrinthe et ses étapes de résolution à l'aide de plt.imshow (on affichera d'une
     couleur différente les chemins explorés du chemin retenu)."""
    plt.clf()  # permet d'effacer l'image précédente et d'améliorer les performances de l'animation
    plt.imshow(labyrinthe)
    plt.pause(0.01)  # permet de garder l'image à l'écran le temps de la voir


if __name__ == '__main__':
    # Génération de labyrinthe
    ## Parcours en profondeur
    labyrinthe = set_initial_grid(21, 21)
    labyrinthe = explore(labyrinthe, (1, 1), active_trace=False)

    # Attention, l'utilisation de matplotlib avant Turtle est déconseillée
    plt.figure()
    plt.imshow(labyrinthe)
    plt.title("Génération de Labyrinthe \n parcours en profondeur")
    plt.show()

    ## Algorithme de Kruskal
    labyrinthe = genere_kruskal(21, 21, active_trace=False)

    plt.figure()
    plt.imshow(labyrinthe)
    plt.title("Génération de Labyrinthe \n Algorithme de Kruskal")
    plt.show()

    # Résolution du labyrinthe
    _, succes = solve(labyrinthe, (0, 1), (20, 19), active_plot=True)
    plt.show()
