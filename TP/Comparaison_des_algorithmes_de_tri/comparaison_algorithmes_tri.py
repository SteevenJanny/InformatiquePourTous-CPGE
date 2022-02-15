"""
    TP : Comparaison des algorithmes de tri
"""
import matplotlib.pyplot as plt
import random as rd
from numpy import logspace


def plot_liste(L):
    """ Q1 : Ecrire une fonction plot_list(l) qui, à partir d'une liste l contenant des nombres, affiche son contenu
    dans un graphique en bâtons"""
    plt.bar(list(range(0, len(L))), L)


def plot_anim(L, delai=0.001, tri=''):
    """ Q2 : Ecrire une fonction plot_anim(L) qui, à partir d'une liste L qui contient des listes l de nombres, affiche
    chaque liste l successivement de manière à créer une animation."""
    for i in range(0, len(L)):
        plt.clf()  # efface la figure précédente de la mémoire et évite des ralentissements
        plot_liste(L[i])
        plt.title(tri + " - itération " + str(i + 1))
        plt.pause(delai)  # contrôle la vitesse de défilement des images


def tri_bulles(T):
    """ Q4 : Coder une fonction tri_bulles(T) qui, à partir d'une liste de nombres T, renvoie l'ensemble des listes à
    chaque étape du processus de tri à bulles. Afficher ensuite son fonctionnement pour une liste T de 20 valeurs
    aléatoires."""
    T_history = [T]
    for i in range(len(T) - 1, 0, -1):
        for j in range(0, i):
            if T[j + 1] < T[j]:
                T[j], T[j + 1] = T[j + 1], T[j]
                T_history.append(T.copy())
    return T_history


def tri_insertion(T):
    """ Q5 : Coder une fonction tri_insertion(T) qui, à partir d'une liste de nombres T, renvoie l'ensemble des listes
    à chaque étape du processus de tri par insertion. Afficher ensuite son fonctionnement pour une liste T de 20 valeurs
     aléatoires."""
    T_history = [T]
    for i in range(1, len(T)):
        t = T[i]
        j = i
        while j > 0 and T[j - 1] > t:
            T[j] = T[j - 1]
            T_history.append(T.copy())
            j = j - 1
        T[j] = t
    return T_history


def tri_selection(T):
    """ Q6 : Faire de même pour le tri par sélection en codant la fonction tri_selection(T). Que remarque-t'on par
    rapport aux deux algorithmes précédents ? Expliquer."""
    N = len(T)
    T_history = [T]
    for i in range(0, N - 1):
        jmin = i
        for j in range(i + 1, N):
            if T[j] < T[jmin]:
                jmin = j
        T[jmin], T[i] = T[i], T[jmin]
        T_history.append(T.copy())
    return T_history


# Attention : il faut modifier le tableau entier à chaque étape pour avoir un
# tri en place et retourner explicitement les étapes intermédiaires
def fusion(T, ind_bas, ind_mid, ind_haut, Thist):
    """ Q7.1 : Ecrire une fonction fusion(T,ind_bas,ind_mid,ind_haut) qui prend une liste globale T et trois indices
    ind_bas (indice du premier élément du sous-tableau 1 de T), ind_mid (indice du premier élément du sous-tableau 2
    de T), ind_haut (indice du dernier élément du sous-tableau 2 de T), et renvoie le tableau T dans lequel l'opération
    de fusion (définie dans le cours) a été effectuée sur les sous-tableaux 1 et 2."""
    if ind_mid <= ind_bas:  # si len(T1) == 0 ...
        return T, Thist
    elif ind_mid > ind_haut:  # si len(T2) == 0 ...
        return T, Thist
    elif T[ind_bas] <= T[
        ind_mid]:  # on ne modifie pas le tableau ; T1[0] est à la bonne place et on ne le considère plus. On incrémente donc ind_bas pour la prochaine fusion
        return fusion(T, ind_bas + 1, ind_mid, ind_haut, Thist)
    else:  # on modifie le tableau (échange de T1[0] et T2[0]), puis on décale en incrémentant ind_bas et ind_mid
        T[ind_bas], T[ind_bas + 1:ind_mid + 1] = T[ind_mid], T[ind_bas:ind_mid]
        Thist.append(T.copy())  # ne pas oublier le .copy()
        return fusion(T, ind_bas + 1, ind_mid + 1, ind_haut, Thist)


def tri_fusion(T, ind_bas, ind_haut, Thist):
    """ Q7.3 : Ecrire une fonction tri_fusion(T,ind_bas,ind_haut,Thist) qui prend en entrée une liste T, deux indices
    ind_bas, ind_haut, ainsi que la liste des tableaux aux précédentes étapes de tri Thist, et renvoie le tableau T et
    l'historique Thist mis à jour. Afficher ensuite les différentes étapes du tri fusion pour une liste de 40 éléments
    aléatoires."""
    if ind_bas < ind_haut:
        ind_mid = ind_bas + int((ind_haut - ind_bas) / 2) + 1
        # ind_bas = 1er indice de T1 ; ind_mid-1 = dernier indice de T1, donc :
        T, Thist = tri_fusion(T, ind_bas, ind_mid - 1, Thist)
        # ind_mid = 1er indice de T2 ; ind_haut = dernier indice de T2, donc :
        T, Thist = tri_fusion(T, ind_mid, ind_haut, Thist)
        T, Thist = fusion(T, ind_bas, ind_mid, ind_haut, Thist)
    return T, Thist


def choix_pivot(ind_bas, ind_haut, choix="random"):
    """ Q8.1 : Coder une fonction choix_pivot(ind_bas,ind_haut) qui renvoie l'indice du pivot, compris entre ind_bas
    et ind_haut."""
    if choix == "random":
        return rd.randint(ind_bas, ind_bas)
    elif choix == "last":
        return ind_haut
    elif choix == "first":
        return ind_bas


def partition(T, ind_bas, ind_pivot, ind_haut, Thist):
    """ Q8.2 : Coder une fonction partition(T,ind_bas,ind_pivot,ind_haut,Thist) qui renvoie le tableau T dont le
    sous-tableau compris entre les indices ind_bas et ind_haut a été partitionné selon le pivot d'indice ind_pivot.
    Cela signifie qu'il faut renvoyer le tableau T modifié, ainsi que les indices de début et/ou de fin des
    sous-tableaux T_g, val_p et T_d du cours sur le tri rapide. Elle renverra aussi l'historique des tableaux des étapes
    intérmédiaires Thist mis à jour."""
    val_pivot = T[ind_pivot]
    k = ind_bas
    ind_endTg = ind_bas - 1  # indice de fin de Tg
    ind_begTd = ind_haut + 1  # indice de début de Td
    for i in range(ind_bas, ind_haut + 1):
        if T[k] < val_pivot:
            T[ind_bas], T[ind_bas + 1:k + 1] = T[k], T[ind_bas:k]
            Thist.append(T.copy())
            k += 1
            ind_endTg += 1
        elif T[k] > val_pivot:
            T[ind_haut], T[k:ind_haut] = T[k], T[k + 1:ind_haut + 1]
            Thist.append(T.copy())
            ind_begTd -= 1
        else:
            k += 1
    return T, ind_endTg, ind_begTd, Thist


def tri_rapide(T, ind_bas, ind_haut, Thist):
    """ Q8.3 : Ecrire une fonction tri_rapide(T,ind_bas,ind_haut,Thist) qui renvoie le tableau T dont le sous tableau
    entre ind_bas et ind_haut est trié, ainsi que l'historique de T lors des étapes intermédiaires Thist."""
    if ind_haut > ind_bas:
        ind_pivot = choix_pivot(ind_bas, ind_haut)
        T, ind_less, ind_more, Thist = partition(T, ind_bas, ind_pivot, ind_haut, Thist)
        T, Thist = tri_rapide(T, ind_bas, ind_less, Thist)
        T, Thist = tri_rapide(T, ind_more, ind_haut, Thist)
    return T, Thist


def tri_comptage(T):
    """ Q9.1 : Ecrire une fonction tri_comptage(T) qui renvoie le tableau T trié ainsi que l'historique de construction
    de la table de comptage Tcompt à partir d'une liste d'entiers positifs T. Le premier élément de Tcompt est une liste
    dont la taille vaut la valeur maximale de T comportant uniquement des zéros, et les éléments suivants sont les mises
    à jour de cette table de comptage au fur et à mesure du parcours de T."""
    maxT = max(T)
    Tcompt = [[0 for i in range(0, maxT + 1)]]
    for i in range(0, len(T)):
        t = Tcompt[-1].copy()
        t[T[i]] += 1
        Tcompt.append(t)
    k = 0
    for i in range(maxT + 1):
        for _ in range(Tcompt[-1][i]):
            T[k] = i
            k += 1
    return T, Tcompt


# 9-2)

def plot_tri_comptage(Tcompt, T, delai=0.1):
    """ Q9.2 : Ecrire une fonction plot_tri_comptage(Tcompt,T) qui, à partir de l'historique de construction de la table
    de comptage Tcompt, affiche simultanément sa construction ainsi que l'élément de T considéré. """
    N = len(T)
    maxT = max(T)
    for i in range(0, N + 1):
        plt.clf()
        plt.subplot(2, 1, 1)
        plt.title(f"Génération de la table de comptage - it n {i}")
        couleur_liste = ['b' for _ in range(0, N)]
        if i >= 1:
            couleur_liste[i - 1] = 'r'  # permet d'afficher en rouge l'élément courant
        plt.bar(range(0, N), T, color=couleur_liste)
        plt.subplot(2, 1, 2)
        plt.bar(range(0, maxT + 1), Tcompt[i])
        plt.pause(delai)


if __name__ == '__main__':
    # Q3 : Tester vos fonctions avec des listes simples et de taille modérée.
    L = [[1, 2, 3], [2, 1, 3], [2, 3, 1], [3, 2, 1]]
    plot_anim(L, delai=1, tri="test")

    # Q4 : Tri à bulles
    N = 20
    L = [rd.randint(0, N) for i in range(0, N)]
    plot_anim(tri_bulles(L), tri="tri à bulles")

    # Q5 : Tri par insertion
    N = 20
    L = [rd.randint(0, N) for i in range(0, N)]
    plot_anim(tri_insertion(L), tri="tri par insertion")

    # Q6 : Tri par selection
    N = 20
    L = [rd.randint(0, N) for i in range(0, N)]
    plot_anim(tri_selection(L), tri="tri par sélection")

    # Q7.3 : Tri fusion
    N = 40
    L = [rd.randint(0, N) for i in range(0, N)]
    plot_anim(tri_fusion(L, 0, N - 1, [L])[1], tri='tri fusion')

    # Q8.3 : Tri rapide
    N = 40
    L = [rd.randint(0, N) for i in range(0, N)]
    plot_anim(tri_rapide(L, 0, N - 1, [L])[1], tri='tri rapide')

    # Q9.2 : Tri comptage
    N = 40
    L = [rd.randint(0, N) for i in range(0, N)]
    T, table_comptage = tri_comptage(L.copy())
    plot_tri_comptage(table_comptage, L)

    # Q10 Comparaisons

    N = logspace(0.3, 3, 15).astype(int)
    Nbulles = []
    Ninsert = []
    Nselect = []
    Nfusion = []
    Nrapide = []
    Ncomptage = []
    for n in N:
        T = [rd.randint(0, n) for i in range(0, n)]
        Nbulles.append(len(tri_bulles(T.copy())))
        Ninsert.append(len(tri_insertion(T.copy())))
        Nselect.append(len(tri_selection(T.copy())))
        Nfusion.append(len(tri_fusion(T.copy(), 0, n - 1, [T.copy()])[1]))
        Nrapide.append(len(tri_rapide(T.copy(), 0, n - 1, [T.copy()])[1]))
        Ncomptage.append(len(tri_comptage(T.copy())[1]))
        print(n)

    plt.figure()
    plt.loglog(N, Nbulles, 'o-k', N, Ninsert, '^-k', N, Nselect, 's-k', N, Nfusion,
               'x-k', N, Nrapide, '+-k', N, Ncomptage, '*k-')
    plt.title("Nombre d'étapes de chaque algorithme de tri")
    plt.xlabel("Taille de la liste")
    plt.ylabel("Nombre d'étapes")
    plt.legend(["bulles", "insertion", "selection", "fusion", "rapide", "comptage"])
    plt.grid()
    plt.show()
