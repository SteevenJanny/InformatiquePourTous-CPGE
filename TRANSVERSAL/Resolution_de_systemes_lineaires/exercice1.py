"""
    Cours : Résolution de systèmes linéaires
    Exercice : Résolution d'une équation de Poisson
"""
import numpy as np
import scipy.linalg as spl
from time import time
import matplotlib.pyplot as plt


def Lapl1D(N, dx):
    """ Q2 : Ecrire une fonction lapl1D(N,dx) qui renvoie Delta_d sous la forme d'un tableau numpy en fonction du
    nombres d'inconnues N et du pas de discrétisation delta x"""
    N = int(N)
    Delta_d = np.zeros((N, N))
    Delta_d[0, 0:2] = np.array([-2, 1])
    Delta_d[-1, -2:] = np.array([1, -2])
    for i in range(1, N - 1):
        Delta_d[i, i - 1:i + 2] = np.array([1, -2, 1])
    return Delta_d / dx ** 2


def Lapl1D_opti(N, dx):
    N = int(N)
    Delta_d = -2 * np.diag(np.ones(N), 0) + np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1)
    return Delta_d / dx ** 2


def dirichlet(Delta_d, F):
    """ Q3 : Etant donné Delta_d et F_d, procéder aux modifications nécessaires pour imposer u_0=0 et u_{N-1} = 0. On
    écrira une fonction dirichlet(Delta, F) qui renvoie la matrice A et le second membre b du système à résoudre, après
    application des conditions limites."""
    A = - Delta_d[1:-1, 1:-1]
    b = F[1:-1]
    return A, b


# Q4 : Résoudre ce système à l'aide de scipy.linalg.solve pour le second membre F_d de votre choix (non-nul).
# Tracer le résultat.

N = 1000
dx = 1 / N

Delta_d = Lapl1D(N, dx)
F = np.ones(N)
A, b = dirichlet(Delta_d, F)

u = np.zeros(N)
t1 = time()
u[1:-1] = spl.solve(A, b)
t_lu = time() - t1

print("t_lu = {:.2e}".format(t_lu))

plt.plot(np.linspace(0, 1, N), u)
plt.xlabel('x (m)')
plt.ylabel('u')
plt.title("Solution de l'équation de Poisson (F constant)")
plt.style.use("grayscale")
plt.show()

# Q5 : Utiliser cette propriété pour résoudre le système linéaire plus efficacement avec  scipy.linalg.solve.
t1 = time()
u[1:-1] = spl.solve(A, b, assume_a='pos')
t_chol = time() - t1
print("t_chol = {:.2e}".format(t_chol))


# Q6 : Calculer l'évolution de la solution sur une période temporelle (on prendra au moins 100 pas de temps)
def secondMembre(N, t):
    x = np.linspace(0, 1, N)
    F = np.sin(2 * np.pi * x) * np.sin(2 * np.pi * t)
    return F


T = np.linspace(0, 1, 100)
U1 = []
t1 = time()
for t in T:
    A, b = dirichlet(Delta_d, secondMembre(N, t))
    u[1:-1] = spl.solve(A, b, assume_a='pos')
    U1.append(u.copy())

t_naif = time() - t1

print("t_naif = {:.2e}".format(t_naif))

# Code optimisé

U2 = []
t1 = time()
L = spl.cholesky(A, lower=True)
for t in T:
    A, b = dirichlet(Delta_d, secondMembre(N, t))
    u[1:-1] = spl.solve_triangular(L.T, spl.solve_triangular(L, b, lower=True))
    U2.append(u.copy())

t_dec = time() - t1

print("t_dec = {:.2e}".format(t_dec))

# Q7 : On veut maintenant une discrétisation bien plus fine : N = 10^5. Que se passe-t-il ?
N = 100000
dx = 1 / N

# Delta_d = Lapl1D(N,dx) #si on décommente ce terme on obtient une MemoryError

# Q8 : Réécrire la matrice Delta_d sous la forme d'une matrice creuse avec scipy.sparse.spdiags, et relancez les 
# calculs de la question 6

from scipy.sparse.linalg import spsolve
from scipy.sparse import diags


def Lapl1D_sparse(N, dx):
    N = int(N)
    Delta_d = -2 * diags(np.ones(N), 0, format='csr')
    Delta_d += diags(np.ones(N - 1), 1, format='csr')
    Delta_d += diags(np.ones(N - 1), -1, format='csr')
    return Delta_d / dx ** 2


Delta_d = Lapl1D_sparse(N, dx)
F = np.ones(N)
A, b = dirichlet(Delta_d, F)

plt.spy(A, markersize=1)
plt.title('Termes non nuls de A')

u = np.zeros(N)
t1 = time()
u[1:-1] = spsolve(A, b)
t_sparse = time() - t1

print("t_sparse = {:.2e}".format(t_sparse))
