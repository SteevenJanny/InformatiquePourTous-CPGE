"""
    Cours : Algorithme de tri
    Exercice : Problème du drapeau hollandais
"""
import random as rd
import time as t
import numpy as np
import matplotlib.pyplot as plt


def genere_liste(N, n):
    """ Q1 : Définir une fonction genere_liste(N, n) qui génère une liste L de N nombres qui peuvent prendre n valeurs
    distinctes (de 0 à n-1)."""
    L = []
    for _ in range(0, N):  # on utilise "_" lorsqu'on n'a pas besoin d'indice de boucle
        L.append(rd.randint(0, n - 1))
    return L


def tri_drapeau_hollandais(L):
    """ Q2 : Implémenter une fonction tri_drapeau_hollandais(L) qui renvoie la liste L triée par l'algorithme précédent.
    Vérifier son bon fonctionnement sur une petite liste."""
    # tri comptage
    maxL = max(L)  # on part du principe qu'on ne connait pas le nombre de valeurs possibles
    table_comptage = [0 for _ in range(maxL + 1)]
    for x in L:  # on parcourt la liste
        table_comptage[x] += 1  # incrémentation de la valeur correspondante
    L_tri = []
    for i in range(maxL + 1):  # génération de la liste triée
        for _ in range(table_comptage[i]):
            L_tri.append(i)  # on met autant de i qu'on a comptés dans la table de comptage
    return L_tri


def tri_drapeau_hollandais2(L):
    """ Q3 :  Ecrire une fonction tri_drapeau_hollandais2(L), basée sur le tri rapide. On veillera à ce que son
    implémentation soit stable."""
    # Tri rapide
    if len(L) <= 1:
        return L
    else:
        p = choix_pivot(L)
        Tg, valp, Td = partitionner(L, p)  # + concatène les listes
        return tri_drapeau_hollandais2(Tg) + valp + tri_drapeau_hollandais2(Td)


def choix_pivot(L):
    return rd.randint(1, len(L) - 1)


def partitionner(L, p):
    Lp = L[p]  # valeur du pivot
    valp, Tg, Td = [], [], []
    for i in range(0, len(L)):
        if L[i] < Lp:  # remplissage du sous-tableau à gauche du pivot
            Tg.append(L[i])
        elif L[i] == Lp:  # remplissage du  sous-tableau des valeurs égales au pivot
            valp.append(Lp)
        else:  # remplissage du  sous-tableau à droite du pivot
            Td.append(L[i])
    return Tg, valp, Td


def compare():
    """ Q5 : Tracer les temps de calcul de ces deux algorithmes pour différentes tailles de listes à trier à l'aide du
    module time."""
    # Tracé du temps de tri en fonction de la taille de la liste
    N = np.logspace(5, 7, 5).astype(int)
    t_comptage = []
    t_rapide = []

    for n in N:
        L = genere_liste(n, 3)
        t1 = t.time()
        tri_drapeau_hollandais(L)
        t_comptage.append(t.time() - t1)
        t1 = t.time()
        tri_drapeau_hollandais2(L)
        t_rapide.append(t.time() - t1)

    plt.figure()
    plt.loglog(N, t_comptage, ':k', N, t_rapide, '-k')
    plt.title('Temps de calcul - tri drapeau hollandais')
    plt.xlabel('Taille de la liste')
    plt.ylabel('T (s)')
    plt.legend(["comptage", "rapide"])
    plt.grid()
    plt.show()


def compare_nlist():
    N = 1000000
    nlist = np.linspace(2, 25, 10).astype(int)
    t_comptage = []
    t_rapide = []

    for n in nlist:
        L = genere_liste(N, n)
        t1 = t.time()
        tri_drapeau_hollandais(L)
        t_comptage.append(t.time() - t1)
        t1 = t.time()
        tri_drapeau_hollandais2(L)
        t_rapide.append(t.time() - t1)
        print(n)

    plt.figure()
    plt.plot(nlist, t_comptage, ':k', nlist, t_rapide, '-k')
    plt.title('Temps de calcul - Liste de 1e6 éléments')
    plt.xlabel('Nombre de termes différents')
    plt.ylabel('T (s)')
    plt.legend(["comptage", "rapide"])
    plt.grid()
    plt.show()


if __name__ == '__main__':
    print(tri_drapeau_hollandais([0, 4, 3, 2, 5, 4, 6]))
    print(tri_drapeau_hollandais2([0, 4, 3, 2, 5, 4, 6]))
    compare()
    compare_nlist()