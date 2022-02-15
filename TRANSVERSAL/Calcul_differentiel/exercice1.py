"""
    Cours : Calcul différentiel
    Exercice : Vitesses de convergence de différentes méthodes d'intégration
"""
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    """ Q1 : Calculer analytiquement I_ref = int_0^1 f(x) dx$. Coder la fonction f(x) qui retourne la valeur de la
    fonction f pour un scalaire x, et tracer son graphe sur l'intervalle I."""
    return np.sin(10 * x) ** 2


def rectd(X, fX):
    """ Q2 : Coder en Python une fonction rectd(X,fX) qui retourne l'intégrale numérique calculée avec la méthode des
    rectangles à droite et qui prend en entrée une liste d'abscisses X et une liste d'ordonnées fX."""
    integrale = 0
    for i in range(0, len(X) - 1):
        integrale += (X[i + 1] - X[i]) * fX[i]
    return integrale


def rectg(X, fX):
    """ Q3 : De manière similaire, coder en Python une fonction rectg(X,fX) qui retourne l'intégrale numérique calculée
    avec la méthode des rectangles à gauche."""
    integrale = 0
    for i in range(0, len(X) - 1):
        integrale += (X[i + 1] - X[i]) * fX[i + 1]
    return integrale


def trapz(X, fX):
    """ Q4 : De même, coder en Python une fonction trapz(X,fX) qui retourne l'intégrale numérique calculée avec la
    méthode des trapèzes."""
    integrale = 0
    for i in range(0, len(X) - 1):
        integrale += (X[i + 1] - X[i]) * (fX[i] + fX[i + 1]) / 2
    return integrale


def compare():
    """ Q5 : Tracer en échelle logarithmique l'erreur d'intégration par rapport à I_{ref} en fonction du nombre de
    points d'intégration. Commenter."""
    err_rectd = []
    err_rectg = []
    err_trapz = []
    N = range(10, 10000, 10)  # Remarque : on peut aussi utiliser np.linspace ou np.logspace

    for n in N:
        X = []
        fX = []
        for x in range(0, n):
            X.append(x / (n - 1))
            fX.append(f(x / (n - 1)))
        err_rectd.append(abs(rectd(X, fX) - Iref))
        err_rectg.append(abs(rectg(X, fX) - Iref))
        err_trapz.append(abs(trapz(X, fX) - Iref))
    plt.figure()
    plt.loglog(N, err_rectd, 'k', N, err_rectg, ':k', N, err_trapz, '-.k')
    plt.xlabel("Nombre de points")
    plt.ylabel("Erreur absolue")
    plt.legend(["rect. à droite", "rect. à gauche", "trapèzes"])
    plt.title("Erreur globale d'intégration")
    plt.grid()
    plt.show()


if __name__ == '__main__':

    # Visualisation fonction
    Iref = 0.5 - np.sin(20) / 40
    X = []
    fX = []
    for x in range(0, 1000):
        X.append(x / 1000)
        fX.append(f(x / 1000))

    plt.figure()
    plt.plot(X, fX, 'k')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Fonction à integrer")
    plt.grid()
    plt.show()

    compare()
