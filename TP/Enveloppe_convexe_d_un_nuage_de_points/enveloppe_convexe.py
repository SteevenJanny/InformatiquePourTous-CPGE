"""
    TP : Enveloppe convexe d'un nuage de points
"""
import numpy as np
import matplotlib.pyplot as plt


def donneNuagePoints(N):
    """ Q1 : Coder une fonction donneNuagePoints(N) qui renvoie une liste de $N$ points 2D échantillonnés uniformément
    dans [0, 1]^2."""
    nuage = []  # Liste de points
    for _ in range(N):  # Génération de N points
        point = np.random.random(2)  # Vecteur 2D aléatoire
        nuage.append(point)
    return nuage


def afficheEnveloppeConvexe(nuage, hull, titre=""):
    """ Q2 : Coder une fonction afficheEnveloppeConvexe(nuage, hull) qui affiche grâce à Matplotlib le nuage de points,
    ainsi que l'enveloppe décrite par la liste de points hull= (p_1, p_2, ...p_n)."""
    # Affichage du nuage
    Xcoordonnees = [p[0] for p in nuage]  # Extraction des coordonnées d'abscisse
    Ycoordonnees = [p[1] for p in nuage]  # Extraction des coordonnées d'ordonnée
    plt.scatter(Xcoordonnees, Ycoordonnees)

    # Affichage de l'enveloppe
    Xcoordonnees = [p[0] for p in hull]
    Ycoordonnees = [p[1] for p in hull]

    # Fermeture de l'enveloppe (retour au premier point)
    Xcoordonnees.append(Xcoordonnees[0])
    Ycoordonnees.append(Ycoordonnees[0])

    plt.plot(Xcoordonnees, Ycoordonnees)
    plt.title(titre)
    plt.show()


def estADroite(A, B, P):
    """ Q4 : Coder une fonction estADroite(A, B, P) qui renvoie True si le point P est à gauche de (AB) et False
    sinon."""
    terme1 = (P[1] - A[1]) * (B[0] - A[0])
    terme2 = (B[1] - A[1]) * (P[0] - A[0])
    return terme1 < terme2


def pointLePlusADroite(E, p):
    """ En déduire une fonction pointLePlusADroite(E, p) qui renvoie le point q \neq p de E tel que tous les points de
    E soient à gauche de (pq)."""
    A = p
    B = E[0] if np.all(A != E[0]) else E[1]
    for P in E:
        if np.all(P != A) and estADroite(A, B, P):
            B = P
    return B


def marcheDeJarvis(S):
    """ Q6 : Implémenter en Python la fonction marcheDeJarvis(E) qui calcule l'enveloppe convexe de E grâce à
    l'algorithme du papier cadeau. Visualiser le résultat sur quelques exemples. """
    p0 = pointLePlusAGauche(S)
    hull = [p0]
    q = None
    while not np.all(q == p0):
        q = pointLePlusADroite(S, hull[-1])
        hull.append(q)
    return hull


def pointLePlusAGauche(E):
    p = E[0]
    for point in E:
        if point[0] < p[0]:
            p = point
    return p


def angle(A, B):
    """ Q8 : Coder une fonction angle(A, B) qui renvoie l'angle que forme le segment [AB] avec l'axe des abscisses."""
    dx = (B[0] - A[0])
    dy = (B[1] - A[1])
    return np.arctan2(dy, dx)


def tri_fusion(L, pivot):
    """ Q9 : Coder un algorithme de tri par fusion renvoyant la liste de points E triés par angle croissant en fonction
    d'un point pivot A constant. Vérifier votre résultat en affichant le nuage de points, ainsi que l'indice de chacun
    d'eux."""
    if len(L) <= 1:
        return L
    indice_milieu = len(L) // 2
    return fusion(tri_fusion(L[:indice_milieu], pivot), tri_fusion(L[indice_milieu:], pivot), pivot)


def fusion(L1, L2, pivot):
    if len(L1) == 0:
        return L2
    if len(L2) == 0:
        return L1

    if angle(pivot, L1[0]) < angle(pivot, L2[0]):
        return [L1[0], *fusion(L1[1:], L2, pivot)]
    return [L2[0], *fusion(L1, L2[1:], pivot)]


def testeTriFusion():
    E = donneNuagePoints(10)  # Génération d'un nuage de point
    pivot = pointLePlusBas(E)  # Sélection d'un pivot
    E = tri_fusion(E, pivot)  # tri des points

    for i, (x, y) in enumerate(E):
        plt.scatter(x, y)  # Affiche le point
        plt.text(x, y, str(i))  # Affiche l'indice du point
        plt.plot([pivot[0], x], [pivot[1], y], '--')  # Affiche le vecteur (AB) en pointillé
    plt.show()


def parcoursDeGraham(E):
    """ Q10 : Implémenter le parcours de Graham, et visualiser le résultat sur quelques exemples."""
    p0 = pointLePlusBas(E)
    E = tri_fusion(E, p0)
    hull = [E[0], E[1]]
    for i in range(2, len(E)):  # On commence au deuxième point
        while estADroite(hull[-2], hull[-1], E[i]):
            hull.pop(-1)
        hull.append(E[i])
    return hull


def pointLePlusBas(E):
    p = E[0]
    for point in E:
        if point[1] < p[1]:
            p = point
    return p


def separerPoint(E, A, B):
    """ Q11 : Coder une fonction separerPoint(E, A, B) qui renvoie les ensembles E_1 et E_2 respectivement au-dessus et
    au-dessous de la droite (AB)."""
    E1, E2 = [], []  # Initialise des liste vides
    for point in E:
        if np.all(point != A) and np.all(point != B):
            if estADroite(A, B, point):
                E1.append(point)
            else:
                E2.append(point)
    return E2, E1


def pointLePlusEloigne(E, A, B):
    """ Q12 : Coder une fonction pointLePlusEloigne(E, A, B) qui renvoie le point le plus éloigné de la droite (AB)."""
    C = E[0]
    maxDistance = distance(A, B, C)
    for point in E:
        d = distance(A, B, point)  # distance entre le point et (AB)
        if d > maxDistance:
            C = point
            maxDistance = d
    return C


def distance(A, B, C):
    a = (B[1] - A[1]) / (B[0] - A[0])  # Pente
    b = A[1] - A[0] * a  # Ordonnée à l'origine
    # d = abs(a * C[0] - C[1] + b) / np.sqrt(a ** 2 + b ** 2)
    d = abs(C[1] - a * C[0] - b) / np.sqrt(1 + a ** 2)
    return d


def pointsHorsTriangle(E, A, B, C):
    """ Coder une fonction pointsHorsTriangle(E, A, B, C) qui renvoie la liste de l'ensemble des points à l'extérieur du
    triangle ABC."""
    horsTriangle = []
    for point in E:
        if np.all(point != A) and np.all(point != B) and np.all(point != C):
            # De quel côté se situe le point
            positions = [estADroite(A, B, point), estADroite(B, C, point), estADroite(C, A, point)]
            # S'il est toujours à gauche ou toujours à droite
            if not (positions == [True] * 3 or positions == [False] * 3):
                horsTriangle.append(point)  # On l'ajoute
    return horsTriangle


def quickhull(E):
    """ Q14 : Coder la fonction quickhull(E) qui implémente l'algorithme décrit plus haut."""
    # Trouve les points les plus à gauche/droite
    A = E[np.argmin(np.array(E)[:, 0])]  # Point le plus à droite
    B = E[np.argmax(np.array(E)[:, 0])]  # Point le plus à gauche

    # Ajoute A et B à l'enveloppe, ils y sont forcement
    hull = [A, B]

    # Sépare les points
    E1, E2 = separerPoint(E, A, B)

    # Cherche les points suivants de l'enveloppe
    hull1 = trouveHull(E1, A, B, side="up")
    hull2 = trouveHull(E2, A, B, side="down")

    # Concatène les résultats
    hull = hull + hull1 + hull2
    return hull


def trouveHull(E, A, B, side):
    if len(E) == 0:
        return []  # Condition d'arrêt de l'algo récursif

    # Trouve le point le plus loin et ajoute le à l'enveloppe
    pointLoin = pointLePlusEloigne(E, A, B)
    hull = [pointLoin]

    # Trouve tous les points hors du triangle ABpointLoin
    E = pointsHorsTriangle(E, A, B, pointLoin)

    # Sépare les points, attention à l'ordre des points et des variables
    if side == "up":
        E1, _ = separerPoint(E, A, pointLoin)
        E2, _ = separerPoint(E, pointLoin, B)
    else:
        _, E1 = separerPoint(E, A, pointLoin)
        _, E2 = separerPoint(E, pointLoin, B)

    # Récursion
    hull1 = trouveHull(E1, A, pointLoin, side)
    hull2 = trouveHull(E2, pointLoin, B, side)

    # Concaténation
    hull = hull + hull1 + hull2
    return hull


if __name__ == '__main__':
    from time import time

    EE = donneNuagePoints(50)
    # Marche de Jarvis :
    hull = marcheDeJarvis(EE)
    afficheEnveloppeConvexe(EE, hull, "Marche de Jarvis")

    # Test tri fusion
    testeTriFusion()

    # Parcours de Graham
    hull = parcoursDeGraham(EE)
    afficheEnveloppeConvexe(EE, hull, "Parcours de Graham")

    # Quick Hull
    hull = quickhull(EE)
    centroid = np.mean(hull, axis=0)
    hull = tri_fusion(hull, centroid)
    afficheEnveloppeConvexe(EE, hull, "Quick Hull")
