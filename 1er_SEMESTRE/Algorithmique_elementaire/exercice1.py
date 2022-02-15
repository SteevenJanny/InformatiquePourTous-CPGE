"""
    Cours : Algorithmique élémentaire
    Exercice : Pronostics hippiques
"""

def pari_hippique(n, j):
    coeff1 = 1
    coeff2 = 1
    for i in range(1, j + 1):
        coeff1 *= n - i + 1
        coeff2 *= i
    p_ordre = 1 / coeff1
    p_desordre = p_ordre * coeff2
    return p_ordre, p_desordre


if __name__ == '__main__':
    print(pari_hippique(10, 3))