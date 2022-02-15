"""
    Cours : Introduction à l'apprentissage profond
    Exercice : Descente de gradient à la main
"""

import numpy as np

X = [np.array([[1], [1]]), np.array([[1], [0]]), np.array([[0], [1]]), np.array([[0], [0]])]
Y = [0, 1, 1, 0]


def sigmoid(x):
    """ Q1 : Dans le corps du script, coder deux listes X, Y contenant les entrées/sorties du problème sous forme de
    vecteurs colonnes. De plus, coder une fonction sigmoid(x) qui renvoie sigma(x), ainsi que la fonction dérivée
    correspondante."""
    return 1 / (1 + np.exp(-x))


def sigmoid_prime(x):
    return np.exp(-x) / (1 + np.exp(-x)) ** 2


def prediction(x, W1, W2, b1, b2):
    """ Q2 : """
    z1 = W1 @ x + b1
    a1 = sigmoid(z1)
    z2 = W2 @ a1 + b2
    y = sigmoid(z2)
    return y


def test_prediction():
    W1 = np.random.randn(2, 2)
    W2 = np.random.randn(1, 2)
    b1 = np.random.randn(2, 1)  # Attention aux dimensions !
    b2 = np.random.randn(1, 1)
    for (x, y) in zip(X, Y):
        y_hat = prediction(x, W1, W2, b1, b2)
        print(f"\t Entrée : {x[0]} {x[1]} Sortie : {y_hat} Bonne réponse : {y}")


def gradient(x, y, W1, W2, b1, b2):
    """ Q4 : Coder une fonction gradient(x, y, W1, W2, b1, b2) qui renvoie les gradients de chaque paramètre."""
    z1 = W1 @ x + b1  # D'abord on applique le réseau de neurones
    a1 = sigmoid(z1)
    z2 = W2 @ a1 + b2
    y_hat = sigmoid(z2)
    # Dérivées de la couche de sortie
    db2 = y_hat - y
    dW2 = (y_hat - y) * a1.T

    # Dérivées de la couche d'entrée
    db1 = W2.T @ (y_hat - y) * sigmoid_prime(z1)
    dW1 = db1 @ x.T
    return dW1, db1, dW2, db2


def descente(W1, W2, b1, b2, alpha=1):
    """ Q5 : Implémenter la descente de gradient en vous aidant de l'algorithme suivant (alpha=1, K =1000)"""
    for _ in range(1000):  # 1000 itérations de descente
        for (x, y) in zip(X, Y):  # Pour chaque donnée dans D
            dW1, db1, dW2, db2 = gradient(x, y, W1, W2, b1, b2)  # Calcul Gradient
            W1 = W1 - alpha * dW1  # Mise à jour des poids
            W2 = W2 - alpha * dW2
            b1 = b1 - alpha * db1
            b2 = b2 - alpha * db2
    return W1, W2, b1, b2


if __name__ == '__main__':
    print("Test prédiction : ")
    test_prediction()

    W1 = np.random.randn(2, 2)
    W2 = np.random.randn(1, 2)
    b1 = np.random.randn(2, 1)
    b2 = np.random.randn(1, 1)

    print("Entrainement : ")
    W1, W2, b1, b2 = descente(W1, W2, b1, b2)
    for (x, y) in zip(X, Y):
        y_hat = prediction(x, W1, W2, b1, b2)
        print(f"\t Entrée : {x[0]} {x[1]} Sortie : {y_hat} Bonne réponse : {y}")
