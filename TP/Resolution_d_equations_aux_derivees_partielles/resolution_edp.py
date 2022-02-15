"""
    TP : Résolution d'équations aux dérivées partielles
"""

import numpy as np
import matplotlib.pyplot as plt

L = 0.64  # longueur de la corde  (m)
c = 100  # célérité de l'onde (m/s)
x0 = L / 2
h0 = 0.005


def y_0(x):
    """ Q1 : Représenter graphiquement y_0 entre x=0 et x=L, et implémenter la fonction y0(x) correspondante. """
    assert (0 <= x <= L), "x n'est pas un point de la corde"

    if np.abs(x - x0) <= L:
        return h0 / 2 * (1 + np.cos((x - x0) * np.pi / x0))
    else:
        return 0


def coeff_An(n, y0, Nx=100):  # y0 est une fonction, pas une liste
    """ Q2 : Ecrire une fonction coeff_An(n, y0, Nx) qui, à partir d'un entier n et d'une fonction y0 décrivant le
    déplacement initial, renvoie une approximation du coefficient A_n, évaluée entre x=0 et x=L à l'aide d'une
    intégration numérique sur Nx points."""
    assert (type(n) == int)
    X = np.linspace(0, L, int(Nx))
    fX = [np.sin(n * np.pi * x / L) * y0(x) for x in X]  # définition de l'intégrande
    return 2 / L * trapz(X, fX)


def trapz(X, fX):  # Intégration (méthode des trapèzes) ; X et fX sont des listes
    integrale = 0
    for i in range(len(X) - 1):
        integrale += (X[i + 1] - X[i]) * (fX[i] + fX[i + 1]) / 2
    return integrale


def An(n):  # expression analytique
    """ Q3 : Représenter graphiquement l'évolution de l'amplitude |A_n| des modes de vibration calculée numériquement
    en fonction de n. Comparer avec l'expression analytique."""
    if n in [0, 2]:
        return 0
    return ((-1) ** n - 1) * h0 * 4 / (np.pi * n * (n - 2) * (n + 2))


def anim_serie(liste_An, tmax=1.28e-2, Nx=1e4, Nt=100):
    """ Coder une fonction anim_serie(An,L,tmax) qui, à partir d'une liste des coefficients A_n affiche une animation
     de l'ondulation de la corde en fonction du temps, de t=0 à t=T_f qui est choisi pour n'observer qu'une période
     d'oscillation. """
    T = np.linspace(0, tmax, int(Nt))
    X = np.linspace(0, L, int(Nx))
    Y = []
    # calcul de la position de la corde pour différents t (somme des modes)
    for t in T:
        Y.append(0)
        for n, An in enumerate(liste_An):
            Y[-1] += An * np.sin(n * np.pi * X / L) * np.cos(n * np.pi * c * t / L)

    # affichage :
    plt.figure()
    for i, t in enumerate(T):
        plt.clf()  # nécessaire pour éviter un ralentissement de la fréquence d'images
        plt.plot(X, Y[i])
        plt.title(f"Position de la corde à t={t:.2e} s ({len(liste_An)} premiers modes)")
        plt.axis([0, L, -1.2 * h0, 1.2 * h0])
        plt.pause(0.01)  # nécessaire pour avoir l'affichage de toutes les images


def lax_wendroff(xmesh, tmesh, y0):
    """ Q9 : En utilisant vos réponses aux questions précédentes, écrire la fonction lax_wendroff(xmesh, tmesh, y0)
     qui renvoie les matrices W et Z du schéma de Lax-Wendroff."""
    Nt, Nx = len(tmesh), len(xmesh)
    dt = tmesh[1] - tmesh[0]
    dx = xmesh[1] - xmesh[0]
    W, Z = np.zeros((Nx, Nt)), np.zeros((Nx, Nt))
    cfl = c * dt / dx

    # CI initialisation t = 0
    W[0, 0] = (y0(dx) - y0(0)) / dx
    for j in range(1, Nx - 1):
        W[j, 0] = (y0(xmesh[j + 1]) - y0(xmesh[j - 1])) / (2 * dx)
    W[-1, 0] = (y0(L) - y0(L - dx)) / dx

    for n in range(1, Nt):
        W[0, 1:] = W[0, :-1] + cfl * (Z[1, :-1] - Z[0, :-1])
        W[-1, 1:] = W[-1, :-1] + cfl * (Z[-1, :-1] - Z[-2, :-1])

        W[1:-1, n] = W[1:-1, n - 1] + cfl * (Z[2:, n - 1] - Z[:-2, n - 1] + cfl * (
                W[2:, n - 1] - 2 * W[1:-1, n - 1] + W[:-2, n - 1])) / 2
        Z[1:-1, n] = Z[1:-1, n - 1] + cfl * (W[2:, n - 1] - W[:-2, n - 1] + cfl * (
                Z[2:, n - 1] - 2 * Z[1:-1, n - 1] + Z[:-2, n - 1])) / 2
        # for j in range(1, Nx - 1):
        #     W[j, n] = W[j, n - 1] + cfl * (Z[j + 1, n - 1] - Z[j - 1, n - 1] + cfl * (
        #             W[j + 1, n - 1] - 2 * W[j, n - 1] + W[j - 1, n - 1])) / 2
        #     Z[j, n] = Z[j, n - 1] + cfl * (W[j + 1, n - 1] - W[j - 1, n - 1] + cfl * (
        #             Z[j + 1, n - 1] - 2 * Z[j, n - 1] + Z[j - 1, n - 1])) / 2
    return W, Z


def resol_onde_LW(xmesh, tmesh, y0):
    """ Q10 : En déduire une fonction resol_onde_LW(xmesh, tmesh, y0) qui prend en entrée les paramètres définis
    précédemment et qui renvoie la matrice Y de dimension N_x \times N_t contenant les positions de la corde, telle
    que Y[j,n] = y(x_j,t_n)."""
    W, Z = lax_wendroff(xmesh, tmesh, y0)  # calcul compliqué du schéma de Lax Wendroff
    dx = xmesh[1] - xmesh[0]
    Y = []
    for j in range(len(tmesh)):  # intégration de W de x=0 à x=L, pour tous les pas de temps
        Y.append([0])
        for i in range(1, len(xmesh)):
            Y[-1] += [Y[-1][-1] + dx * W[i, j]]  # méthode des rectangles
    return Y


def anim_LW(xmesh, tmesh, Y):
    """ Q11 : Coder une fonction anim_LW(xmesh, tmesh, Y) qui à partir des discrétisations spatiale xmesh, temporelle
     tmesh et de la matrice solution Y obtenue à la question précédente, renvoie une animation de l'oscillation de la
     corde. Que se passe-t-il ?"""
    dt = tmesh[1] - tmesh[0]
    dx = xmesh[1] - xmesh[0]
    cfl = c * dt / dx
    for i in range(0, len(tmesh), 5):  # le 5 est là pour gagner en fréquence d'image
        plt.clf()
        plt.plot(xmesh, Y[i])
        plt.title("Position de la corde à t={:.2e} s (CFL = {:.2f})".format(tmesh[i], cfl))
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.axis([0, L, -1.2 * h0, 1.2 * h0])
        plt.pause(0.005)


def anim_compare(Aref, AN, YLW, tmesh, xmesh):
    """ Q13 : Comparer les deux méthodes numériques, conclure."""
    Y_ref, Y_AN = np.zeros((len(tmesh), len(xmesh))), np.zeros((len(tmesh), len(xmesh)))
    # calcul de la position de la corde pour différents t (somme des modes)
    for i, t in enumerate(tmesh):
        for n, An in enumerate(Aref):
            Y_ref[i] += An * np.sin(n * np.pi * xmesh / L) * np.cos(n * np.pi * c * t / L)
        for n, An in enumerate(AN):
            Y_AN[i] += An * np.sin(n * np.pi * xmesh / L) * np.cos(n * np.pi * c * t / L)
            # affichage :
    # affichage :
    plt.figure()
    for i, t in enumerate(tmesh):
        plt.clf()
        plt.plot(xmesh, Y_ref[i], '-', xmesh, Y_AN[i], '--', xmesh, YLW[i], ':')
        plt.title("Position de la corde à t={:.2e} s )".format(t))
        plt.axis([0, L, -1.2 * h0, 1.2 * h0])
        plt.legend(["référence", "série", "Lax-Wendroff"])
        plt.pause(0.01)  # nécessaire pour avoir l'affichage de toutes les images


if __name__ == '__main__':

    Aref = [An(n) for n in range(100)]
    A_N = [coeff_An(n, y_0) for n in range(4)]
    Nt, Nx = 50, 20
    xmesh = np.linspace(0, L, Nx)
    tmesh = np.linspace(0, 1.28e-2, Nt)

    YLW = resol_onde_LW(xmesh, tmesh, y_0)
    anim_compare(Aref, A_N, YLW, tmesh, xmesh)
