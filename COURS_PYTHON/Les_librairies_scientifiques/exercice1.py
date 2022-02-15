"""
    Cours : Les librairies scientifiques
    Exercice : La puissance de Numpy
"""
import numpy as np
import math
from time import time

LISTE = np.random.rand(10000)
VECTEURS = np.random.rand(10000, 2)
MATRICE = np.random.rand(100, 100)


# Q1 : Multiplication de chaque élément d'une liste par un scalaire en utilisant un array ou une liste.
def f_python():
    double = []
    for k in range(len(LISTE)):
        double.append(LISTE[k] * 2)


def f_numpy():
    double = LISTE * 2


t = time()
for k in range(100):
    f_python()
print("Multplication scalaire (Python): ", time() - t)
t = time()
for k in range(100):
    f_numpy()
print("Multplication scalaire (Numpy): ", time() - t)


# Q2 : Calcul de la moyenne et de la variance.
def f_python():
    moyenne = 0
    for k in LISTE:
        moyenne += k / len(LISTE)
    variance = 0
    for k in LISTE:
        variance += (k - moyenne) ** 2 / len(LISTE)


def f_numpy():
    moyenne = np.mean(LISTE)
    variance = np.var(LISTE)


t = time()
for k in range(100):
    f_python()
print("Moyenne et Variance (Python): ", time() - t)
t = time()
for k in range(100):
    f_numpy()
print("Moyenne et Variance (Numpy): ", time() - t)


# Q3 : Calcul les normes d'une liste de vecteurs 2D.
def f_python():
    normes = []
    for k in range(len(VECTEURS)):
        x, y = VECTEURS[k]
        norme = math.sqrt(x ** 2 + y ** 2)
        normes.append(norme)


def f_numpy():
    normes = np.sqrt(np.sum(VECTEURS ** 2, axis=1))


t = time()
for k in range(100):
    f_python()
print("Norme (Python): ", time() - t)
t = time()
for k in range(100):
    f_numpy()
print("Norme (Numpy): ", time() - t)


# Q4 : Transposition d'une matrice.
def f_python(MATRICE):
    transpose = []
    for i in range(MATRICE.shape[0]):
        transpose.append([])  # Ajoute une ligne
        for j in range(MATRICE.shape[1]):
            transpose[i].append(MATRICE[j, i])


def f_numpy(MATRICE):
    transpose = np.transpose(MATRICE)


import matplotlib.pyplot as plt

tps_python, tps_numpy = [], []
tailles_matrices = [10, 20, 50, 100, 200, 500, 1000]
for N in tailles_matrices:
    MATRICE = np.random.rand(N, N)
    t = time()
    f_python(MATRICE)
    tps_python.append(time() - t)

    t = time()
    f_numpy(MATRICE)
    tps_numpy.append(time() - t)

plt.grid()
plt.loglog(tailles_matrices, tps_python, c="gray", marker=".")
plt.loglog(tailles_matrices, tps_numpy, "--", c="black", marker=".")
plt.title("Evolution du temps de transposition")
plt.xlabel("Taille de la matrice")
plt.ylabel("Temps en seconde")
plt.legend(["Python pur", "Numpy"])
plt.show()
