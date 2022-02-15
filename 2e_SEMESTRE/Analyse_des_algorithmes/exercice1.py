"""
    Cours : Analyse des algorithmes
    Exercice : Recherche de la somme minimale des coupes d'une liste
"""
from random import randint
from time import time


def somme(x, i, j):
    S = 0
    for k in range(i, j):
        S += x[k]
    return S


def somme_minimale1(x):
    """ Q1 : Un algorithme au coût cubique"""
    minimum = x[0]
    for i in range(len(x)):
        for j in range(i + 1, len(x) + 1):
            S = somme(x, i, j)
            if S < minimum:
                minimum = S
    return minimum


def somme_minimale2(x):
    """ Q1 : Un algorithme au coût quadratique"""
    minimum = x[0]
    for i in range(len(x)):
        s_min = somme_mini_debut(x, i)
        if s_min < minimum:
            minimum = s_min
    return minimum


def somme_mini_debut(x, i):
    S = x[i]
    minimum = x[i]
    for j in range(i + 1, len(x)):
        S += x[j]
        if S < minimum:
            minimum = S
    return minimum


def somme_minimale3(x):
    """ Q1 : Un algorithme au coût linéaire"""
    m = x[0]
    p = x[0]
    for i in range(1, len(x)):
        p = min(p + x[i], x[i])
        m = min(m, p)
    return m


if __name__ == '__main__':
    x1 = [randint(-100, 100) for _ in range(1000)]

    t = time()
    somme_minimale1(x1)
    print("Somme minimale 1 : ", time() - t)

    t = time()
    somme_minimale2(x1)
    print("Somme minimale 2 : ", time() - t)

    t = time()
    somme_minimale3(x1)
    print("Somme minimale 3 : ", time() - t)
