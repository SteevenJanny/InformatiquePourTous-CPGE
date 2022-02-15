"""
    Cours : Résolution d'équations différentielles
    Exercice : Modèle proies-prédateurs
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

alpha, beta, gamma, delta = 2, 0.2, 1.5, 0.1
omega = 0
H = 0.005


def F(y, t):
    """ Q1 : Montrer que l'évolution des effectifs des lapins et des furets obéit à l'EDO ci-dessous.
    Mettre l'équation sous sa forme de Cauchy."""
    return np.array([alpha * y[0] - beta * y[0] * y[1] - omega * y[0] ** 2, delta * y[0] * y[1] - gamma * y[1]])


def solve_euler(y0, time):
    """ Q2 : Utiliser la méthode d'Euler pour simuler l'évolution de la population sur 50 ans (avec un pas de 
    discrétisation constant de 0.005 an). On prendra alpha = 2, beta=0.2, gamma=1.5 et delta=0.1. Démarrer la 
    simulation avec 10 lapins et 4 furets. Afficher l'évolution des populations sur un graphe."""
    solution = [y0]
    for i in range(len(time) - 1):
        y = solution[-1] + H * F(solution[-1], t)
        solution.append(y)
    return np.array(solution)


if __name__ == '__main__':
    y0 = np.array([10, 4])
    t = np.arange(0, 20, H)
    sol_euler = solve_euler(y0, t)
    sol_odeint = odeint(F, y0, t)

    plt.figure(figsize=(8, 4))
    plt.title("Evolution des effectifs des deux espèces")
    plt.xlabel("Temps (années)")
    plt.ylabel("Effectifs")
    plt.grid(c="gray")
    plt.plot(t, sol_euler[:, 0], c="black", label="Lapins (Euler)")
    plt.plot(t, sol_euler[:, 1], c="black", label="Furets (Euler)")
    plt.plot(t, sol_odeint[:, 0], '--', label="Lapins (Odeint)")
    plt.plot(t, sol_odeint[:, 1], '--', label="Furets (Odeint)")
    plt.legend()
    plt.savefig("graphe_lotka_odeint.pdf")
    plt.show()
