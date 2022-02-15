"""
    Cours : Programmation Dynamique
    Exercice : Plus longue sequence de cartes
"""


def glouton(T, s):
    """ Q3 : Coder un algorithme glouton récursif qui donne la valeur de L(T, s)"""
    if len(T) == 1:  # Condition d'arrêt (car récursif)
        return sontCompatibles(T[0], s)  # Renvoie 1 si la seule carte en main peut être posée, 0 sinon.
    else:
        scores = []
        for c in T:
            if sontCompatibles(c, s):
                # Pour chaque carte compatible, on regarde la longueur de la séquence qu'on obtiendrait si on la posait.
                Tbis = T.copy()
                Tbis.remove(c)
                scores.append(1 + glouton(Tbis, c))

        if len(scores) == 0:  # Si aucune carte n'est compatible
            return 0
        else:  # Sinon, on renvoie le score maximal
            return max(scores)


def sontCompatibles(x, y):
    return x == y or x == y + 1 or x == y - 1


MEMO = {}  # variable globale


def dynamique(T, s):
    """ Q4 : En ajoutant une mémoire à votre fonction, utiliser la programmation dynamique pour résoudre ce problème
    (approche top-down)"""
    # Création d'une clé pour le dictionnaire
    cle = str(T) + "/" + str(s)

    if cle in MEMO.keys():  # Si ce noeud a déjà été calculé
        return MEMO[cle]  # Renvoie de la valeur mémorisée

    elif len(T) == 1:
        MEMO[cle] = sontCompatibles(T[0], s)  # Mémorisation de la valeur
        return sontCompatibles(T[0], s)

    else:
        scores = []
        for carte in T:
            if sontCompatibles(carte, s):
                Tbis = T.copy()
                Tbis.remove(carte)
                scores.append(1 + dynamique(Tbis, carte))

        if len(scores) == 0:
            MEMO[cle] = 0
            return 0
        else:
            MEMO[cle] = max(scores)  # Mémorisation
            return max(scores)


def dynamiqueAvecSolution(T, s):
    """ Q5 : Modifier votre fonction pour permettre de récupérer l'ordre des cartes à jouer"""
    cle = str(T) + "/" + str(s)

    if cle in MEMO.keys():
        return MEMO[cle], []

    elif len(T) == 1:
        # Construction du premier terme de la solution
        solution = [T[0], ] if sontCompatibles(T[0], s) else []
        MEMO[cle] = sontCompatibles(T[0], s)
        return sontCompatibles(T[0], s), solution

    else:
        scores, solutions = [], []
        for c in T:
            if sontCompatibles(c, s):
                Tbis = T.copy()
                Tbis.remove(c)
                l, solution = dynamiqueAvecSolution(Tbis, c)
                solution.append(c)  # Ajoute une carte à la solution
                scores.append(1 + l)
                solutions.append(solution)

        if len(scores) == 0:
            MEMO[cle] = 0
            return 0, []
        else:
            i = scores.index(max(scores))
            MEMO[cle] = max(scores)
            # On renvoie la solution associée au meilleur score
            return max(scores), solutions[i]


if __name__ == '__main__':
    print("Solution Gloutonne : ", glouton([6, 5, 8, 7, 4, 6], 7))
    print("Solution Dynamique : ", dynamique([6, 5, 8, 7, 4, 6], 7))
    MEMO = {}
    print("Solution Dynamique : ", dynamiqueAvecSolution([6, 5, 8, 7, 4, 6], 7))
