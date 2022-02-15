"""
    Cours : Traitement d'images
    Exercice : Horses and Horses and Horses
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

img = data.horse()


def symetrie(img):
    """ Q1 : Écrire une fonction symetrie(img) qui prend en argument une image img monochrome et renvoie l'image obtenue
    par symétrie autour de l'axe vertical passant par le milieu de l'image d'origine."""
    hauteur, largeur = img.shape
    img_sym = np.zeros(img.shape)  # nouvelle matrice
    for i in range(hauteur):
        for j in range(largeur):
            img_sym[i, largeur - 1 - j] = img[i, j]  # img[ i', j' ] = img[ i, j ]
    return img_sym


def rotation(img):
    """ Q2 : Écrire une fonction rotation(img) qui prend en argument une image img monochrome et renvoie l'image
    obtenue par rotation de 90° dans le sens horaire."""
    hauteur, largeur = img.shape
    img_rot = np.zeros((largeur, hauteur))  # dimensions transposées
    for i in range(hauteur):
        for j in range(largeur):
            img_rot[j, hauteur - 1 - i] = img[i, j]
    return img_rot


def negatif(img):
    """ Q3 : Écrire une fonction negatif(img) qui prend en argument une image img monochrome et renvoie son négatif,
    c'est-à-dire l'image dans laquelle chaque pixel de l'image d'origine est remplacé par sa valeur complémentaire."""
    return np.invert(img)


def photomaton(img):
    """ Q4 : Écrire une fonction photomaton(img) qui prend en argument une image img monochrome et renvoie l'image
    obtenue par transformation du photomaton"""
    hauteur, largeur = img.shape
    img_photo = np.zeros(img.shape)
    for i in range(hauteur):
        for j in range(largeur):
            i_photo, j_photo = coord(i, j, largeur, hauteur)
            img_photo[int(i_photo), int(j_photo)] = img[i, j]
    return img_photo


def coord(i, j, largeur, hauteur):
    if i % 2 == 0:
        if j % 2 == 0:
            return i / 2, j / 2
        return i / 2, (j - 1) / 2 + largeur / 2
    else:
        if j % 2 == 0:
            return (i - 1) / 2 + hauteur / 2, j / 2
        return (i - 1) / 2 + hauteur / 2, (j - 1) / 2 + largeur / 2


def periode_photomaton(img):
    """ Q5 : Écrire une fonction periode_photomaton(img) qui prend en argument une image img monochrome et renvoie le
    nombre de transformations du photomaton successives nécessaires pour revenir à l'image d'origine."""
    plt.figure()
    x = photomaton(img)
    T = 1
    while (x != img).any():
        x = photomaton(x)
        plt.clf()
        plt.imshow(x)
        plt.pause(0.1)
        T += 1
    return T


def masque(img):
    """ Q6 : Écrire une fonction masque(img) qui prend en argument une image img monochrome et renvoie l'image obtenue
    en appliquant un masque circulaire à img"""
    hauteur, largeur = img.shape
    img_masque = np.zeros(img.shape)
    rayon = min(hauteur, largeur) / 2
    for i in range(hauteur):
        for j in range(largeur):
            if (i - hauteur / 2) ** 2 + (j - largeur / 2) ** 2 < rayon ** 2:
                img_masque[i, j] = img[i, j]
            else:
                img_masque[i, j] = 0
    return img_masque


def convolution(img, C):
    """ Q7 : Écrire une fonction convolution(img, C) qui prend en argument une image img monochrome et une matrice 
    carrée V de taille 3x3 et renvoie l'image obtenue par filtrage avec C comme noyau de convolution."""
    hauteur, largeur = img.shape
    img_conv = np.zeros(img.shape)
    for i in range(hauteur):
        for j in range(largeur):
            if i in [0, hauteur - 1] or j in [0, largeur - 1]:  # on n'y touche pas
                img_conv[i, j] = img[i, j]
            else:  # on centre mentalement le noyau sur le pixel [i, j]
                img_conv[i, j] = np.multiply(img[i - 1:i + 2, j - 1:j + 2], C).sum()
    return img_conv


if __name__ == '__main__':
    plt.figure()
    plt.subplot(2, 2, 1)
    plt.imshow(img)

    # Symetrie
    plt.subplot(2, 2, 2)
    plt.imshow(symetrie(img))
    plt.title("Symétrie")

    # Rotation
    plt.subplot(2, 2, 3)
    plt.imshow(img)
    plt.imshow(rotation(img))
    plt.title("Rotation")

    # Négatif
    plt.subplot(2, 2, 4)
    plt.imshow(img)
    plt.imshow(negatif(img))
    plt.title("Négatif")

    # Photomaton
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.subplot(1, 2, 2)
    plt.imshow(photomaton(img))

    plt.show()

    print("Période photomaton : ", periode_photomaton(img))

    C = np.array([[-2, -1, 0],
                  [-1, 1, 1],
                  [0, 1, 2]])
    img_mystere = convolution(img, C)
    plt.figure()
    plt.imshow(img_mystere)
