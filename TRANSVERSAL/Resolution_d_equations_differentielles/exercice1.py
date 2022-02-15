"""
    Cours : Résolution d'équations différentielles
    Exercice : Comparaison de plusieurs schémas numériques
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

g = 9.81  # accélération de pesanteur (m/s^2)
k = 0.3  # coefficient de frottement (kg/m)
m = 100  # masse du parachutiste (kg)


def F(v, t):
    """ Q1 : Après avoir écrit l'EDO sous sa forme de Cauchy, implémenter une fonction F(y) appropriée à la résolution
    de cette ODE."""
    return g - k / m * v ** 2


def solve_odeint(v0, time):
    """ Q2 : Déterminer la valeur de v sur son intervalle de définition en utilisant la méthode odeint de scipy."""
    sol_odeint = odeint(F, v0, time)
    return sol_odeint


def solve_euler(v0, time):
    """ Q3 : Implémenter la méthode d’Euler explicite présentée dans ce chapitre pour simuler la vitesse de chute du
    parachutiste sur les 30 premières secondes (on prendra un pas de temps de 3 secondes)."""
    solution = [v0]
    for i in range(len(time) - 1):
        y = solution[-1] + (time[i + 1] - time[i]) * F(solution[-1], time[i])  # Calcule le prochain y
        solution.append(y)
    return np.array(solution)


def solve_rk4(v0, time):
    """ Q4 : Implémenter la méthode de Runge Kutta d’ordre 4 pour résoudre cette équation."""
    solution = [v0]
    for i in range(len(time) - 1):
        dt = time[i + 1] - time[i]
        y, t = solution[-1], time[i]  # Récupération des valeurs à l'instant t

        # Calcul des coefficients de la méthode
        a1 = F(y, t)
        a2 = F(y + dt / 2 * a1, t + dt / 2)
        a3 = F(y + dt / 2 * a2, t + dt / 2)
        a4 = F(y + dt * a3, t + dt)

        # Calcul du prochain y
        solution.append(y + (dt / 6) * (a1 + 2 * a2 + 2 * a3 + a4))
    return np.array(solution)


def compare_solutions():
    """ Q5 : Sur un même graphique, représenter les solutions approximées. Comparer à la solution exacte. """
    dt = 3
    time = np.arange(0, 30, dt)
    v0 = 0
    sol_odeint = solve_odeint(v0, time)
    sol_euler = solve_euler(v0, time)
    sol_rk4 = solve_rk4(v0, time)
    sol_analytique = np.sqrt(g * m / k) * np.tanh(np.sqrt(k * g / m) * time)
    sol_odeint2 = odeint(F, v0, time, atol=1e-10, rtol=1e-10)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(time, sol_analytique, "-")
    plt.plot(time, sol_euler, "--")
    plt.plot(time, sol_rk4, "-.")
    plt.plot(time, sol_odeint, ":")
    plt.style.use("grayscale")
    plt.grid()
    plt.xlabel("Temps (s)")
    plt.ylabel("Vitesse (m/s)")
    plt.title("Vitesse de chute du parachutiste")
    plt.legend(["analytique", "Euler", "RK4", "odeint"])

    plt.subplot(1, 2, 2)
    plt.semilogy(time, np.abs(sol_euler - sol_analytique), "--")
    plt.semilogy(time, np.abs(sol_rk4 - sol_analytique), "-.")
    plt.semilogy(time, np.abs(sol_odeint[:, 0] - sol_analytique), ":")
    plt.semilogy(time, np.abs(sol_odeint2[:, 0] - sol_analytique), "-")
    plt.style.use("grayscale")
    plt.grid()
    plt.xlabel("Temps (s)")
    plt.ylabel("Erreur (m/s)")
    plt.title("Ecart à l'expression analytique en fonction du temps")
    plt.legend(["Euler", "RK4", "odeint", "odeint 1e-10"])
    plt.show()


def compare_dt():
    """ Q6 : Représenter en échelle logarithmique l'intégrale de la norme de l'erreur sur l'ensemble de l'intervalle
    temporel pour les trois méthodes."""
    DT = np.logspace(-3, 1, 20)
    v0 = 0

    def trapz(X, fX):  # Intégration (méthode des trapèzes) ; X et fX sont des listes
        integrale = 0
        for i in range(len(X) - 1):
            integrale += (X[i + 1] - X[i]) * (fX[i] + fX[i + 1]) / 2
        return integrale

    erreur_euler = []
    erreur_rk4 = []
    erreur_odeint = []

    for dt in DT:
        time = np.arange(0, 30, dt)
        sol_euler = solve_euler(v0, time)
        sol_rk4 = solve_rk4(v0, time)
        sol_odeint = odeint(F, v0, time)
        sol_analytique = np.sqrt(g * m / k) * np.tanh(np.sqrt(k * g / m) * time)

        erreur_euler.append(trapz(time, abs(sol_euler - sol_analytique)))
        erreur_rk4.append(trapz(time, abs(sol_rk4 - sol_analytique)))
        erreur_odeint.append(trapz(time, abs(sol_odeint[:, 0] - sol_analytique)))

    plt.figure()
    plt.loglog(DT, erreur_euler, "--")
    plt.loglog(DT, erreur_rk4, "-.")
    plt.loglog(DT, erreur_odeint, ":")
    plt.style.use("grayscale")
    plt.grid()
    plt.xlabel("pas temporel (s)")
    plt.ylabel("Erreur globale (m/s)")
    plt.title("Erreur globale en fonction du pas de temps")
    plt.legend(["Euler", "RK4", "odeint"])
    plt.show()


if __name__ == '__main__':
    compare_solutions()
    compare_dt()
