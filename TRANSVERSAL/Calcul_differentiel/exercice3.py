"""
    Cours : Calcul différentiel
    Exercice : Simulation d'un filtre passe-bas du premier ordre
"""
import numpy as np
import matplotlib.pyplot as plt


def sys_analytique_echelon(t, E, tau):
    """ Q1 : Ecrire une fonction sys_analytique_echelon(t,E,tau) qui calcule la réponse exacte du système à un échelon E à
    l'instant t"""
    return E * (1 - np.exp(-t / tau))


def sys_euler_av(En, sn, tau, dt):
    """ Q2 : Ecrire une fonction sys_euler_av(s,e,tau,dt) qui calcule s(t+\Delta t) en fonction de s(t), e(t), tau et Delta t
     avec la méthode d'Euler avant."""
    return (En - sn) / tau * dt + sn


def sys_euler_ar(E_next, sn, tau, dt):
    """ Q3 : De même, écrire une fonction sys_euler_ar(s,e,tau,dt) qui calcule s(t+\Delta t) en fonction de s(t),
    e(t+\Delta t), tau et \Delta t avec la méthode d'Euler arrière."""
    return (E_next * dt + sn * tau) / (tau + dt)


def compare(p):
    """ Q4 : Comparer les réponses issues des deux méthodes pour un échelon, pour différents rapports Delta t / tau.
    Commentez et expliquez notamment ce qui se passe pour Delta t / tau >= 2. Quelle méthode peut-on utiliser pour une
    simulation en temps réel ?"""
    tau = 3
    dt = p * tau  # on peut changer dt/tau à cette ligne
    S_av, S_ar, S_ref, t = [0], [0], [0], [0]
    E = 1

    for k in range(1, 30):
        t.append(dt * k)
        S_av.append(sys_euler_av(E, S_av[k - 1], tau, dt))  # simulation avec Euler avant
        S_ar.append(sys_euler_ar(E, S_ar[k - 1], tau, dt))  # simulation avec Euler arrière
        S_ref.append(sys_analytique_echelon(k * dt, E, tau))  # calcul analytique
    return t, S_av, S_ar, S_ref


if __name__ == '__main__':
    fig = plt.figure()
    for i, tau in enumerate([0.5, 1.9, 2, 2.1]):
        plt.subplot(2, 2, i + 1)
        t, S_av, S_ar, S_ref = compare(tau)
        plt.plot(t, S_av, '--k', t, S_ar, ':k', t, S_ref, '-k')
        plt.legend(['Euler avant', 'Euler arrière', 'Analytique'])
        plt.title(f"Réponse du système à un échelon unitaire - dt/tau = {tau}")
        plt.xlabel('temps (s)')
        plt.ylabel('sortie')
        plt.grid()
    plt.show()
