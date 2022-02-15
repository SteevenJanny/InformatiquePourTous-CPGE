import numpy as np
import matplotlib.pyplot as plt

N = 100  # nombre de spires
R = 0.05  # rayon du tore (m)


def mu(B):
    """ Q1 : Ecrire une fonction mu(B), qui renvoie la valeur de la perméabilité pour un champ magnétique B donné.
    Tracer la courbe B(H) anhystérétique de ce matériau magnétique entre 0 et 2T. H étant l'excitation magnétique en
    A/m"""
    return 1 / (100 + 10 * np.exp(1.8 * B ** 2))


def affiche_cycle_anhysteretique():
    B = np.linspace(0, 2, 100)
    h = B / mu(B)

    plt.figure()
    plt.plot(h, B, 'k')
    plt.xlabel("H (A/m)")
    plt.ylabel("B (T)")
    plt.title('Courbe B(H)')
    plt.grid()
    plt.show()


def f(B, I):
    """ Q2 : Exprimer le problème à résoudre sous forme de recherche de zéro d'une fonction f(B, I) qu'on implémentera 
     la tracer pour i=5A, N=100, R=5cm."""
    return B / mu(B) - N * I / (2 * np.pi * R)


def affiche_f():
    B = np.linspace(0, 2, 100)
    F = f(B, I=5)

    plt.figure()
    plt.plot(B, F, 'k')
    plt.xlabel("B (T)")
    plt.ylabel("f(B) (A/m)")
    plt.title('Fonction à annuler')
    plt.grid()
    plt.show()


def dmudb(B):
    """ Q3 : Exprimer la dérivée df/dB et écrire la fonction Python associée dfdB(B)"""
    return -(36 * B * np.exp(1.8 * B ** 2)) / (10 * np.exp(1.8 * B ** 2) + 100) ** 2


def dfdb(B):
    return (mu(B) - B * dmudb(B)) / mu(B) ** 2


def erreur(B, I):
    """ Q4 : Ecrire une fonction erreur(B, I) qui estime la valeur absolue de l'écart entre la valeur de B courante et
    la valeur exacte (mais inconnue) B(I). On majorera cette estimation de l'erreur par epsilon_max = 1 T"""
    err = abs(f(B, I) / dfdb(B))
    if np.isnan(err) or np.isinf(err) or np.isinf(dfdb(B)) or err > 1:
        return 1  # il est possible de rencontrer des NaN ou des infinis en cas de divergence
    return err  # NaN = not a number (ex : division par 0), inf = overflow (ex : np.exp(1000))


def seq(I, err_max, B=0):
    """ Q5 : Coder une fonction seq(I, err_max) permettant de trouver le champ magnétique B pour un courant I donné,
    avec une précision sur B donnée par err_max."""
    while f(B, I) * f(B + err_max, I) > 0:
        B += err_max
    return B


def trace_sequentiel():
    """ Q6 : Tracer la courbe B(I) pour I allant de 0 à 10A pour une erreur absolue sur B de 1e-2 T"""
    I = np.linspace(0, 10, 501)
    B = [0]
    for i in I[1:]:
        B.append(seq(i, 1e-2, B=B[-1]))  # sans le "B = B[-1]", on est bien moins efficace !
    plt.figure()
    plt.plot(I, B, 'k')
    plt.xlabel("I (A)")
    plt.ylabel("B (T)")
    plt.title('Intensité du champ magnétique obtenue par recherche séquentielle')
    plt.grid()
    plt.show()


def dichot(I, Binf, Bsup, err_max):
    """ Q8 : {Implémenter une fonction dichot(I, Binf, Bsup, err_max) permettant de trouver le champ magnétique B
    compris entre Binf et Bsup pour un courant I donné, avec une précision donnée par err_max."""
    while Bsup - Binf > err_max:
        Bmid = (Bsup + Binf) / 2
        if f(Binf, I) * f(Bmid, I) <= 0:
            Bsup = Bmid
        else:
            Binf = Bmid
    return Bmid


def trace_dichotomie():
    I = np.linspace(0, 10, 501)
    B = [0]
    for i in I[1:]:
        B.append(dichot(i, 0, 2, 1e-2))
    plt.figure()
    plt.plot(I, B, 'k')
    plt.xlabel("I (A)")
    plt.ylabel("B (T)")
    plt.title('Intensité du champ magnétique obtenue par recherche séquentielle')
    plt.grid()
    plt.show()


def point_fixe(I, err_max, it_max=100, B=0):
    """ Q10 : Implémenter une fonction point_fixe(I, err_max, it_max) qui calcule les termes de la suite u jusqu'à
    atteindre n=it_max ou bien une erreur inférieure à err_max, et qui renvoie le dernier terme calculé ainsi que
    l'erreur associée."""
    err = err_max + 1
    it = 0
    while err > err_max and it < it_max:
        B = N * I / (2 * np.pi * R) * mu(B)
        err = erreur(B, I)
        it += 1
    return B, err


def dhdB(B, I):
    return 1 - dmudb(B) * f(B, I) - mu(B) * dfdb(B)


def trace_pointfixe():
    """ Q11 : Tester cette fonction pour I compris entre 0 et 10A avec err_max=1e-2 T"""
    I, Err, B = np.linspace(0, 10, 501), [], []

    for i in I:
        b, err = point_fixe(i, 1e-2)
        B.append(b)
        Err.append(err)

    plt.figure()
    plt.plot(I, B, 'k')
    plt.xlabel("I (A)")
    plt.ylabel("B (T)")
    plt.title('Intensité du champ magnétique obtenue par point fixe')
    plt.grid()

    plt.figure()
    plt.semilogy(I, Err, 'k')
    plt.xlabel("I (A)")
    plt.ylabel("erreur estimée (T)")
    plt.title('Erreur du point fixe (100 itérations)')
    plt.grid()

    I, B = np.linspace(0, 10, 501), [0]
    DHDB = [dhdB(0, 0)]
    for i in I[1:]:
        B.append(seq(i, 1e-2, B=B[-1]))
        DHDB.append(dhdB(B[-1], i))

    plt.figure()
    plt.plot(I, DHDB, 'k')
    plt.plot([0, 10], [-1, -1], '--k')
    plt.text(5, -0.5, 'point fixe attractif', fontsize='large')
    plt.text(5, -2, 'point fixe répulsif', fontsize='large')
    plt.xlabel("I (A)")
    plt.ylabel("h'(Bf)")
    plt.title('Valeur de h(Bf)')
    plt.grid()
    plt.show()

    plt.show()


def point_fixe2(I, err_max, r=1, it_max=100, B=0):
    """ Q12 : Modifier la fonction précédente de manière à prendre en compte ce paramètre r, et étudier la convergence
    en fonction de I et de r."""
    err = err_max + 1
    it = 0
    while err > err_max and it < it_max:
        B = (1 - r) * B + r * N * I / (2 * np.pi * R) * mu(B)
        err = erreur(B, I)
        it += 1
    return B, err


def trace_pointfixe2():
    I = np.linspace(0, 10, 30)
    B1, Err1, B2, Err2 = [], [], [], []
    for i in I:
        b1, err1 = point_fixe2(i, 1e-2, r=0.1)
        b2, err2 = point_fixe2(i, 1e-2, r=1)
        B1.append(b1)
        B2.append(b2)
        Err1.append(err1)
        Err2.append(err2)

    plt.figure()
    plt.plot(I, B1, 'k', I, Err1, 'ok', I, B2, '--k', I, Err2, '*k')
    plt.xlabel("I (A)")
    plt.ylabel("(T)")
    plt.title('Intensité du champ magnétique obtenue par point fixe')
    plt.legend(["B (r = 0.1)", "erreur (r=0.1)", "B (r=1)", "erreur (r=1)"])
    plt.grid()
    plt.show()

    def dgdB(B, I, r):
        return 1 - r + r * dhdB(B, I)

    r = np.linspace(0.1, 1, 10)
    plt.figure()
    for R in r:
        I = np.linspace(0, 10, 30)
        Dgdb = [dgdB(0, 0, R)]
        B = [0]
        for i in I[1:]:
            B.append(seq(i, 1e-3, B=B[-1]))
            Dgdb.append(dgdB(B[-1], i, R))
        plt.plot(I, Dgdb, 'k')
    plt.plot([0, 10], [-1, -1], '--k', [0, 10], [1, 1], '--k')
    plt.xlabel("I (A)")
    plt.ylabel("g'(Bf)")
    plt.title("g'(Bf) pour r allant de 0.1 à 1")
    plt.grid()
    plt.show()


def newton(I, err_max, it_max=100, B=0):
    """ Q14 : Implémenter une fonction newton(I, err_max, it_max) permettant de trouver le champ magnétique B pour un
    courant I donné, avec une précision donnée par err_max dans la limite de it_max itérations."""
    err = err_max + 1
    it = 0
    while err > err_max and it < it_max:
        B = B - f(B, I) / dfdb(B)
        err = erreur(B, I)
        it += 1
    return B, err


def trace_newton():
    I = np.linspace(0, 10, 501)
    B = []
    Err = []
    for i in I:
        b, err = newton(i, 1e-2)
        B.append(b)
        Err.append(err)

    plt.figure()
    plt.semilogy(I, B, 'k', I, Err, '--k')
    plt.xlabel("I (A)")
    plt.ylabel("(T)")
    plt.legend(["B calculé", "erreur estimée"])
    plt.title('Intensité du champ magnétique obtenue par Newton')
    plt.grid()
    plt.show()


def newton2(I, err_max, r=1, it_max=100, B=0):
    """ Q15 : En s'inspirant des questions précédentes, proposer une amélioration de cette méthode afin de renforcer
    sa robustesse. Trouver une combinaison de paramètres permettant de tracer la courbe B(I) avec une erreur inférieure
    à 1e-2 T pour un courant I allant de 0 à 10A"""
    err = err_max + 1
    it = 0
    while err > err_max and it < it_max:
        B = B - r * f(B, I) / dfdb(B)
        err = erreur(B, I)
        it += 1
    return B, err


def trace_newton2():
    I = np.linspace(0, 10, 501)
    B = []
    Err = []
    for i in I:
        b, err = newton2(i, 1e-2, r=1, B=2)
        B.append(b)
        Err.append(err)

    plt.figure()
    plt.semilogy(I, B, 'k', I, Err, '--k')
    plt.xlabel("I (A)")
    plt.ylabel("B (T)")
    plt.title('Intensité du champ magnétique obtenue par Newton (r = 1, B0 = 2 T)')
    plt.legend(["B caclulé", "erreur estimée"])
    plt.grid()
    plt.show()

    I = np.linspace(0, 10, 501)
    B = []
    Err = []
    for i in I:
        b, err = newton2(i, 1e-2, r=0.05)
        B.append(b)
        Err.append(err)

    plt.figure()
    plt.semilogy(I, B, 'k', I, Err, '--k')
    plt.xlabel("I (A)")
    plt.ylabel("B (T)")
    plt.title('Intensité du champ magnétique obtenue par Newton (r = 0.05)')
    plt.grid()
    plt.show()

    B = []
    Err = []

    for i in I:
        b, err = newton2(i, 1e-2, r=0.3, B=2)
        B.append(b)
        Err.append(err)

    plt.figure()
    plt.plot(I, B, 'k', I, Err, '--k')
    plt.xlabel("I (A)")
    plt.ylabel("B (T)")
    plt.title('Intensité du champ magnétique obtenue par Newton (r = 0.3, B0 = 1T)')
    plt.grid()
    plt.show()


def compare():
    """ Q16 : Tracer le nombre d'itérations nécessaire à la résolution de l'équation 1 avec les quatre méthodes
    précédentes pour I compris entre 0 et 10A. Pour les méthodes de point fixe et de Newton, on fera aussi varier le
    coefficient r dans [0,1[, ainsi que le point d'initialisation."""

    def newton3(I, err_max, r=1, it_max=100, B=0):
        err = err_max + 1
        it = 0
        while err > err_max and it < it_max:
            B = B - r * f(B, I) / dfdb(B)
            err = erreur(B, I)
            it += 1
        return B, err, it

    def point_fixe3(I, err_max, r=1, it_max=100, B=0):
        err = err_max + 1
        it = 0
        while err > err_max and it < it_max:
            B = (1 - r) * B + r * N * I / (2 * np.pi * R) * mu(B)
            err = erreur(B, I)
            it += 1
        return B, err, it

    def dichot2(I, Binf, Bsup, err_max):
        it = 0
        while Bsup - Binf > err_max:
            it += 1
            Bmid = (Bsup + Binf) / 2
            if f(Binf, I) * f(Bmid, I) <= 0:
                Bsup = Bmid
            else:
                Binf = Bmid
        return Bmid, it

    def seq3(I, err_max):
        B = 0
        it = 0
        while f(B, I) * f(B + err_max, I) > 0:
            B += err_max
            it += 1
        return B, it

    I = np.linspace(0, 10, 30)

    it_seq = []
    it_dichot = []
    it_pf_r01 = []
    it_n_r005 = []
    it_n_r1_B02 = []

    for i in I:
        it_seq.append(seq3(i, 1e-3)[1])
        it_dichot.append(dichot2(i, 0, 2, 1e-3)[1])
        it_pf_r01.append(point_fixe3(i, 1e-3, r=0.1, it_max=500)[2])
        it_n_r005.append(newton3(i, 1e-3, r=0.05, it_max=500)[2])
        it_n_r1_B02.append(newton3(i, 1e-3, B=2, it_max=500)[2])

    plt.figure()
    plt.semilogy(I, it_seq, '-k', I, it_dichot, '--k', I, it_pf_r01, 'o-k', I, it_n_r005, '*-k', I, it_n_r1_B02, '+-k')
    plt.xlabel("I (A)")
    plt.ylabel("itérations")
    plt.title("Nombre d'itérations des différentes méthodes (erreur max = 1e-3)")
    plt.legend(["rech. sequentielle", "dichotomie", "point fixe (r=0.1)", "Newton (r=0.05)", "Newton (B0=2T)"])
    plt.grid()
    plt.show()

    errmax = np.logspace(-9, -1, 30)
    it_seq = []
    it_dichot = []
    it_pf_r01 = []
    it_n_r005 = []
    it_n_r1_B02 = []

    for err in errmax:
        if err >= 1e-6:
            it_seq.append(seq3(1, err)[1])
        it_dichot.append(dichot2(1, 0, 2, err)[1])
        it_pf_r01.append(point_fixe3(1, err, r=0.1, it_max=1000)[2])
        it_n_r005.append(newton3(1, err, r=0.05, it_max=1000)[2])
        it_n_r1_B02.append(newton3(1, err, B=2, it_max=1000)[2])

    plt.figure()
    plt.loglog(errmax[11:], it_seq, '-k', errmax, it_dichot, '--k', errmax, it_pf_r01, 'o-k', errmax, it_n_r005, '*-k',
               errmax, it_n_r1_B02, '+-k')
    plt.xlabel("Erreur maximale (T)")
    plt.ylabel("itérations")
    plt.title("Nombre d'itérations des différentes méthodes (I = 1A)")
    plt.legend(["rech. sequentielle", "dichotomie", "point fixe (r=0.1)", "Newton (r=0.05)", "Newton (B0=2T)"])
    plt.grid()
    plt.show()


if __name__ == '__main__':
    affiche_cycle_anhysteretique()
    affiche_f()
    trace_sequentiel()
    trace_dichotomie()
    trace_pointfixe()
    trace_pointfixe2()
    trace_newton()
    trace_newton2()
    compare()
