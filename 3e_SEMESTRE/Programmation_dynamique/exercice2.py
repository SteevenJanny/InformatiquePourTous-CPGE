"""
    Cours : Programmation Dynamique
    Exercice : Plus grand carré blanc
"""
import numpy as np
import matplotlib.pyplot as plt


def get_image(N, p=0.1):
    """ N : Taille de l'image
        p : proportion de points noirs"""
    image = np.random.random((N, N)) > p
    return image.astype(float)


def T(x, y, memo):
    """ Q2 : Coder une fonction en programmation dynamique top-down qui, pour chaque pixel (x, y), calcule T(x,y)."""
    if memo[x, y] != -1:  # Si le calcul a déjà été effectué pour ce pixel
        return memo, memo[x, y]  # Renvoyer la valeur
    if x == 0 or y == 0:  # Condition d'arrêt 1
        return memo, 1
    elif IMG[x, y] == 0:  # Condition d'arrêt 2
        return memo, 0
    else:
        # Calcul des sous-carrés
        memo, P1 = T(x - 1, y - 1, memo)
        memo, P2 = T(x - 1, y, memo)
        memo, P3 = T(x, y - 1, memo)
        value = 1 + min(P1, P2, P3)  # Formule de récurrence
        memo[x, y] = value  # Mise à jour de la mémoire
        return memo, value


def T_bottomup():
    """ Q3 : Coder la même fonction, mais avec une approche bottom-up."""
    memo = np.zeros((N, N))  # Matrice de mémoire
    for x in range(N):
        for y in range(N):
            if IMG[x, y] == 0:  # Condition d'arrêt 1
                memo[x, y] = 0
            elif x == 0 or y == 0:  # Condition d'arrêt 2
                memo[x, y] = 1
            else:
                memo[x, y] = 1 + min(memo[x - 1, y - 1], memo[x - 1, y], memo[x, y - 1])
    return memo


def plus_grand_carre_blanc(image):
    """ Q4 : Coder une fonction qui affiche le plus grand carré blanc dans une image. On pourra par exemple colorier
    d'une couleur différente les pixels de ce carré."""
    # Calcul des carrés maximaux
    memo = T_bottomup()

    # Recherche du maximum
    x, y = np.unravel_index(np.argmax(memo), memo.shape)
    # Coloriage
    N = int(np.max(memo))
    IMG_colorie = IMG.copy()
    # Coloriage rapide par slicing !
    IMG_colorie[x - N + 1:x + 1, y - N + 1:y + 1] = 0.5

    plt.subplot(131)
    plt.imshow(IMG, cmap="gray")
    plt.axis("off")
    plt.title("Image d'origine")

    plt.subplot(132)
    plt.imshow(IMG_colorie, cmap="gray")
    plt.axis("off")
    plt.title("Position du carré")

    plt.subplot(133)
    plt.imshow(memo, cmap="gray")
    plt.axis("off")
    plt.title("Mémoire de l'algorithme")
    plt.show()


if __name__ == '__main__':
    N = 50
    IMG = get_image(N)
    memo = -np.ones((N, N))
    for x in range(N):
        for y in range(N):
            memo, _ = T(x, y, memo)
    # Génération de l'image
    IMG = get_image(N=50, p=0.1)
    plus_grand_carre_blanc(IMG)
