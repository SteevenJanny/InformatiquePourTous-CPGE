"""
    Cours : Fonction et commentaires
    Exercice : Espace de nommage
"""
# Q1 : Essayer d'appeler la fonction g dans le corps de votre programme (ligne 8) ou dans la console, que se passe t-il ?
# Essayer ensuite de l'appeler dans la fonction f, puis d'appeler f dans l'espace global. En déduire la position de g
# dans le diagramme.
x1 = "global"


def f():
    x2 = "enclosing"

    def g():
        x3 = "local"
        print(x3)

    g()  # Appel à la fonction g dans la fonction f


print("Appel à la fonction f")
f()
print("Appel à la fonction g")
# g()

# Q2 : Dans le corps du programme, essayer d'afficher x1, puis x2 et x3. Faire de même dans f puis dans g. En déduire
# la position des variables dans le diagramme.
x1 = "global"


def f():
    x2 = "enclosing"

    def g():
        x3 = "local"
        # Emplacement 1
        print("Dans g :")
        print("\tx1 : ", x1)
        print("\tx2 : ", x2)
        print("\tx3 : ", x3)

    g()  # Appel à la fonction g dans la fonction f
    # Emplacement 2
    # print("Dans f :")
    # print("\tx1 : ", x1); print("\tx2 : ", x2); print("\tx3 : ", x3)


f()
# Emplacement 3
# print("Dans global :")
# print("\tx1 : ", x1); print("\tx2 : ", x2); print("\tx3 : ", x3)
# Pour tester ce code, commentez et dé-commentez chaque emplacements à tour de rôles.

# Q3 : Renommer x1, x2 et x3 en x. Qu'affiche le programme ? Dans quel ordre Python cherche t-il une variable ?
x = "global"


def f():
    x = "enclosing"

    def g():
        x = "local"
        print("Dans g, x = ", x)

    g()  # Appel à la fonction g dans la fonction f
    print("Dans f, x = ", x)


f()
print("Dans global, x = ", x)
