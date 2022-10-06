#Parameters of the hamiltonian
arbitrary_mass = 1
masses = [1,2,3,4,5,6]
k_OHconstant = [1,2,3,4,5,6]
k_coupling = [1,2,3,4,5,6]
hbar = 1.054571800e-34

#Setting up and filling up a zero_matrix.

import numpy

a = numpy.zeros((len(masses), len(masses)))

#loop to fill up the Matrix

a[0,len(masses)-1] = masses[-1]
a[len(masses)-1,0] = masses[-1]
for i in range(len(masses)):
 for j in range(len(masses)):
  if i == j + 1 :
   a[i,j]=arbitrary_mass * k_coupling[j]/numpy.sqrt(masses[i]*masses[j])
  if i == j - 1 :
   a[i,j]=arbitrary_mass * k_coupling[i]/numpy.sqrt(masses[i]*masses[j])
  if i == j :
   a[i,j]=arbitrary_mass * k_OHconstant[i]/masses[i]
print (a)

#Matrix diagonalization 

from numpy import linalg
K = linalg.eigvals(a)
print("Eigenvalues of K are {}".format(K)) 
Energy_HOS = []

for i in range(len(K)): 
 ei = (0.5) * hbar * numpy.sqrt(K[i]/arbitrary_mass)
 Energy_HOS.append(ei)
print(Energy_HOS)
print("TOTAL ENERGY IS {}!".format(sum(Energy_HOS)))

