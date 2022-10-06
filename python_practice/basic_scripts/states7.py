#inputs reduced in number
states = 2
mass = [1,1,1,1,1,1,1,1]
k_OHconstant = [1,1,1,1,1,1,1,1]
hbar = 1
arbitrary_mass = 1

import numpy

def baseN(num,b):
  return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

Energy_HOS = []

for i in range(5):
 for j in range(len(mass)):
  mystates = baseN(i,states)
#  print(mystates)
  while len(mystates) < len(mass):
#  print(mystates)
   mystates = "0" + mystates  
  e = (int(str(mystates)[j]) + 0.5) * hbar * numpy.sqrt(k_OHconstant[i]/arbitrary_mass)
  Energy_HOS.append(e)
print(Energy_HOS)
print(sum(Energy_HOS))
