# Une suite constante... en théorie
###############################################################################
# 1)

# pas de code nécessaire

###############################################################################
# 2)

def suite(N):
    u = 0.3
    for n in range(0, N):
        u = 11*u - 3
    return u

###############################################################################
# 3) tracé

import matplotlib.pyplot as plt

N_all = []
termes_suite = []

for n in range(1, 21):
    N_all.append(n)
    termes_suite.append(suite(n))
    print(f'suite({n}) = {suite(n)}')
        
plt.plot(N_all, termes_suite, 'k')
plt.xlabel('n') ; plt.ylabel('suite(n)')
plt.title('Valeurs calculées de la suite')
plt.grid() ; plt.show()

###############################################################################
# 4) 32 bits

import numpy as np

def suite32(N):
    u = np.float32(0.3)
    for n in range(0, N):
        u = np.float32(11*u - 3)
    return u

termes_suite32=[]

for n in range(1,21):
    termes_suite32.append(suite32(n))
    print(f'suite32({n})={suite32(n)}')

# tracé :
    
plt.figure()
plt.semilogy(N_all,np.abs(termes_suite),'k',N_all,np.abs(termes_suite32),'k:')
plt.legend(['64 bit','32 bits'])
plt.xlabel('n') ; plt.ylabel('|suite(n)|')
plt.title('Valeurs absolues calculées de la suite')
plt.grid() ; plt.show()