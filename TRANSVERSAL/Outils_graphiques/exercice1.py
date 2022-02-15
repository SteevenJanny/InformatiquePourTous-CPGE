"""
    Cours : Outils Graphiques
    Exercice : Filtre passe-bas du second ordre
"""
import matplotlib.pyplot as plt
import numpy as np

K1 = 5e-3
K2 = 1.65e-4


def phase(omega):
    """ Q1.1 : Écrire la fonction phase(omega) qui prend en entrée une liste de pulsations omega et qui renvoie la
    liste des phases correspondantes en radians phi(omega)=arg(H(j omega))"""
    return np.angle(1 / (1 + K1 * omega * 1j - K2 * omega ** 2))


def gain_db(omega):
    """ Q1.2 : Écrire la fonction gain_db(omega) qui prend en entrée une liste de pulsations omega et qui renvoie la
    liste des gains correspondants en décibels  G_dB(omega)=20log(|H(j omega)|)"""

    return 20 * np.log10(np.absolute(1 / (1 + K1 * omega * 1j - K2 * omega ** 2)))


def diagramme_bode():
    """ Q2.1 : Tracer le diagramme de Bode en phase du filtre, c'est-à-dire la phase phi(omega) en fonction de la
    pulsation omega, pour omega allant de 10 à 1000 rad/s. On rappelle que l'échelle des pulsations doit être
    logarithmique
    Q2.2 : Tracer le diagramme de Bode en gain du filtre, c'est-à-dire le gain G_dB(omega) en fonction de la pulsation
    omega, pour omega allant de 10 à 1000 rad/s.  On rappelle que l'échelle des pulsations doit être logarithmique
    Q2.3 : Afficher les deux graphiques dans la même fenêtre, l'un en-dessous de l'autre"""

    omega = 10 ** np.linspace(1, 3, 100)  # 100 valeurs de omega allant de 10^1 à 10^3
    graduations = [10 * i for i in range(1, 10)] + [100 * i for i in range(1, 11)]

    plt.figure()  # crée la fenêtre

    plt.subplot(211)  # premier sous-graphique
    plt.title('Diagramme de Bode en gain')
    plt.semilogx(omega, gain_db(omega))
    plt.xlabel('Pulsation (rad/s)')
    plt.ylabel('Amplitude (dB)')
    plt.xticks(graduations)
    plt.grid()

    plt.subplot(212)  # deuxième sous-graphique
    plt.title('Diagrame de Bode en phase')
    plt.semilogx(omega, phase(omega))
    plt.xlabel('Pulsation (rad/s)')
    plt.ylabel('Phase (rad)')
    plt.xticks(graduations)
    plt.grid()

    plt.tight_layout()  # ajuste les marges de la fenêtre
    plt.show()


def reponse_temporelle():
    """ Q3 : Tracer la réponse temporelle du filtre à une entrée e(t)=5 cos(2 pi x 10+1). On affichera l'entrée et la
    sortie du filtre sur le même graphique. Attention, il faut utiliser le gain "normal" (i.e. le gain linéaire), pas
    celui en décibels"""

    # Caracteristiques de l'entrée
    freq = 10  # frequence
    periode, omega = 1 / freq, 2 * np.pi * freq  # periode et pulsation
    amplitude_e, phase_e = 5, 1  # amplitude et phase

    # Calcul des caracteristiques de la sortie
    amplitude_s = amplitude_e * np.absolute(1 / (1 + K1 * omega * 1j - K2 * omega ** 2))
    phase_s = phase_e + phase(omega)

    # Affichage
    t = np.linspace(0, 2 * periode, 100)  # on affichera la réponse temporelle sur 2 periodes
    e = amplitude_e * np.cos(omega * t + phase_e)
    s = amplitude_s * np.cos(omega * t + phase_s)

    plt.figure()
    plt.plot(t, e, linestyle='-.', label='entree')
    plt.plot(t, s, linestyle=':', label='sortie')
    plt.title('Reponse temporelle du filtre à une entrée sinusoidale de frequence {} Hz'.format(freq))
    plt.xlabel('Temps (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.legend()
    plt.show()


def diagramme_mesure():
    """ Q4 : Sur le même graphique, tracer le diagramme de Bode théorique en gain et le nuage de points correspondant
    au diagramme de Bode en gain expérimental du filtre. Les points correspondant aux pulsations dans la bande passante
    devront être rouges et plus gros que les autres points, qui eux devront être bleus"""

    omega_th = 10 ** np.linspace(1, 3, 100)  # valeurs théoriques
    gain_th = gain_db(omega_th)
    omega_exp = [10, 50, 80, 100, 500, 1000]  # valeurs expérimentales
    gain_exp = [0, 4, 6.9, 1.7, -32, -44.5]
    c = ['red' if g > -3 else 'blue' for g in gain_exp]  # liste des couleurs
    s = [50 if g > -3 else 20 for g in gain_exp]  # liste des tailles des points
    plt.figure()
    plt.title('Diagramme de Bode en gain (théorique et expérimental)')
    plt.semilogx(omega_th, gain_th)
    plt.scatter(omega_exp, gain_exp, s=s, c=c)
    plt.xlabel('Pulsation (rad/s)')
    plt.ylabel('Amplitude (dB)')
    # plt.xticks(graduations)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    diagramme_bode()
    reponse_temporelle()
    diagramme_mesure()
