"""
    Cours : Plus court chemin dans un graphe
    Exercice : IA dans un jeu video
"""
import matplotlib.pyplot as plt
import numpy as np
import heapdict


def load_map(map_name):
    """ Q1 : À l'aide de la fonction imread de matplotlib, coder une fonction qui renvoie une grille rempli de zéros,
    excepté sur les cases blanches de l'image. La fonction prendra en entrée le nom du labyrinthe."""
    grille = plt.imread(f"{map_name}.png")
    grille = grille[:, :, 0]  # Ne garde qu'un seul canal
    grille = grille > 0.5  # Seuillage
    grille = grille.astype(int)  # Conversion en entier
    return grille


def get_voisins(grille, position):
    """ Q2 : Coder une fonction qui, pour une position donnée (i,j) dans l'image, renvoie la liste des voisins,
    c'est-à-dire la liste des positions accessibles par l'agent. Cette fonction prendra en paramètres la grille (une
    matrice 2D), ainsi que la position du pixel concerné (i, j)."""
    x, y = position  # Dépaquetage
    # Liste des cases voisines possibles
    next_positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    valid_voisins = []
    for p in next_positions:
        if 0 <= p[0] < 50 and 0 <= p[1] < 50:  # Si on ne sort pas des limites
            if grille[p[0], p[1]] == 1:  # Si la case n'est pas un mur
                valid_voisins.append(p)
    return valid_voisins


def heuristique(position):
    """ Q3 : Proposer et implémenter une fonction d'heuristique pertinente pour l'application de l'algorithme A*."""
    x, y = position
    return np.sqrt((x - 50) ** 2 + (y - 50) ** 2)


def plus_court_chemin(grille):
    """ Q4 : Utiliser l'algorithme A* pour trouver le plus court chemin entre le point de départ et celui d'arrivée."""
    distances = np.inf * np.ones_like(grille)  # Grille de distances
    distances[0, 0] = 0  # Départ
    P = heapdict.heapdict()  # File de priorité
    P[(0, 0)] = 0
    C = {}

    while len(P) > 0:
        V = P.popitem()[0]
        if V == (49, 49):  # Arrêt si le noeud cible est atteint
            return C
        for v in get_voisins(grille, V):
            d = distances[V] + 1
            estimation = d + heuristique(v)  # Utilisation heuristique
            if distances[v] > d:
                C[v] = V
                distances[v] = d
                P[v] = estimation
    return C


def plot_solution(grille, C):
    """ Q5 : Afficher ce chemin avec matplotlib"""
    # Calcul du chemin en partant de la fin
    position = [(49, 49)]
    while position[-1] != (0, 0):
        position.append(C[position[-1]])

    # coordonnées du chemin calculé
    X = [p[0] for p in position]  # liste par compréhension
    Y = [p[1] for p in position]

    plt.imshow(grille)  # Affiche image
    plt.plot(Y, X)  # Inversion Y et X à cause de l'image
    plt.show()


if __name__ == '__main__':
    carte = load_map('virage')
    C = plus_court_chemin(carte)
    plot_solution(carte, C)
