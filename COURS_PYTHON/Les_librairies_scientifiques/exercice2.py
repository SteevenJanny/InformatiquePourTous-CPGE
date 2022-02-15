"""
    Cours : Les librairies scientifiques
    Exercice : Générateurs de nombres aléatoires
"""
import random
import math


def loiBernoulli(p):
    """ Q1 : Coder une fonction loiBernoulli(p) qui renvoie une variable aléatoire issue d'une loi de Bernoulli de
    paramètre p"""
    nombreAleatoire = random.random()
    if nombreAleatoire < p:
        return True
    else:
        return False


def loiBinomiale(n, p):
    """ Q2 : Coder une fonction loiBinomiale(n, p) qui renvoie une variable aléatoire issue d'une loi Binomiale de
    paramètre (n, p)"""
    longueursSegments = []
    for k in range(n):
        proba = math.comb(n, k) * p ** k * (1 - p) ** (n - k)
        longueursSegments.append(proba)

    x = random.random()
    somme = 0
    for k in range(n):
        nextSomme = somme + longueursSegments[k]
        if somme < x < nextSomme:
            return k
        somme = nextSomme


def loiPoisson(l):
    """ Q3 : Coder une fonction loiPoisson(l) qui renvoie une variable aléatoire issue d'une loi de Poisson de
    paramètre lambda = l"""
    k = 0  # On initialise la sortie à 0
    somme = 0
    x = random.random()  # Tirage d'un nombre uniformement

    factorielle = 1
    while somme < x:
        somme += l ** k / (factorielle) * math.exp(-l)
        k = k + 1  # Incrémente le compteur
        factorielle *= k  # Anticipation de la prochaine factorielle
    return k


if __name__ == '__main__':
    nombreTrue = 0
    for _ in range(100_000):
        X = loiBernoulli(0.76)
        if X == True:  # Si la variable est vraie
            nombreTrue += 1  # On ajoute 1 au compteur de True
    print("Verif Bernouilli : ", nombreTrue / 10_000)
