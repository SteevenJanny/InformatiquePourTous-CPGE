# Bonus : résolution d'un labyrinthe par la résolution d'une équation de 
# diffusion par la méthode des éléments finis

###############################################################################
# 1) Importation d'une image de labyrinthe

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def im2lab(filename):
    img = mpimg.imread(filename)[:,:,1]
    img = img / np.max(img)
    img[img < 0.5] = 0
    img[img >= 0.5] = 1
    return img
    
# 0 : en dehors
# -1 : domaine
# 1 : contour

lab = im2lab("ex_labyrinthe.png")
plt.imshow(lab)
plt.title("Labyrinthe à résoudre")
plt.show()

###############################################################################
# 2) Génération maillage

# La méthode des éléments finis fait intervenir des intégrales, calculées sur
# de petits triangles qui forment un maillage. Les sommets de ces triangles
# représentent l'endroits où seront calculées les inconnues du problèmes ; en
# dehors le champ physique calculé est interpolé linéairement.

def maillage(lab):
    # renvoie un maillage des zones blanches d'un labyrinthe uniquement
    shape=lab.shape
    T=np.zeros(((shape[0]-1)*(shape[1]-1)*2,3),dtype='int') # table de connectivité
    XY=np.zeros((shape[0]*shape[1],2)) # coordonnées des noeuds
    kp = 0 ; kt = 0
    for j in range(0,shape[1]):
        for i in range(0,shape[0]):
            XY[kp,:] = [j,-i]
            if j<shape[1]-1 and i<shape[0]-1 and lab[i,j] and lab[i,j+1] and lab[i+1,j+1]:
                T[kt,:] = [kp,kp+shape[0],kp+shape[0]+1]
                kt += 1
            if j<shape[1]-1 and i<shape[0]-1 and lab[i,j] and lab[i+1,j] and lab[i+1,j+1]:
                T[kt,:] = [kp,kp+1,kp+shape[0]+1]
                kt += 1
            kp+=1
    T=T[1:kt,:]
    return XY, T

print("maillage en cours...")

noeuds, triangles = maillage(lab)


def trace_maillage(triangles,noeuds):
    # permet de tracer le maillage (à éviter car très long...)
    plt.figure()
    x=noeuds[triangles[:,[0,1,2,0]]-1,0]
    y=noeuds[triangles[:,[0,1,2,0]]-1,1]
    plt.plot(x.transpose(),y.transpose(),'k')
    plt.title('Maillage de référence')
    plt.show()

#trace_maillage(triangles,noeuds)

###############################################################################
# 3) Calcul analytique des intégrales 2D sur chaque triangle

def int_tri(X,Y):
    def produit(*args):
        A=args[0]
        for i in range(1,len(args)):
            A=np.dot(A,args[i])
        return A

    detJ = (X[0]-X[2])*(Y[1]-Y[2])-(X[1]-X[2])*(Y[0]-Y[2])
    invJ = 1/detJ*np.array([[Y[1]-Y[2],-Y[0]+Y[2]],[-X[1]+X[2], X[0]-X[2]]])
    G = np.array([[1,0,-1],[0,1,-1]])
    return produit(np.abs(detJ), G.transpose(), invJ.transpose(), invJ, G) / 2

###############################################################################
# 4) Assemblage de la matrice du système éléments finis
print("assemblage en cours...")

from scipy.sparse import coo_matrix

def assemblage(noeuds, triangles):
    Nt=len(triangles)
    Nn=len(noeuds)
    I=np.zeros(6*Nt); J=np.zeros(6*Nt) ; val=np.zeros(6*Nt) ;
    for i in range(Nt):
        noeuds_triangle = triangles[i,:]
        X = noeuds[noeuds_triangle,0]
        Y = noeuds[noeuds_triangle,1]
        Kel = int_tri(X,Y)
        I[6*i:6*i+6] = noeuds_triangle[[0,1,2,1,2,2]]
        J[6*i:6*i+6] = noeuds_triangle[[0,0,0,1,1,2]]
        val[6*i:6*i+6] = np.array([Kel[0,0]/2,Kel[0,1],Kel[0,2],Kel[1,1]/2,Kel[1,2],Kel[2,2]/2])
    # on génère une matrice creuse dans laquelle seul les termes non nuls sont 
    # stockés en mémoire :
    K = coo_matrix((val,(I,J)), shape = (Nn,Nn))
    K = K + K.transpose()
    return K

K = assemblage(noeuds, triangles)
plt.figure()
plt.spy(K, markersize = 3)
plt.title("Termes non nuls de la matrice éléments finis")
plt.show()

###############################################################################
# 5) Détection de l'entrée et de la sortie

print("Application des conditions limites...")

def detect_inout(mat):
    # détecte l'entrée et la sortie
    shape = mat.shape
    IN = []; OUT = []
    test1 = False; test2 = False; test3 = False; test4 = False
    
    # détection de l'entrée
    for i in range(0, shape[0]):
        if mat[i, 0] == 1:
            IN.append(i)
            test1 = True
    if not test1:
        for i in range(0, shape[0]):
            if mat[i, shape[1]-1] == 1:
                IN.append(i+shape[0]*(shape[1]-1))
                test2 = True 
    if not test1 and not test2:
        for i in range(0, shape[1]):
            if mat[0, i] == 1:
                IN.append(i*shape[0])
                test3 = True
                
# On a forcément un de ces test qui est bon
    for i in range(0, shape[1]):
        if mat[shape[0]-1, i] == 1:
            OUT.append(i*shape[0]-1)
            test4 = True
    
    if not test4 and not test3:
       for i in range(0, shape[1]):
            if mat[0, i] == 1:
                OUT.append(i*shape[0])
                test3 = True
    
    if not test4 and not test2:
        for i in range(0,shape[0]):
            if mat[i, shape[1]-1] == 1:
                OUT.append(i+shape[0]*(shape[1]-1))
                test2 = True
    return IN, OUT

IN,OUT = detect_inout(lab)

###############################################################################
# 6) Expression des conditions limites de Dirichlet à l'entrée et à la sortie

def Dirichlet_CL(triangles,noeuds,IN,OUT):
    noeuds_utiles = np.unique(triangles)
    noeuds_inutile = np.arange(0,len(noeuds))[np.in1d(np.arange(0,len(noeuds)),noeuds_utiles,invert=True)]
    Nn = len(noeuds)
    I = [];  J = []; valC = [] ; valB = [] ; k = 0
    
    for noeud in noeuds_inutile:
        I += [k]
        J += [noeud]
        valC += [1]
        valB += [0]
        k += 1
    
    for noeud in IN:
        I += [k]
        J += [noeud]
        valC += [1]
        valB += [1e5]
        k += 1
        
    for noeud in OUT:
        I += [k]
        J += [noeud]
        valC += [1]
        valB += [-1e5]
        k += 1
    
    C = coo_matrix((valC,(I,J)),shape=(k,Nn))
    b = coo_matrix((valB,(I,np.zeros(k))),shape=(k,1))
    
    return C,b

C,b = Dirichlet_CL(triangles,noeuds,IN,OUT)


###############################################################################
# 7) Imposition des conditions limites par pénalisation


def imposeCL(K, C, b, coeff = 1e5):
    coeff = np.max(np.abs(K))*coeff
    Kp = K + coeff * (C.transpose() * C)
    bp = coeff * (C.transpose() * b)
    return Kp, bp

Kp, bp = imposeCL(K, C, b)

###############################################################################
# 8) Résolution du système

print("Résolution du systèmes en cours...")

from scipy.sparse.linalg import spsolve
T = spsolve(Kp,bp)

###############################################################################
# 9) Affichage du champ physique

print("Affichage...")

def affiche_T(T,lab):
    # affiche directement la solution (température par exemple)
    k = 0
    shape = lab.shape
    maxT = np.max(np.abs(T))
    lab1 = lab.copy()
    for j in range(shape[1]):
        for i in range(shape[0]):
            lab1[i,j] = T[k]/maxT * 1e5
            k += 1
    plt.figure()
    plt.imshow(lab1)
    plt.title("Pseudo-température finale")
    plt.show()

affiche_T(T,lab)


###############################################################################
# 9) Affichage de la norme du flux (donne le chemin du labyrinthe)

def grad(X,Y,val):
    # calcule le gradient de température pour un triangle
    G = np.array([[1,0,-1],[0,1,-1]])
    detJ=(X[0]-X[2])*(Y[1]-Y[2])-(X[1]-X[2])*(Y[0]-Y[2])
    invJ=1/detJ*np.array([[Y[1]-Y[2],-Y[0]+Y[2]],[-X[1]+X[2], X[0]-X[2]]])
    return np.dot(np.dot(invJ,G),val)

def affiche_flux(T,noeuds,triangles):
    # affiche le gradient de température (solution du labyrinthe)
    Nt=len(triangles)
    X=np.zeros(Nt); Y=np.zeros(Nt) ; val=np.zeros(Nt) ;
    flux = np.zeros((Nt,2))
    plt.figure()
    
    for i in range(Nt):
        noeuds_triangle = triangles[i,:]
        X[i] = np.mean(noeuds[noeuds_triangle,0])
        Y[i] = np.mean(noeuds[noeuds_triangle,1])
        flux[i,:]=-grad(noeuds[noeuds_triangle,0],noeuds[noeuds_triangle,1],T[noeuds_triangle]).T
        val[i] = np.linalg.norm(flux[i,:])
    plt.tripcolor(noeuds[:,0], noeuds[:,1], triangles, facecolors=val)
    #plt.quiver(X,Y,flux[:,0],flux[:,1],angles='xy',scale=5e3) # affiche la direction du flux (moche...)
    plt.title("Solution du labyrinthe")
    plt.show()
    

affiche_flux(T,noeuds,triangles) 
