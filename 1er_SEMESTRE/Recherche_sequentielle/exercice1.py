"""
    Cours : Recherche séquentielle
    Exercice : Recherche d'extrema et aléas informatiques
"""
from math import inf
import random
import matplotlib.pyplot as plt


def min1(L):
    """ Q1 : Écrire une fonction min1(L) qui prend en entrée une liste L non vide et renvoie le tuple (m,i)
    correspondant au minimum et à son indice d'occurrence. On veillera à ce que i corresponde à l'indice de la dernière
    occurrence de m dans L"""
    i, m = 0, L[0]
    for indice, valeur in enumerate(L):
        if valeur <= m:  # Si inférieur strict, on garde en mémoire la première occurrence du min
            i, m = indice, valeur
    return i, m


def min12(L):
    """ Q2 : Écrire une fonction min12(L) qui prend en entrée une liste L de longueur supérieure à 2, et renvoie les
    indices de dernière occurrence et les valeurs des deux plus petits éléments distincts de la liste."""
    i1, i2, m1, m2 = 0, 0, L[0], inf
    for indice, valeur in enumerate(L):
        if valeur < m1:
            m1, m2, i1, i2 = valeur, m1, indice, i1
        elif valeur == m1:
            i1 = indice
        elif valeur <= m2:
            m2, i2 = valeur, indice
    return i1, i2, m1, m2


def histogramme1():
    """ Q3 : À l'aide de la fonction randint(), générer une liste L de 100 entiers compris entre 1 et 100"""
    L = [random.randint(1, 100) for _ in range(100)]
    plt.figure()
    plt.hist(L, 100, edgecolor='white')
    plt.show()


def histogramme2():
    """ Q4 : La question précédente correspond à un tirage aléatoire. On souhaite maintenant représenter l'évolution du 
    nombre d'occurrences de chaque entier sur un grand nombre de tirages aléatoires. Reproduire le graphique de la 
    question précédente en cumulant les occurrences de chaque entier sur 100 puis 1000 tirages. On stockera le 
    nombre total d'apparitions de chaque entier dans un dictionnaire. Commenter"""
    dic_occur = {}
    tirages = 100
    for _ in range(tirages):
        L = [random.randint(1, 100) for _ in range(100)]
        for k in L:
            if k in dic_occur.keys():
                dic_occur[k] += 1
            else:
                dic_occur[k] = 1

    plt.bar(list(dic_occur.keys()), list(dic_occur.values()))
    plt.ylabel("Nombre d'occurrences")
    plt.xlabel('#')
    plt.title("Histogramme du nombre d'occurrences ({} tirages)".format(tirages))
    plt.show()


if __name__ == '__main__':
    print(min12([68, 27, 55, 47, 55, 5, 74, 88, 99, 30]))
    histogramme1()
    histogramme2()