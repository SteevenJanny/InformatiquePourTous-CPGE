"""
    Cours : Calcul différentiel
    Exercice : Correcteur PID bruité
"""
import numpy as np
import matplotlib.pyplot as plt

Ki, Kp, Kd = 50, 10, 1e-2  # paramètres du PID
dt = 1e-4  # intervalle de temps élémentaire, à faire varier
SIGMA = 1e-2  # écart type du bruit (à modifier) ; 0 = pas de bruit


def PID(Ki, Kp, Kd, e_list, dt):
    """ Q1 : Coder une fonction PID(Kp,Ki,Kd,eps_list,dt) qui renvoie la sortie de ce correcteur en fonction des
    différents gains K_p, K_i, K_d, de la liste de ses précédentes entrées epsilon et de Delta t."""

    # on commence par reconstruire la liste t pour le calcul de l'intégrale :
    t = np.linspace(0, dt * (len(e_list) - 1), len(e_list))
    P = Kp * e_list[-1]  # contribution proportionnelle (au dernier échantillon)
    I = Ki * rectg(t, e_list)  # contribution intégrale (méthode des rectangles à gauche)
    D = Kd * (e_list[-1] - e_list[-2]) / dt  # contribution dérivée (Euler arrière)
    return P + I + D


def rectg(X, fX):
    integrale = 0
    for i in range(0, len(X) - 1):
        integrale += (X[i + 1] - X[i]) * fX[i + 1]
    return integrale


def compare():
    """ Q2 : Comparer les sorties de ce correcteur lorsqu'il est soumis à un échelon unitaire exact et bruité, pour
    K_p=10, K_i=50, K_d=10^{-2}, pour plusieurs valeurs de \Delta t. """
    E_bruit, S_pid_bruit, t = [1], [0], [0]

    for k in range(1, int(1 / dt)):
        t.append(dt * k)
        E_bruit.append(1 + np.random.normal(0, SIGMA))  # échelon bruité
        S_pid_bruit.append(PID(Ki, Kp, Kd, E_bruit, dt))

    plt.figure()
    plt.plot(t, S_pid_bruit, 'k')
    plt.xlabel("temps (s)")
    plt.ylabel("sortie")
    plt.title('Réponse du PID à un échelon exact (dt={:.2e} s)'.format(dt))
    plt.grid()
    plt.show()

    sigma = 1e-2  # écart type du bruit (à modifier) ; 0 = pas de bruit
    E_bruit = [1]
    S_pid_bruit = [0]

    for k in range(1, int(1 / dt)):
        E_bruit.append(1 + np.random.normal(0, sigma))  # échelon bruité
        S_pid_bruit.append(PID(Ki, Kp, Kd, E_bruit, dt))

    plt.figure()
    plt.plot(t, S_pid_bruit, 'k')
    plt.xlabel("temps (s)")
    plt.ylabel("sortie")
    plt.title('Réponse du PID à un échelon bruité (dt={:.2e} s)'.format(dt))
    plt.grid()
    plt.show()


def sys_euler_av(En, sn, tau, dt):
    return (En - sn) / tau * dt + sn


def boucle_ferme():
    """ Q3 : Implémenter ce correcteur afin de corriger le système constitué du filtre passe-bas de l'exercice précédent
    en présence et en l'absence de bruit. On pourra prendre K_p=10, K_i=50, K_d=10^{-2}, ainsi qu'un écart-type
    sigma=10^{-2} pour le bruit"""

    tau = 0.3  # on peut faire varier tau
    E, S_pid_bruit, S_BF_bruit, erreur_bruit = [0], [0], [0], [0]
    t, bruit = [0], [0]
    for n in range(1, int(1 / dt)):
        E.append(1)
        bruit.append(np.random.normal(0, SIGMA))
        t.append(dt * n)
        erreur_bruit.append(E[-1] - S_BF_bruit[-1] + bruit[-1])
        S_pid_bruit.append(PID(Ki, Kp, Kd, erreur_bruit, dt))
        # sortie du système (cf exercice 1)
        S_BF_bruit.append(sys_euler_av(S_pid_bruit[-1], S_BF_bruit[-1], tau, dt))
    plt.figure()
    plt.plot(t, S_BF_bruit, 'k')
    plt.xlabel("temps (s)")
    plt.ylabel("sortie")
    plt.title('Réponse de la boucle fermée à un échelon bruité (dt={:.2e} s)'.format(dt))
    plt.grid()
    plt.show()


def gain_ftbf(f, Ki, Kd, Kp, tau):
    w = 2 * np.pi * f
    num = np.sqrt((Ki - Kd * w ** 2) ** 2 + (Kp * w) ** 2)
    den = np.sqrt((Ki - (Kd + tau) * w ** 2) ** 2 + ((1 + Kp) * w) ** 2)
    return num / den


if __name__ == '__main__':
    compare()
    boucle_ferme()
