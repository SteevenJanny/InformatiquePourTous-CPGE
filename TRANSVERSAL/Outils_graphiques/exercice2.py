"""
    Cours : Outils Graphiques
    Exercice : Mouvements de planètes
"""
import matplotlib.pyplot as plt
import numpy as np

rayon_terre = 150e6  # en km
periode_terre = 365 * 24 * 3600  # en s

rayon_venus = 108e6  # en km
periode_venus = 225 * 24 * 3600  # en s


def traj_terre():
    """ Q1 : Tracer la trajectoire de la Terre dans le référentiel héliocentrique en pointillés. Représenter le Soleil
    par un point."""
    t1 = np.linspace(0, periode_terre, 100)  # 100 échantillons répartis sur un an
    v1 = 2 * np.pi / periode_terre  # vitesse angulaire : 1 tour (2pi radians) en 1 an
    theta1 = t1 * v1  # positions angulaires

    plt.figure()
    plt.plot(rayon_terre * np.cos(theta1), rayon_terre * np.sin(theta1), linestyle=':', label="Terre")
    plt.scatter([0], [0])
    plt.axis('equal')
    plt.axis('off')
    plt.show()


def traj_venus():
    """ Q2 : Ajouter, sur le même graphique, la trajectoire de Vénus dans le référentiel héliocentrique en pointillés
    mixtes. Légender"""
    t2 = np.linspace(0, periode_venus, 100)  # temps
    v2 = 2 * np.pi / periode_venus  # vitesse angulaire
    theta2 = t2 * v2  # positions angulaires

    t1 = np.linspace(0, periode_terre, 100)  # 100 échantillons répartis sur un an
    v1 = 2 * np.pi / periode_terre  # vitesse angulaire : 1 tour (2pi radians) en 1 an
    theta1 = t1 * v1  # positions angulaires

    plt.plot(rayon_terre * np.cos(theta1), rayon_terre * np.sin(theta1), linestyle=':', label="Terre")
    plt.plot(rayon_venus * np.cos(theta2), rayon_venus * np.sin(theta2), linestyle='-.', label='Venus')
    plt.scatter(0, 0, label='Soleil')
    plt.axis('equal')
    plt.axis('off')
    plt.legend()
    plt.show()


def traj_geocentrique():
    """ Q3 : Tracer, sur la même fenêtre, la trajectoire de Vénus dans le référentiel géocentrique sur 1 an, 5 ans,
    10 ans et 20 ans."""
    nb_annees = [2, 5, 10, 20]
    plt.figure()
    idx_subplot = 1
    t2 = np.linspace(0, periode_venus, 100)  # temps
    v2 = 2 * np.pi / periode_venus  # vitesse angulaire
    theta2 = t2 * v2  # positions angulaires

    t1 = np.linspace(0, periode_terre, 100)  # 100 échantillons répartis sur un an
    v1 = 2 * np.pi / periode_terre  # vitesse angulaire : 1 tour (2pi radians) en 1 an
    theta1 = t1 * v1  # positions angulaires

    for n in nb_annees:
        plt.subplot(2, 2, idx_subplot)  # fixe l'emplacement du sous-graphe actuel
        t = np.linspace(0, n * periode_terre, 1000)  # on augmente le nombre d'échantillons pour lisser les courbes
        theta1, theta2 = t * v1, t * v2  # positions angulaires
        x_soleil = rayon_terre * np.cos(theta1)
        y_soleil = rayon_terre * np.sin(theta1)
        x_venus = x_soleil + rayon_venus * np.cos(theta2)
        y_venus = y_soleil + rayon_venus * np.sin(theta2)
        plt.plot(x_venus, y_venus, linestyle='--')
        plt.scatter(0, 0)
        plt.axis('equal')
        plt.axis('off')
        plt.title("Sur {} ans".format(n))
        idx_subplot += 1  # on passera au sous-graphe suivant
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    traj_terre()
    traj_venus()
    traj_geocentrique()
