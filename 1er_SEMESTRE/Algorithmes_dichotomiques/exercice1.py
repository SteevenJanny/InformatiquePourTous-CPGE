"""
    Cours : Algorithmes dichotomiques
    Exercice : Un chauffage optimal
"""
from random import randint
import numpy as np
import matplotlib.pyplot as plt

SUP, INF = 1000, -1000


def genereSalle(N, K):
    """ Q1 : Coder une fonction genereSalle(N, K) qui renvoie deux listes représentant les positions des N tables et des
    K radiateurs."""
    tables = [(randint(INF, SUP), randint(INF, SUP)) for _ in range(N)]
    radiateurs = [(randint(INF, SUP), randint(INF, SUP)) for _ in range(K)]
    return np.array(tables), np.array(radiateurs)


def chauffeTous(tables, radiateurs, r):
    """ Q2 : Coder une fonction chauffeTous(tables, radiateurs, r) qui renvoie True si toutes les tables (de positions
    tables) sont chauffées par les radiateurs de positions radiateurs et de rayon d'action r, False sinon."""
    for t in tables:  # Pour chaque table
        est_chauffee = False
        for rad in radiateurs:
            if sum((t - rad) ** 2) < r ** 2:  # Si on trouve un radiateur assez proche
                est_chauffee = True
                break  # On arrête de chercher pour cette table t (on sort de la dernière boucle for)
        if not est_chauffee:  # Si on trouve une seule table non chauffée...
            return False  # ... inutile de continuer.
    return True


def solutionNaive(tables, radiateurs):
    """ Q3 : Proposer une borne supérieure pour r"""
    maximum = 0
    for b in tables:
        # On cherche le radiateur le plus proche de la table
        radiateurLePlusProche = np.inf
        for r in radiateurs:
            dist = np.sqrt(np.sum((b - r) ** 2))
            if dist < radiateurLePlusProche:
                radiateurLePlusProche = dist

        # Puis on cherche la plus grande distance minimale entre un radiateur et un bureau
        if radiateurLePlusProche > maximum:
            maximum = radiateurLePlusProche
    return maximum


def dichotomie(tables, radiateurs):
    """ Q4 : Résoudre le problème pour N=1000 tables et K=10 radiateurs"""
    G = 0
    D = np.sqrt(2) * 2000  # Borne supérieure
    while G < D:
        m = (G + D) / 2  # Calcul du milieu
        if chauffeTous(tables, radiateurs, m):  # Si il permet de chauffer toutes les tables
            D = m  # On cherche un rayon plus petit
        else:
            G = m + 1  # Sinon on cherche un rayon plus grand
    return m


def visu(tables, radiateurs, r):
    """ Q5 : Visualiser la réponse à l'aide de Matplotlib"""
    # Affichage des tables
    plt.scatter(tables[:, 0], tables[:, 1], s=2, label="tables", color="black")
    # Affichage des radiateurs
    plt.scatter(radiateurs[:, 0], radiateurs[:, 1], s=15, label="radiateurs", color="gray")
    # Dessine un cercle autour de chaque radiateur
    for rad in radiateurs:
        circle1 = plt.Circle(rad, r, color='black', fill=True, alpha=0.1)
        plt.gca().add_patch(circle1)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    b, r = genereSalle(100, 10)
    radius = dichotomie(b, r)
    visu(b, r, radius)
