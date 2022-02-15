"""
    Cours : Algorithmes récursifs
    Exercice : Problème des 8 reines
"""
import numpy as np
import matplotlib.pyplot as plt


def estSolution(S):
    """ Q1 : Coder une fonction estSolution(S) qui renvoie True si la liste S est solution du problème, c'est-à-dire si
    aucune reine n'en menace une autre."""
    for reine1 in range(7):
        for reine2 in range(reine1 + 1, 8):  # On teste pour chaque paire de reines
            distanceVerticale = abs(reine1 - reine2)
            distanceHorizontale = abs(S[reine1] - S[reine2])
            if distanceHorizontale == distanceVerticale:
                return False  # Si deux reines se menacent, S n'est pas solution
    return True


def permutation(A, p=[]):
    """ Q2 : Coder une fonction récursive qui énumère toutes les permutations possibles d'une liste passée en argument"""
    P = []
    if len(A) > 0:
        for i in range(len(A)):
            concat = p + [A[i]]  # Concaténation
            r = A[:i] + A[i + 1:]  # Retire A[i]
            P = P + permutation(r, concat)  # Concaténation
        return P
    else:
        return [p]


def afficheSolution(S):
    """ Q4 : Coder une fonction afficheSolution(S) qui transforme une solution S en une matrice M telle que M_{ij}=0 
    si une reine se trouve en position (i,j), et 1 sinon."""
    M = np.ones((8, 8))  # Matrice de 8x8 cases remplies de 1
    for i, j in enumerate(S):
        M[i, j] = 0  # Place des 0 aux bons endroits
    plt.imshow(M, cmap="gray")

    plt.xticks(np.arange(8) + 0.5, [])  # Astuce pour dessiner un échiquier
    plt.yticks(np.arange(8) + 0.5, [])
    plt.grid()
    plt.show()


if __name__ == '__main__':
    A = list(range(8))
    solutions_candidates = permutation(A)
    solutions = [s for s in solutions_candidates if estSolution(s)]
    print(len(solutions))
    afficheSolution(solutions[0])
