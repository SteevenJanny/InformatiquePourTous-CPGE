"""
    Cours : Algorithmes gloutons
    Exercice : Planification d'un ordre de passage
"""
import time
import random
import matplotlib.pyplot as plt


def genereCreneaux(N):
    """ Q1 : coder une fonction qui génère aléatoirement une liste de N = 100 créneaux échantillonnés entre aujourd'hui
    et aujourd'hui + 23 heures."""
    now = time.time()  # Nombre de secondes jusqu'à maintenant
    creneaux = []
    for _ in range(N):
        depart = random.randint(0, 23 * 3600)  # Décalage temporel aléatoire
        creneaux.append(now + depart)
    return creneaux


def afficheCreneaux(creneaux):
    """ Q2 : Coder une fonction afficheCreneau(creneaux) qui prend en paramètre une liste de N créneaux et qui trace
    pour le i^e créneau une droite entre (creneaux[i], i) et (creneaux[i]+3600, i)"""
    plt.figure()
    for i, c in enumerate(creneaux):
        debut, fin = c, c + 3600
        plt.plot([debut, fin], [i, i], marker="o")
    plt.xticks(rotation=45)  # Rotation des labels sur l'axe X
    # Titre des axes
    plt.ylabel("# Créneau")
    plt.xlabel("Temps (epoch)")
    plt.show()


def dernierCreneauAvant(T, creneaux):
    """ Q3 : Coder une fonction dernierCreneauAvant(T, creneaux) qui renvoie l'indice du créneau de la liste creneaux
    qui finit le plus tard sans dépasser T. Elle renverra None si aucun créneau ne convient."""
    indice_max = None  # Initialisation des variables
    maximum = 0
    for indice, c in enumerate(creneaux):  # Début de la recherche séquentielle
        if maximum < c and c + 3600 <= T:  # Cherche max qui ne dépasse pas T
            maximum = c
            indice_max = indice
    return indice_max


def organisePassage(creneaux):
    """ Q4 : Coder une fonction organisePassage(creneaux) qui renvoie le planning des passages maximisant le nombre de
    candidats auditionnés par le jury à l'aide de l'approche gloutonne."""
    solution = []
    # Calcul du premier créneau (en partant de la fin)
    prochain = dernierCreneauAvant(max(creneaux) + 3600, creneaux)
    while prochain is not None:
        solution.append(creneaux[prochain])
        T = creneaux[prochain]  # Début du dernier créneau ajouté à la solution
        prochain = dernierCreneauAvant(T, creneaux)  # Recherche créneau le plus proche sans superposition
    return solution


def organisePassageRecursif(creneaux, T=0):
    """ Q5 : Coder la même fonction en récursif."""
    if T == 0:  # paramètre par défaut = on lance la fonction pour la première fois
        T = max(creneaux) + 3600
    prochain = dernierCreneauAvant(T, creneaux)
    if prochain is None:  # Condition d'arrêt : on ne trouve plus de créneau
        return []
    T = creneaux[prochain]
    return [creneaux[prochain]] + organisePassageRecursif(creneaux, T)


if __name__ == '__main__':
    creneaux = genereCreneaux(100)
    solution = organisePassage(creneaux)  # itératif
    afficheCreneaux(solution)

    solutionRecursive = organisePassageRecursif(creneaux)
    print(solutionRecursive == solution)
