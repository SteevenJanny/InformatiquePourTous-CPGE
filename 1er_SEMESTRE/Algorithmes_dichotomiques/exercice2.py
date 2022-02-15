"""
    Cours : Algorithmes dichotomiques
    Exercice : Exponentiation rapide
"""
from time import time
import matplotlib.pyplot as plt
import numpy as np


def expoNaive(x, p):
    """ Q1 : Coder la fonction d'exponentiation naïve."""
    resultat = 1
    for k in range(p):
        resultat *= x
    return resultat


def expoRapide(x, p):
    """ Q2 : Coder la fonction d'exponentiation rapide."""
    resultat = 1
    while p != 0:  # Tant que p est non nul
        if p % 2 == 1:  # Si p est impair
            resultat *= x
        x = x * x
        p = p // 2  # Division entière
    return resultat


def mesure_temps(f, x, p):
    """ Q3 : Comparer la durée d'exécution des deux algorithmes (rapide et naïf) en fonction de la valeur de p."""
    t = time()
    for k in range(300):  # on fait 300 fois le même calcul pour avoir plus de précision car
        r = f(x, p)  # les temps d'exécution sont très très petits
    return time() - t


if __name__ == '__main__':
    x = 1.1  # on choisit exprès un flottant (pas un entier) car ses puissances seront + longues à calculer
    temps_naif, temps_rapide = [], []
    valeurs_p = np.logspace(2, 4, 100).astype(int)
    for p in valeurs_p:
        temps_naif.append(mesure_temps(expoNaive, x, p))
        temps_rapide.append(mesure_temps(expoRapide, x, p))

    # Affichage des résultats en échelle log sur l'ordonnée
    plt.semilogy(valeurs_p, temps_naif, '--', c="black")
    plt.semilogy(valeurs_p, temps_rapide, c="black")

    # Décorations
    plt.legend(["Naive", "Rapide"])
    plt.title("Temps d'exécution des methodes \n d'exponentiation rapide et naive")
    plt.xlabel("p")
    plt.ylabel("Temps (seconde)")
    plt.grid()

    plt.show()
