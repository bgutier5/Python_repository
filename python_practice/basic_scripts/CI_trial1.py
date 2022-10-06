#inputs reduced in number
states = 2
mass = [1,1,1]
k_OHconstant = [1,1,1]
hbar = 1
arbitrary_mass = 1

import numpy

def change_of_base(x,length):
 ivals = []
 while x > 0:
  ivals.append(x%states)
  x = x // states
 pad = length - len(ivals)
 ivals = ivals + [0]*pad
 return(ivals)

a = numpy.zeros((states**len(mass),states**len(mass)))


for i in range(states**len(mass)):
 e = 0.0
 for j in range(len(mass)):  
  ei = (change_of_base(i,len(mass))[j] + 0.5) * hbar * numpy.sqrt(k_OHconstant[j]/arbitrary_mass)  
  e += ei
 a[i,i] = e
print(a)



