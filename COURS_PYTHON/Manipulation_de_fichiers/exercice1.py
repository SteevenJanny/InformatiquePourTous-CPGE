"""
    Cours : Manipulation de fichiers
    Exercice : Analyse de textes
"""

with open("fleurdumal.txt", 'r') as fichier:
    contenu = fichier.read()  # Lis le fichier
    contenu = contenu.lower()  # Retire les majuscules


def estUnMot(mot):
    """ Q2 : A l'aide de la table ASCII, coder une fonction qui renvoie True si tous les caractères d'un mot passé en
    entrée sont des lettres minuscules (sans accent) et False sinon. Traiter également le cas où le mot est une chaîne
    vide."""
    if mot == "":
        return False  # Si le mot est vide, on renvoie False

    for lettre in mot:  # On parcourt le mot lettre par lettre
        if not 97 <= ord(lettre) <= 122:  # Si la lettre n'est pas dans a...z
            return False
    return True


def liste_des_mots(contenu):
    """ Q3 : Coder une fonction qui renvoie la liste des mots (sans les éventuels symboles!) d'une phrase écrite en
    minuscule passée en entrée. Remarquez qu'un mot est (très souvent) délimité par deux espaces."""
    liste_raw = contenu.split(" ")
    liste_mots = []
    for mot in liste_raw:  # Pour tous les mots candidats
        if estUnMot(mot):  # Si ce mot est valide (i.e. pas un symbole)
            liste_mots.append(mot)  # ajoute à la liste des mots
    return liste_mots


def compteMots(liste_mots):
    """ Q4 : Coder une fonction qui, pour une liste de mots, renvoie un dictionnaire associant à chaque mot unique son
    nombre d'occurrences dans la liste."""
    compteur_mots = {}
    for mot in liste_mots:  # On passe sur chaque mot
        if mot in compteur_mots.keys():  # Si on a déjà rencontré ce mot:
            compteur_mots[mot] += 1
        else:  # Si ce mot est nouveau
            compteur_mots[mot] = 1
    return compteur_mots


def trouveMotsFrequents(frequence_mots, longueur_min=5, N=10):
    """ Q5 : Finalement, coder une fonction qui renvoie les N mots les plus fréquents dont la longueur est supérieure
    à un certain seuil"""
    # On commence par retirer les mots trop courts
    mots_long = []
    for mot in frequence_mots.keys():  # Pour chaque mot
        if len(mot) >= longueur_min:  # si le mot est suffisamment long
            mots_long.append(mot)  # On l'ajoute à la liste

    # Ensuite on trie cette liste
    def valeur(x):
        return frequence_mots[x]

    mots_tries = sorted(mots_long, key=valeur, reverse=True)
    return mots_tries[:N]


if __name__ == '__main__':
    # Extraction liste de mots
    liste_mots = liste_des_mots(contenu)
    # Compte les mots
    frequence_mots = compteMots(liste_mots)
    # Trouve les plus fréquents
    mots_frequents = trouveMotsFrequents(frequence_mots)
    print(mots_frequents)
