import math
#Parameters of the hamiltonian
arbitrary_mass = 1
hbar           =1 #1.054571800e-34


number_OHs     = 7
mass_of_OH     = 1
k_OH           = 1
v_coupling     = 0.9



mass           = number_OHs * [ mass_of_OH ] 
k_OHconstant   = number_OHs * [ k_OH ]
k_coupling     = number_OHs * [ v_coupling ]

#Setting up and filling up a zero_matrix.

import numpy

a = numpy.zeros((len(mass), len(mass)))

#loop to fill up the Matrix

a[0,len(k_coupling)-1] = k_coupling[-1]
a[len(k_coupling)-1,0] = k_coupling[-1]
for i in range(len(mass)):
 for j in range(len(mass)):
  if i == j + 1 :
   a[i,j]=arbitrary_mass * k_coupling[j]/numpy.sqrt(mass[i]*mass[j])
  if i == j - 1 :
   a[i,j]=arbitrary_mass * k_coupling[i]/numpy.sqrt(mass[i]*mass[j])
  if i == j :
   a[i,j]=arbitrary_mass * k_OHconstant[i]/mass[i]
#print (a)

#Matrix diagonalization 

from numpy import linalg
K = linalg.eigvals(a)
print("Eigenvalues of K are {}".format(K)) 
Energy_HOS = []

for i in range(len(K)): 
 ei = (0.5) * hbar * numpy.sqrt(K[i]/arbitrary_mass)
 Energy_HOS.append(ei)
#print("Energy of each of the HO is {}!".format(Energy_HOS))
print("TOTAL ENERGY IS {}!".format(sum(Energy_HOS)))

