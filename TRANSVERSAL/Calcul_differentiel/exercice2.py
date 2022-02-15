"""
    Cours : Calcul différentiel
    Exercice : Calcul de l'emprise au sol d'un bâtiment
"""
import numpy as np


def f1(x):
    return 20 * np.sqrt(np.sin(x / 20) ** 2) / ((x / 20) ** 2 + 1)


def f2(x):
    return 20 * np.log10(np.sin(x / 10) ** 2 + 0.1) / ((x / 20) ** 2 + 1)


def rectd(X, fX):
    integrale = 0
    for i in range(0, len(X) - 1):
        integrale += (X[i + 1] - X[i]) * fX[i]
    return integrale


N = 1000  # on prend N grand pour avoir une erreur d'intégration faible
X = np.linspace(0, 50, N)  # renvoie une liste de N points régulièrement espacés de 0 à 50
F1 = []
F2 = []
for i in range(0, len(X)):
    F1.append(f1(X[i]))
    F2.append(f2(X[i]))

A = rectd(X, F1) - rectd(X, F2)
print("L'aire du batiment vaut {:.2f} m^2".format(A))
