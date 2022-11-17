"""
    Cours : Théorie des jeux
    Exercice : Minimax et Tic-Tac-Toe
"""
import matplotlib.pyplot as plt
import numpy as np

ORDI = 1
HUMAIN = -1
arene = np.zeros((3, 3))


def estGagnant(arene, joueur):
    """ Q1 : Coder une fonction estGagnant(arene, joueur) qui renvoie True si joueur gagne la partie, et False sinon. En déduire
    une fonction gameover(arene) qui renvoie True si la partie est gagnée par l'un des joueurs et False sinon"""
    conditionsGains = [  # Liste de toutes les combinaisons possibles
        [arene[0, 0], arene[0, 1], arene[0, 2]],  # Ligne 1
        [arene[1, 0], arene[1, 1], arene[1, 2]],  # Ligne 2
        [arene[2, 0], arene[2, 1], arene[2, 2]],  # Ligne 3
        [arene[0, 0], arene[1, 0], arene[2, 0]],  # Colonne 1
        [arene[0, 1], arene[1, 1], arene[2, 1]],  # Colonne 2
        [arene[0, 2], arene[1, 2], arene[2, 2]],  # Colonne 3
        [arene[0, 0], arene[1, 1], arene[2, 2]],  # Diagonale 1
        [arene[2, 0], arene[1, 1], arene[0, 2]], ]  # Diagonale 1
    if [joueur, joueur, joueur] in conditionsGains:  # Test victoire
        return True
    else:
        return False


def gameover(arene):
    return estGagnant(arene, HUMAIN) or estGagnant(arene, ORDI)


def casesVides(arene):
    """ Q2 : Coder une fonction casesVides(arene) qui renvoie la liste des cases vides de l'arène"""
    cases = []  # Liste accueillant les cases libres
    for x in range(3):
        for y in range(3):
            if arene[x][y] == 0:  # Si la case est libre...
                cases.append([x, y])  # ... on l'ajoute à la liste
    return cases


def jouerHumain(arene):
    """ Q3 : Coder une fonction jouerHumain(arene) qui demande à l'utilisateur de choisir une case, puis modifie l'arène
    en conséquence et la renvoie. On prendra soin d'empêcher de jouer sur une case déjà prise"""
    moves = {  # Dictionnaire de conversion entier -> ligne/colonne dans arene
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2], }

    print(arene)  # Affiche l'arène
    move = int(input('Choisir case: '))  # Conversion de l'entrée en int
    x, y = moves[move]
    while [x, y] not in casesVides(arene):  # Demande une case tant qu'elle n'est pas libre
        move = int(input('Choisir case: '))
        x, y = moves[move]
    arene[x][y] = HUMAIN  # Modifie la case correspondante
    return arene


def evaluation(arene):
    """ Q4 : Coder une fonction evaluation(arene) qui renvoie 1 si le joueur 1 gagne, -1 s'il perd et 0 en cas de match nul"""
    if estGagnant(arene, ORDI):
        return 1
    elif estGagnant(arene, HUMAIN):
        return -1
    return 0


def minimax(arene, joueur):
    """ Q5 : A l'aide de l'algorithme décrit dans le cours, coder une fonction minimax(arene, joueur) qui renvoie le
    meilleur coup à jouer selon l'algorithme minimax"""
    # Si la partie est terminée...
    if len(casesVides(arene)) == 0 or gameover(arene):
        score = evaluation(arene)  # Evalue l'arène
        return None, score  # Renvoie le score et None pour la position

    # Initialisation de la sortie
    scores, coups = [], []
    for x, y in casesVides(arene):  # Pour chaque coup possible
        arene[x, y] = joueur  # Joue le coup
        _, score = minimax(arene, -joueur)  # Evalue le coup
        arene[x, y] = 0  # Annule le coup

        scores.append(score)
        coups.append((x, y))

    if joueur == ORDI:  # On doit maximiser le score
        idx = np.argmax(scores)
        return coups[idx], scores[idx]
    else:  # On doit minimiser le score
        idx = np.argmin(scores)
        return coups[idx], scores[idx]


def jouerIA(arene):
    """ Q6 : Coder une fonction jouerIA() qui calcule un coup à jouer avec minimax puis modifie l'arène en
    conséquence."""
    print(arene)  # Affichage de l'arène
    (x, y), score = minimax(arene, ORDI)
    arene[x][y] = ORDI  # On joue sur la case choisie
    return arene


def jouer():
    """ Q7 : Enfin, coder une fonction jouer() qui simule une partie entre l'humain et l'ordinateur."""
    global arene
    while len(casesVides(arene)) > 0 and not gameover(arene):
        arene = jouerHumain(arene)
        if len(casesVides(arene)) == 0 or gameover(arene):
            break
        arene = jouerIA(arene)

    if estGagnant(arene, HUMAIN):
        print(arene)
        print('Vous avez gagné !')
    elif estGagnant(arene, ORDI):
        print(arene)
        print('Vous avez perdu !')
    else:
        print(arene)
        print('Egalité !')


if __name__ == '__main__':
    jouer()
