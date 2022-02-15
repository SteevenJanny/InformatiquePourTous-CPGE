"""
    Cours : Algorithmes récursifs
    Exercice : Triangle de Pascal
"""


def pascal(n, k):
    """ Q1 : À l'aide de la formule de récurrence ci-dessus, coder une fonction récursive calculant le coefficient
    binomial C^k_n."""
    if k > n or k < 0:
        return 0
    if n == 0:
        return 1
    return pascal(n - 1, k - 1) + pascal(n - 1, k)


def afficheTrianglePascal(N):
    """ Q2 : Coder une fonction afficheTrianglePascal(N) qui affiche les valeurs C^k_n du triangle de Pascal pour
    n dans [0, N-1] et k dans [n-N, N] en respectant  les règles suivantes ..."""
    for n in range(N):  # Première boucle sur les lignes
        s = ""
        for k in range(n - N, N + 1):  # Deuxième boucle sur les colonnes
            s += str(pascal(n, k)) + " "  # ne pas oublier l'espace !
        print(s)


def afficheSierpinsky(N):
    """ Q3 : Coder une fonction afficheSierpinski(N) qui reprend les mêmes règles que la fonction précédente 
    mais qui affiche"""
    for n in range(N):
        s = ""
        for k in range(n - N, N + 1):
            if pascal(n, k) % 2 == 1:  # Si impair
                s += "* "
            elif 0 < k < n:  # on sait déjà que c'est forcément pair donc pas besoin de vérifier
                s += "  "
            else:
                s += "-"
        print(s)


if __name__ == '__main__':
    N = 8
    afficheTrianglePascal(N)
    afficheSierpinsky(N)
