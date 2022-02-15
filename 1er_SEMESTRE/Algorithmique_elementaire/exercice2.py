"""
    Cours : Algorithmique élémentaire
    Exercice : Le problème de Monty Hall
"""
from random import choice, randint


def autrePorte(i, j):
    """" Q1 : Écrire une fonction Python appelée autrePorte(i, j) qui prend deux nombres entiers distincts i et j
    compris entre 1 et 3 en entrée, et qui renvoie en sortie l'entier compris entre 1 et 3 différent de i et de j"""
    return (1 + 2 + 3) - (i + j)


def choix_presentateur(i, j):
    """ Q2 : À quoi sert l'algorithme suivant ? Implémenter en Python."""
    if i == j:
        k = choice([el for el in [1, 2, 3] if el != i])
    else:
        k = autrePorte(i, j)
    return k


def changeEtGagne():
    """ Q3 : En déduire l'algorithme principal changeEtGagne qui modélise une instance du jeu décrit. Il ne prend pas
    d'entrées et il renvoie 1 en sortie si le candidat trouve la bonne porte après avoir changé d'avis, 0 sinon"""
    bonne_porte = randint(1, 3)
    choix_c = randint(1, 3)
    choix_p = choix_presentateur(bonne_porte, choix_c)
    echange = autrePorte(choix_c, choix_p)
    if echange == bonne_porte:
        return 1
    return 0


def frequenceGainSiChange(N):
    """ Q4 : Écrire une fonction frequenceGainSiChange(N) qui simule N instances de la situation décrite et qui renvoie 
    la fréquence à laquelle le candidat gagne lorsqu'il change d'avis."""
    n = 0
    for i in range(N):
        n += changeEtGagne()
    return n / N


def frequenceGainSiChange2(N):
    n = 0
    for i in range(N):
        bonne_porte = randint(1, 3)
        choix_candidat = randint(1, 3)
        if choix_candidat != bonne_porte:
            n += 1
    return n / N


if __name__ == '__main__':
    print(frequenceGainSiChange(10000))
