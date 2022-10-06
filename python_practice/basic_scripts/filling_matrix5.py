#Setting up and filling up a zero_matrix.

import numpy as np
#from qode.many_body.hierarchical_fluctuations.translationally_transformed.integral_transformer import get_semiMO_basis


n_orbitals = 4
n_cells = 3
#f = numpy.zeros((n_orbitals, n_orbitals, n_cells))
f = np.array([np.zeros((n_orbitals, n_orbitals))] * n_cells, dtype=np.float64)

#loop to fill up the Matrix

L_0 = [-1, 0, 1]
for n in L_0: 
    for p in range(n_orbitals):
        for q in range(n_orbitals):
            f[n, p, q] = p+q #n*(n_orbitals*n_orbitals) + p*(n_orbitals) + q 

# modifying corners
f[0,3,0] = 5 
f[0,0,3] = 5

def get_semiMO_basis(S, C):
    Be_coef = len(C)
    n_Be    = int(len(S)/Be_coef)
    l = 0
    for n in range(n_Be):
        beg   = int(n*Be_coef)
        end   = int(beg + Be_coef)
        S_Be  = S[:,beg:end]
        Spp_slice   = S_Be @ C
        if l == 0:
            Spp = Spp_slice
            l  += 1
        else:
            Spp = np.concatenate( (Spp, Spp_slice), axis = 1)
    m = 0
    for n in range(n_Be):
        beg   = int(n*Be_coef)
        end   = int(beg+ Be_coef)
        S_Be  = Spp[beg:end,:]
        S_semiMO_slice = C.T @ S_Be
        if m == 0:
            S_semiMO = S_semiMO_slice
            m += 1
        else:
            S_semiMO = np.concatenate( (S_semiMO, S_semiMO_slice), axis = 0)
    return(S_semiMO)





print(f[0], 'Dummy symmetric matrix')
print('--------------------')
print(f[-1,2:,:2], 'Dummy Coefficient matrix')
print('--------------------')
print(get_semiMO_basis(f[0], f[-1,2:,:2]), 'Dummy semiMO')
