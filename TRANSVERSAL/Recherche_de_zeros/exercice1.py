"""
    Cours : Recherche de zéros
    Exercice : Recherche de zéros
"""
import numpy as np
from time import time
from scipy.optimize import newton, bisect
import matplotlib.pyplot as plt


def f(x):
    """ Q1 : Coder la fonction f(x) qui renvoie la valeur de x^3-2x+2 évaluée en x, puis tracer sa courbe rapidement sur
     I. En déduire un encadrement grossier de x_*."""
    return x ** 3 - 2 * x + 2


def draw_function():
    x = np.linspace(-3, 3, 1000)
    y = []
    for k in range(1000):
        y.append(f(x[k]))

    plt.plot(x, y, c="black")
    plt.grid()
    plt.title("Fonction à résoudre sur l'intervalle [-3, 3]")
    plt.xlabel("x")
    plt.ylabel("y = f(x)")
    plt.show()


def rechercheSequentielle(start, epsilon):
    """ Q2 : Coder et tester la méthode de recherche séquentielle."""
    while f(start) * f(start + epsilon) > 0:
        start += epsilon
    return start


def rechercheDichotomie(start, end, epsilon):
    """ Q3 : Coder et tester la méthode de dichotomie."""
    while end - start > epsilon:
        middle = (start + end) / 2
        if f(start) * f(middle) <= 0:
            end = middle
        else:
            start = middle
    return start


def fprime(x):
    """ Q4 : Calculer la dérivée de f, puis coder la méthode de Newton. Comparer le temps d'exécution avec les autres
    méthodes."""
    return 3 * x ** 2 - 2


def rechercheNewton(start, epsilon):
    N = 0  # Un compteur de nombre d'itérations
    xk = start
    xkk = xk - f(xk) / fprime(xk)

    while abs(xk - xkk) > epsilon and N < 1000:
        next_x = xkk - f(xkk) / fprime(xkk)
        xk, xkk = xkk, next_x
        N += 1

    if N == 1000:
        print("Warning : Exceed number of iteration")
    return xkk


def compare_temps_epsilon():
    temps_sequentiel = []
    temps_dichotomie = []
    temps_newton = []
    epsilon = np.logspace(-2, -15, 25)  # 25 valeurs entre 0.1 et 10^-12

    for e in epsilon:
        if e > 1e-7:
            t = time()
            s = rechercheSequentielle(-2, e)
            temps_sequentiel.append(time() - t)

        t = time()
        s = rechercheDichotomie(-2, -1, e)
        temps_dichotomie.append(time() - t)

        t = time()
        s = rechercheNewton(-1.5, e)
        temps_newton.append(time() - t)
    plt.loglog(epsilon[:len(temps_sequentiel)], temps_sequentiel, linestyle='solid', c="black", label="Sequentiel")
    plt.loglog(epsilon[:len(temps_dichotomie)], temps_dichotomie, linestyle='dashed', c="black", label="Dichotomie")
    plt.loglog(epsilon[:len(temps_newton)], temps_newton, linestyle='dashdot', c="black", label="Newton")
    plt.grid()
    plt.legend()
    plt.xlabel("Epsilon")
    plt.ylabel("Temps d'exécution (s)")
    plt.title("Temps d'exécution en fonction de la précision")
    plt.show()


def demonstration_methodes():
    print("RECHERCHE SEQUENTIELLE")
    t = time()
    solution, _ = rechercheSequentielle(-2, epsilon=1e-8)
    print(f"\tSolution : {solution} trouvée en {time() - t} secondes")

    print("METHODE DE LA DICHOTOMIE")
    t = time()
    solution, _ = rechercheDichotomie(-2, -1, epsilon=1e-8)
    print(f"\tSolution : {solution} trouvée en {time() - t} secondes")

    print("METHODE DE NEWTON")
    t = time()
    solution, _ = rechercheNewton(-1.5, epsilon=1e-8)
    print(f"\t Solution : {solution} trouvée en {time() - t} secondes")

    print("METHODE DE LA DICHOTOMIE (Scipy)")
    t = time()
    solution = bisect(f, -2, -1)
    print(f"\t Solution : {solution} trouvée en {time() - t} secondes")

    print("METHODE DE NEWTON (Scipy)")
    t = time()
    solution = newton(f, -1.5, fprime)
    print(f"\t Solution : {solution} trouvée en {time() - t} secondes")


if __name__ == '__main__':
    # # demonstration_methodes()
    compare_temps_epsilon()
