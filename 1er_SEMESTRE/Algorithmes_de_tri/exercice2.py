"""
    Cours : Algorithme de tri
    Exercice : Orientation d'un maillage
"""
from maillage import NOEUDS, TRIANGLES
import matplotlib.pyplot as plt
import random as rd
import time as t
import numpy as np


def trace_maillage_ref(triangles, noeuds):
    """ Q1 : Récupérer le maillage et écrire une fonction trace_maillage_ref(triangles, noeuds) de manière à afficher
    la figure de l'énoncé."""
    Nt = len(triangles)
    Nn = len(noeuds)
    plt.figure()
    for i in range(0, Nt):  # on trace d'abord les arêtes de chaque triangle
        x = noeuds[triangles[i, [0, 1, 2, 0]] - 1, 0]
        y = noeuds[triangles[i, [0, 1, 2, 0]] - 1, 1]
        plt.plot(x, y, 'k')
    for i in range(0, Nn):  # on affiche ensuite les numéros des noeuds
        plt.text(noeuds[i, 0] + 1e-2, noeuds[i, 1] + 1e-2, i)
    plt.title('Maillage de référence')
    plt.show()


def trace_maillage_orientation(triangles, noeuds):
    """ Q2 : Ecrire une fonction trace_maillage_orientation(triangles, noeuds) permettant d'afficher l'orientation
    locale des arêtes du maillage pour chaque triangle"""
    N = len(triangles)
    plt.figure()
    for i in range(0, N):
        x = noeuds[triangles[i, [0, 1, 2, 0]] - 1, 0]
        y = noeuds[triangles[i, [0, 1, 2, 0]] - 1, 1]
        plt.plot(x, y, 'k')  # tracé du triangle
        u = x[[1, 2, 2]] - x[[0, 1, 0]]
        v = y[[1, 2, 2]] - y[[0, 1, 0]]
        plt.quiver((x[0:3] + x[1:4]) / 2, (y[0:3] + y[1:4]) / 2, u, v, angles='xy', scale=3)  # tracé des orientations


def tri_insertion(T):
    """ Q3 : Quelle fonction de tri vous semble la plus adaptée pour résoudre le problème posé à la question précédente?
    Vérifier votre code en affichant l'orientation des arêtes à partir de la table de connectivité triée. Il faut
    obtenir l'image ci-contre"""
    N = len(T)
    for i in range(1, N):
        t = T[i]
        j = i
        while j > 0 and T[j - 1] > t:
            T[j] = T[j - 1]
            j = j - 1
        T[j] = t
    return T


def genere_table(N, n):
    """ Q4 : Ecrire une fonction genere_table(N, n) qui génère une table de N lignes et n colonnes, comportant des
    entiers choisis aléatoirement entre 1 et N"""
    T = []
    for i in range(0, N):
        T.append([])
        for _ in range(0, n):
            T[i] += [rd.randint(0, N)]
    return T


def tri_fusion(T):
    def fusion(T1, T2):
        if len(T1) == 0:
            return T2
        elif len(T2) == 0:
            return T1
        elif T1[0] <= T2[0]:
            return [T1[0]] + fusion(T1[1:], T2)
        else:
            return [T2[0]] + fusion(T1, T2[1:])

    if len(T) <= 1:
        return T
    else:
        idmid = int(len(T) / 2)
        return fusion(tri_fusion(T[0:idmid]), tri_fusion(T[idmid:]))
    return T


# tracé en fonction du nombre d'éléments N (listes à trier)
def demo_fusion():
    """ Q5 : A l'aide de la fonction time(), comparer les performances de votre algorithme avec celles du tri fusion 
    (que vous implémenterez) en fonction de N, puis en fonction de n. Conclure."""
    N = np.logspace(3.5, 6, 10).astype(int)
    T_fusion = []
    T_insertion = []
    for n in N:
        T = genere_table(n, 3)
        t1 = t.time()
        for i in range(0, n):
            tri_fusion(T[i])
        T_fusion.append(t.time() - t1)
        T = genere_table(n, 3)
        t1 = t.time()
        for i in range(0, n):
            tri_insertion(T[i])
        T_insertion.append(t.time() - t1)
        print(n)

    plt.figure()
    plt.loglog(N, T_insertion, 'k', N, T_fusion, ':k')
    plt.xlabel('N')
    plt.ylabel('T (s)')
    plt.title('Temps de tri en fonction de N (n=3)')
    plt.legend(["insertion", "fusion"])
    plt.grid()
    plt.show()

    # tracé en fonction du nombre de sommets n (taille des listes)

    N = 1000
    n_sommets = np.logspace(0.5, 2, 10).astype(int)
    T_fusion = []
    T_insertion = []
    for n in n_sommets:
        T = genere_table(N, n)
        t1 = t.time()
        for i in range(0, N):
            tri_fusion(T[i])
        T_fusion.append(t.time() - t1)
        t1 = t.time()
        for i in range(0, N):
            tri_insertion(T[i])
        T_insertion.append(t.time() - t1)
        print(n)

    plt.figure()
    plt.loglog(n_sommets, T_insertion, 'k', n_sommets, T_fusion, ':k')
    plt.xlabel('n')
    plt.ylabel('T (s)')
    plt.title('Temps de tri en fonction de n (N=1000)')
    plt.legend(["insertion", "fusion"])
    plt.grid()
    plt.show()


if __name__ == '__main__':
    trace_maillage_ref(TRIANGLES, NOEUDS)
    trace_maillage_orientation(TRIANGLES, NOEUDS)
    plt.title('Orientations du maillage original')
    plt.show()

    for i in range(0, len(TRIANGLES)):
        TRIANGLES[i, :] = tri_insertion(TRIANGLES[i, :])

    trace_maillage_orientation(TRIANGLES, NOEUDS)
    plt.title('Orientations du maillage trié')
    plt.show()

    demo_fusion()
