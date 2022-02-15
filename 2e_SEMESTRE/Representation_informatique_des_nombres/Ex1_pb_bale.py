# Problème de Bâle

###############################################################################
# 1)
 
import numpy as np

def somme_start2end32(N):
    somme = np.float32(0)
    for n in range(1, N+1):
        somme += np.float32(1/ n**2 )
    return somme

###############################################################################
# 2)

def somme_end2start32(N):
    somme = np.float32(0)
    for n in range(N, 0, -1):
        somme += np.float32(1 / n**2)
    return somme

###############################################################################
# 3)

import matplotlib.pyplot as plt
resultat_theorique = np.pi**2 / 6

# initialisation des listes
all_N = np.logspace(1, 6, 30).astype(int) # impose que N soit un entier
erreur_start2end32 = []
erreur_end2start32 = []

# calcul
for N in all_N:
    start2end32 = somme_start2end32(N)
    end2start32 = somme_end2start32(N)
    erreur_start2end32.append(abs(start2end32 - resultat_theorique))
    erreur_end2start32.append(abs(end2start32 - resultat_theorique))
    
# on trace start2end32 et end2start 32 en fonction de all_N en échelle logarithmique
plt.figure()
plt.loglog(all_N,erreur_start2end32,'k:',all_N,erreur_end2start32,'k--')
plt.legend(['erreur start2end','erreur end2start'])
plt.xlabel('nombre de termes') ; plt.ylabel('valeur de la somme')
plt.title('Erreur en fonction du nombre de termes (32 bits)')      
plt.grid() ; plt.show()

###############################################################################
# 4) 64 bits

def somme_start2end64(N):
    somme = 0
    for n in range(1, N+1):
        somme += 1 / n**2
    return somme

def somme_end2start64(N):
    somme = 0
    for n in range(N, 0, -1):
        somme += 1 / n**2
    return somme

# initialisation des listes
all_N=np.logspace(1, 7, 30).astype(int)
erreur_start2end64 = []
erreur_end2start64 = []

# calcul
for N in all_N:
    start2end64 = somme_start2end64(N)
    end2start64 = somme_end2start64(N)
    erreur_start2end64.append(abs(start2end64 - resultat_theorique))
    erreur_end2start64.append(abs(end2start64 - resultat_theorique))
    
# tracé
plt.figure()
plt.loglog(all_N,erreur_start2end64,'k:',all_N,erreur_end2start64,'k--')
plt.legend(['erreur start2end','erreur end2start'])
plt.xlabel('nombre de termes') ; plt.ylabel('valeur de la somme')
plt.title('Erreur en fonction du nombre de termes (64 bits)')      
plt.grid() ; plt.show()
