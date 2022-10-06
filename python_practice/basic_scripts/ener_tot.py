

#Matrix diagonalization exercise 
arbitrary_mass = 1
hbar = 1 #modified to make calculation easier
import numpy
from numpy import linalg
K = [1,4,9,16]
Energy_HOS = []
print(K) 
for i in range(len(K)): 
 ei = (0.5) * hbar * numpy.sqrt(K[i]/arbitrary_mass)
 Energy_HOS.append(ei)
print(sum(Energy_HOS))
