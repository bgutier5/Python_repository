#INPUTS/ Parameters of the hamiltonian
mass = [1,1,1,1,1]                      #masses of each of the oscilators 
k_OHconstant = [1,1,1,1,1]              #constant of each of the oscilators
k_coupling = [0.1,0.1,0.1,0.1,0.1]      #coupling constant of each pair of oscilators
hbar = 1                                #h bar in atomic units
nstates = 2                             #number of each of the states
arbitrary_mass = 1

import numpy

def baseN(num,b):
  return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])


Energy_HOS = []

for i in range(len(mass)):
 for j in range(len(mass)):
  a = (int(str(baseN(i,nstates))[j] + 0.5) * hbar * numpy.sqrt(k_OHconstant[i]/arbitrary_mass)
#  Energy_HOS.append(a)
#print(sum(Energy_HOS))

