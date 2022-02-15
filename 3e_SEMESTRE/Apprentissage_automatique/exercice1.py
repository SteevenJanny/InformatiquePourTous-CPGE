"""
    Cours : Apprentissage automatique
    Exercice : Big brother is watching you
"""
from math import sqrt
import numpy as np
from random import uniform


def dist(x1, x2):
    """ Q1 : Écrire une fonction dist(x1, x2) qui prend en arguments deux listes de même taille, et calcule la distance
    euclidienne entre les deux."""
    S = 0
    for i in range(len(x1)):
        S += (x1[i] - x2[i]) ** 2
    return sqrt(S)


def distances_au_point(delits, x):
    """ Q2.1 : Écrire une fonction distances_au_point(delits, x) qui prend en arguments la matrice contenant les données
    criminelles des N individus et une liste de longueur p contenant les données criminelles d'un nouvel individu, et
    qui renvoie une liste distances de longueur N où la i-ème case contient la distance de x à l'observation i de delits"""
    distances = []
    N = delits.shape[0]
    for i in range(N):
        x_i = delits[i]  # observation i
        distances.append(dist(x, list(x_i)))  # dist n'accepte que des listes en entrée
    return distances


def trier_individus(distances):
    """ Q2.2 : Écrire une fonction trier_individus(distances) qui prend en argument une liste contenant les distances de
    x à chaque observation et qui renvoie une liste indices_tries contenant les indices de la liste rangés par distance
    croissante."""
    N = len(distances)

    def f(i):
        return distances[i]

    return sorted(range(N), key=f)


def moyenne_des_k_voisins(indices_tries, notes, k):
    """ Q2.3 : Écrire une fonction moyenne_des_k_voisins(indices_tries, notes, k) qui prend en arguments la liste
    contenant les indices des observations triées par distance croissante à x, la liste contenant les notes
    d'insoumission des individus et le nombre de voisins à considérer, et qui renvoie la moyenne des notes
    d'insoumission des k plus proches voisins de x."""
    indices_voisins = indices_tries[:k]
    note = 0
    for i in indices_voisins:
        note += notes[i]
    note /= k  # il y a k voisins au total, donc il faut diviser par k pour avoir la moyenne
    return note


def k_plus_proches_voisins(delits, notes, x, k):
    """ Q2.4 : En déduire une fonction k_plus_proches_voisins(delits, notes, x, k) qui renvoie la note d'insoumission
    estimée pour le citoyen ayant x comme données criminelles."""
    distances = distances_au_point(delits, x)
    indices_tries = trier_individus(distances)
    note = moyenne_des_k_voisins(indices_tries, notes, k)
    return note


def initialisation_poles(infos, k):
    """ Q3.1 : Écrire une fonction initialisation_poles(infos, k) qui génère la matrice poles initiale."""
    M, q = infos.shape
    poles = np.zeros((k, q))
    for qq in range(q):
        mini, maxi = min(infos[:, qq]), max(infos[:, qq])
        for kk in range(k):
            poles[kk, qq] = uniform(mini, maxi)
    return poles


def pole_le_plus_proche(poles, x):
    """ Q3.2 :  Écrire une fonction pole_le_plus_proche(poles, x) qui prend en arguments la matrice contenant les
    caractéristiques des pôles et une liste contenant les caractéristiques d'un individu, et qui renvoie l'indice du
    pôle le plus proche de x."""
    k = poles.shape[0]
    distance_min = np.inf
    pole_x = 0
    for j in range(k):
        distance = dist(x, list(poles[j]))
        if distance < distance_min:
            distance_min = distance
            pole_x = j
    return pole_x


def poles_les_plus_proches(poles, infos):
    """ Q3.3 : Écrire une fonction poles_les_plus_proches(poles, infos) qui renvoie une liste qu'on appellera
    repartition, dont la i-ième case contient l'indice du pôle le plus proche de l'observation i."""
    M = infos.shape[0]
    repartition = []
    for i in range(M):
        repartition.append(pole_le_plus_proche(poles, list(infos[i])))
    return repartition


def nouveaux_poles(infos, repartition, k):
    """ Q3.4 : Écrire une fonction nouveaux_poles(infos, repartition, k) qui renvoie une matrice poles contenant les
    caractéristiques des barycentres de chaque catégorie"""
    M, q = infos.shape
    nb_observations = [0 for _ in range(k)]
    poles = np.zeros((k, q))
    for i in range(M):
        l = repartition[i]  # catégorie à laquelle appartient l'observation i
        poles[l] += infos[i]  # on l'ajoute aux autres observations de même classe qu'elle
        nb_observations[l] += 1  #
    # Il ne nous reste plus qu'à diviser chaque pôle l par le nombre d'observations classées l
    for l in range(k):
        if nb_observations[l] != 0:
            poles[l] /= nb_observations[l]
    return poles


def k_moyennes(infos, k):
    """ Q3.5 : En déduire une fonction k_moyennes(infos, k) qui renvoie la matrice poles des pôles, correspondant aux k
    classes trouvées par l'algorithme des k-moyennes."""
    poles = initialisation_poles(infos, k)
    a_bouge = True
    while a_bouge:
        repartition = poles_les_plus_proches(poles, infos)
        poles0 = nouveaux_poles(infos, repartition, k)
        a_bouge = (poles != poles0).any()  # teste si les pôles ont bougé
        poles = poles0
    return poles


if __name__ == '__main__':
    delits = np.random.randn(100, 2)
    notes = np.random.rand(100)
    x = np.random.randn(2)

    infos = np.random.randn(100, 2)

    note = k_plus_proches_voisins(delits, notes, x, 4)
    print(k_moyennes(infos, 10))
