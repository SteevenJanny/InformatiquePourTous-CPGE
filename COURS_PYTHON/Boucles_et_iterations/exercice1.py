"""
    Cours : Boucles et itérations
    Exercice : Nombres premiers et crible d'Eratosthène
"""

# Q1 : Déterminer à l'aide d'un programme les 20 nombres premiers les plus petits.
liste_premiers = []
nb_en_cours = 2
while len(liste_premiers) < 20:
    estPremier = True
    for i in range(2, nb_en_cours):  # on cherche si nb_en_cours possède un diviseur
        if nb_en_cours % i == 0:  # on en a trouvé un
            estPremier = False
            break
    if estPremier:  # variable restée vraie seulement si on n'a trouvé aucun diviseur
        liste_premiers.append(nb_en_cours)
    nb_en_cours += 1
print(liste_premiers)

# Q2 : En implémentant le crible d'Eratosthène, déterminer la liste premiers des nombres premiers inférieurs à 100.
N = 100
crible = [True for _ in range(N)]  # Liste de N fois True
crible[0], crible[1] = False, False  # 0 et 1 ne sont pas premiers
for i in range(N):
    if crible[i]:  # case pas cochée, donc c'est un nombre premier
        for j in range(2 * i, N, i):  # on supprime ses multiples suivants dans notre liste
            crible[j] = False
# Extraction des nombres premiers du crible
premiers = []
for i, p in enumerate(crible):
    if p is True:
        premiers.append(i)
print(premiers)

# Q3 : À partir de cette liste, écrire un code qui, à partir d'un entier N < 100, calcule la liste de ses facteurs 
# premiers, répétés autant de fois que nécessaire,  
N = 78
list_facteurs = []
residu = N
i = 0
while residu > 1:
    if residu % premiers[i] == 0:  # Si le nombre premier courant divise le résidu
        list_facteurs.append(premiers[i])  # Ajoute le nombre premier aux facteurs
        residu = residu / premiers[i]  # Divise par ce nombre pour obtenir le résidu

    else:  # N1 pas divisible par liste_prem[i], on passe au nombre premier suivant
        i += 1
print(list_facteurs)
