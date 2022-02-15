"""
    Cours : Boucles et itérations
    Exercice : Recherche de caractères dans un texte
"""

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# Q1 : Écrire un script permettant d'obtenir indices, une liste contenant les indices d'apparition d'un caractère c
# fixé dans une chaîne de caractères text.
c = "a"  # Caractère recherché
indices = []
for ind, caractere in enumerate(text):  # on parcourt text avec enumerate
    if caractere == c:
        indices.append(ind)  # on ajoute les indices d'apparition de c
print("il y a {0} occurrences de a".format(len(indices)))

# Q2 : Générer le dictionnaire carac. On veillera à ne considérer que les caractères de l'alphabet, sans prendre en
# compte la casse
carac = {}
for c in text:  # Pour chaque lettre
    if c in carac.keys():
        continue  # Si la lettre à déjà été comptée, on passe à la suivante
    if 97 <= ord(c) <= 122:  # Si le caractère est une lettre minuscule
        carac[c] = [i for i in range(len(text)) if text[i] == c]
print("il y a {0} caracteres distincts.".format(len(carac.keys())))

# Q3 : À l'aide du dictionnaire carac, déduire les 5 caractères les plus utilisés et leur fréquence d'apparition.
for k in range(5):
    # Cherche la lettre la plus fréquente
    mostFrequentCaracter = None
    maxOccurences = 0
    for c in carac.keys():
        if len(carac[c]) > maxOccurences:  # Si une lettre plus fréquente est trouvée...
            maxOccurences = len(carac[c])  # Mettre à jour les variables
            mostFrequentCaracter = c

    carac[mostFrequentCaracter] = []  # On élimine cette lettre, puis on recommence
    print(f"Le caractère {mostFrequentCaracter} apparait {maxOccurences} fois")
