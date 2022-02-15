"""
    TP : Déchiffrer un message avec la méthode de Metropolis
"""

from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
import random

message = "J BLME HMZ MTJNHZ PJ CJODM HX ONLCLWXM MZC JLZMM EYXZ EM NLZWXYEZ IJZ TNJEH ODYZMZ MC IYXNCJEC EYXZ " \
          "GYXLZZYEZ H XEM IYZLCLYE HM ZXIMNLYNLCM IJN NJIIYNC J OMXA WXL ZM ZYXFMCCMEC JUMO PMXN CNJUJLP J EYCNM " \
          "GXTMFMEC EYXZ EYXZ MIJEYXLZZYEZ HJEZ PJ ONLCLWXM EMTJCLUM IPJLZJECM J MONLNM MC J PLNM FJLZ P JFMNM " \
          "UMNLCM WX LP EYXZ VJXC BLME NMTJNHMN ME VJOM O MZC WXM HJEZ PM TNJEH YNHNM HMZ ODYZMZ PM FMCZ PM IPXZ " \
          "FMHLYONM J ZJEZ HYXCM IPXZ HM UJPMXN WXM PJ ONLCLWXM WXL PM HMEYEOM OYFFM CMP"

with open("swann.txt") as file:
    corpus = file.read()


def chr2id(c):
    """ Q1 : Coder une fonction chr2id(c) qui encode le caractère c en un entier correspondant à sa position dans
    l'alphabet. Si c est un espace, on renverra zéro. Coder la fonction inverse id2chr(i) """
    return 0 if c == " " else ord(c) - 64


def id2chr(i):
    return " " if i == 0 else chr(i + 64)


def encode(message):
    """ Q2 : Coder les fonctions encode(message) et decode(message) qui réalisent l'encodage et le décodage d'une chaîne
     de caractère message. On stockera le code de chaque caractère dans une liste. """
    return [chr2id(c) for c in message]


def decode(message):
    return "".join([id2chr(c) for c in message])


def genererCode():
    """ Q3 : Coder une fonction genererCode() qui renvoie un code de substitution aléatoire sous la forme ci-dessus. """
    alphabet = list(range(1, 27))  # Liste contenant l'alphabet
    shuffle(alphabet)  # Mélange l'alphabet (opération en place)
    code = [0, ] + alphabet  # On respecte f(0)=0
    return code


def cipher(message, f):
    """ Q4 : A l'aide des fonctions précédentes, implémenter une fonction cipher(message, f) qui encode la chaîne message,
     le chiffre avec la clé de chiffrement f, puis le décode. """
    message_encode = encode(message)  # On commence par encoder le message
    message_cipher = []  # Pour stocker le message codé
    for c in message_encode:
        i = f[c]  # Chiffre le caractère
        message_cipher.append(i)  # On ajoute au message chiffré
    message_cipher = decode(message_cipher)
    return message_cipher


def decipher(message, f):
    """ Q5 : De même, coder la fonction \texttt{decipher(message, f)}. """
    message = encode(message)
    message_decipher = []
    for c in message:
        i = f.index(c)  # On cherche la position de la lettre dans le code
        message_decipher.append(i)  # Ajoute au message déchiffré
    message_decipher = decode(message_decipher)
    return message_decipher


def compteMonogramme(corpus):
    """ Q6 : Coder une fonction compteMonogramme(corpus) qui renvoie la fréquence d'apparition de chaque lettre dans la
    chaîne de caractères corpus sous forme de liste. Autrement dit, la k^e valeur de la liste contient la fréquence
    d'apparition de la $k^e$ lettre de l'alphabet. Afficher les fréquences dans un diagramme en bâton."""
    stat = np.zeros(27)  # Liste contenant les fréquences des lettres
    corpus = encode(corpus)  # Convertie le corpus en liste de nombres
    for i in range(27):
        stat[i] += corpus.count(i)  # Compte le nombre d'occurence de la lettre encodée i
    stat = stat[1:]  # Retire l'espace de la liste
    return stat / sum(stat)  # Normalisation par le nombre de lettre dans le corpus.


def sortAlphabet(frequence):
    """ Q7 : Coder une fonction sortAlphabet(frequence) qui, à partir des fréquences, renvoie une liste de lettres
    triées de la plus fréquente à la moins fréquente. On pourra représenter les lettres par leurs indices dans
    l'alphabet"""
    indices = list(range(len(frequence)))  # Une liste d'indices qui sera triée en même temps que frequence
    for i in range(len(frequence)):
        for j in range(0, len(frequence) - i - 1):
            if frequence[j] < frequence[j + 1]:  # échange si l'élement est plus grand que le suivant
                frequence[j], frequence[j + 1] = frequence[j + 1], frequence[j]
                indices[j], indices[j + 1] = indices[j + 1], indices[j]  # Même procédure sur les indices
    return indices


def trouveCode(alphabet_corpus, alphabet_message):
    """ Q8 : Compléter le code ci-dessous pour calculer la clé de chiffrement correspondante à l'analyse des
    fréquences"""
    # Calcul des fréquences
    code = [0 for k in range(26)]
    for k in range(26):
        code[alphabet_corpus[k]] = alphabet_message[k] + 1  # Le +1 permet de prendre en compte l'espace dans l'encodage
    code = [0, ] + code  # Ajout de l'espace
    return code


def compteBigramme(corpus):
    """ Q10 : Coder une fonction compteBigramme(corpus) qui calcule et renvoie M sur le corpus. """
    M = np.zeros((27, 27))  # Matrice de transition
    corpus = encode(corpus)  # Encodage du corpus en liste d'entiers
    c1 = 0  # On commence par un espace (arbitrairement)
    for c2 in corpus:  # Pour chaque lettre du corpus
        M[c1, c2] += 1  # On incrémente la case de M correspondante
        c1 = c2  # La lettre 2 devient la lettre 1, et on recommence.
    return M / sum(M)


def permuteCode(code, i, j):
    """ Q12 : Coder une fonction permuteCode(code, i, j) qui inverse les cases i et j de la liste code,
    puis la renvoie. """
    newcode = code.copy()
    newcode[j] = code[i]
    newcode[i] = code[j]
    return newcode


def V(m, M):
    """ Q13 : Coder une fonction V(m, M) qui renvoie la plausibilité du message m selon la matrice de transition M."""
    m = encode(m)
    plausible = 0
    c1 = 0
    for c2 in m:
        plausible += np.log(M[c1, c2] + 1e-6)
        c1 = c2
    return plausible / len(m)


def metropolis(m, M, MAX_ITER=10000, THRESH=-2.166):
    """ Q14 : Implémenter la méthode de Metropolis, afin de déchiffrer le message. On pourra effectuer "à la main"
    les dernières substitutions."""
    current_code = genererCode()
    current_trad = decipher(m, current_code)
    current_score = V(current_trad, M)
    best_code, best_trad, best_score = current_code.copy(), current_trad, current_score
    n_iter = 0

    while n_iter < MAX_ITER and best_score < THRESH:
        i, j = random.choices(range(1, 27), k=2)
        new_code = permuteCode(current_code, i, j)  # Essaie nouvelle permutation
        new_trad = decipher(m, new_code)
        new_score = V(new_trad, M)
        if new_score > best_score:  # On accepte le nouveau code si le score est meilleur
            current_code, current_trad, current_score = new_code.copy(), new_trad, new_score
            best_code, best_trad, best_score = new_code.copy(), new_trad, new_score
            # print("# ", n_iter, " L=", round(new_score, 3), " => ", best_trad[:48])  # Affiche la solution
        elif random.random() < np.exp((new_score - current_score) * len(m)):
            # Sinon, on accepte avec une certaine probabilité
            current_code, current_trad, current_score = new_code.copy(), new_trad, new_score
        n_iter += 1
    return best_trad


if __name__ == '__main__':
    # Section 1
    message_test = "LABOR OMNIA VINCIT IMPROBUS"
    cle = genererCode()
    message_chiffre = cipher(message_test, cle)
    message_dechifre = decipher(message_chiffre, cle)

    print("Démo Section 1")
    print("\tMessage clair : ", message_test)
    print("\tClé de chiffrement : ", cle)
    print("\tMessage chiffré : ", message_chiffre)
    print("\tMessage déchiffré : ", message_dechifre)

    # Section 2
    print("\nDémo section 2")
    frequence = compteMonogramme(corpus)
    stat = compteMonogramme(corpus)

    frequence_message = compteMonogramme(message)
    frequence_corpus = compteMonogramme(corpus)
    alphabet_corpus = sortAlphabet(frequence_corpus)
    alphabet_message = sortAlphabet(frequence_message)
    code = trouveCode(alphabet_corpus, alphabet_message)
    message_decipher = decipher(message, code)
    print("\tLettres les plus fréquentes en français : ", decode(np.array(alphabet_corpus) + 1))
    print("\tMessage déchiffré avec AdF : ", message_decipher[:49], "...")

    # Section 3
    print("\nDémo Section 3")
    M = compteBigramme(corpus)
    message_dechifre = metropolis(message, M)
    print("\tMessage déchiffré : ", message_dechifre)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))  # Figure séparée en 2 colonnes
    alphabet = [" "] + [chr(k) for k in range(65, 65 + 26)]  # Liste de lettre pour l'axe des abscisse

    ax[0].bar(np.arange(26), stat)
    ax[0].set_title("Fréquence des monogrammes")
    ax[0].set_xticks(np.arange(26))
    ax[0].set_xticklabels(alphabet[1:])  # Affiche l'alphabet sur l'axe des abscisse

    ax[1].imshow(M)
    ax[1].set_xticks(np.arange(27))
    ax[1].set_xticklabels(alphabet)
    ax[1].set_yticks(np.arange(27))
    ax[1].set_yticklabels(alphabet)
    ax[1].set_xlabel("Deuxieme lettre")
    ax[1].set_ylabel("Premiere lettre")
    ax[1].set_title("Fréquences des bigrammes")

    plt.tight_layout()
    plt.show()
