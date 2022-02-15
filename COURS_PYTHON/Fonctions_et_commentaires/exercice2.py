"""
    Cours : Fonction et commentaires
    Exercice : Le piège des listes
"""


# Q1 : Coder une fonction f(x) qui ajoute 3 à l'entrée x et renvoie cette nouvelle valeur. Tester votre code avec x=3 et
# x2=f(x). Que vaut x après l'appel à f ?
def f(x: int):
    """ Ajoute 3 à x """
    x = x + 3
    print(id(x))
    return x


x = 3
print(id(x))
x2 = f(x)
print(x, x2)


# Q2 : Coder une fonction g(liste) qui remplace la première valeur de liste par le chiffre 3, et la renvoie. Tester avec
# liste2 = g(liste). Que vaut liste après l'appel à g ?
def g(liste):
    liste2 = liste  # Copie la liste
    liste2[0] = 3  # Change le premier terme
    print("ID dans g : ", id(liste2))
    return liste2


liste = [1, 2, 3]
print("ID dans Global : ", id(liste))
liste2 = g(liste)
print(liste)

# Q3 : Selon vous, que doit afficher ce code ? Vérifier.
x = [1, 2]
liste = [x, x]
x[0] = 2
print(liste, x)


# Q4 : Selon vous, que doit afficher ce code ? Vérifier.
def f(liste=[]):
    liste.append("foo")
    print(liste)


f()
f()
