#inputs reduced in number
states = 3
mass = [1,1]
k_OHconstant = [1,1]
k_coupling = [0.1,0.1]
hbar = 1
arbitrary_mass = 1

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

def change_of_base(x):
 ivals = []
 while x > 0:
  ivals.append(x%states)
  x = x // states
 pad = len(mass) - len(ivals)
 ivals = ivals + [0]*pad
 return(ivals)

def compare(bra,ket):
 diff = []
 for i in range(len(mass)):
  if bra[i] != ket[i]:
   diff.append((i,bra[i],ket[i]))
 return(diff)
 


a = numpy.zeros((states**len(mass),states**len(mass)))


for i in range(states**len(mass)):
 e = 0.0
 for k in range(len(mass)):  
  ei = (change_of_base(i)[k] + 0.5) * hbar * numpy.sqrt(k_OHconstant[k]/arbitrary_mass)  
  e += ei
 a[i,i] = e
 for j in range(states**len(mass)):
#####################################################
  if i == 0 and j == 7:
   print(compare(change_of_base(i), change_of_base(j)))
######################################################
  if len(compare(change_of_base(i), change_of_base(j))) ==  2 and (compare(change_of_base(i), change_of_base(j))[1][0] - compare(change_of_base(i), change_of_base(j))[0][0] == 1 or compare(change_of_base(i), change_of_base(j))[1][0] - compare(change_of_base(i), change_of_base(j))[0][0] == len(mass) - 1 ):
#######################################################
   if i == 0 and j == 8:
    print("Check2")
########################################################
   p = 0.0
   for m in range(2):
    if compare(change_of_base(i), change_of_base(j))[m][1] - compare(change_of_base(i), change_of_base(j))[m][2] == 1:
#####################################################
     if i == 0 and j == 8:
      print("Check3")
######################################################
     pi = ( (hbar/ (2 * (mass[compare(change_of_base(i), change_of_base(j))[m][0]] * k_OHconstant[compare(change_of_base(i), change_of_base(j))[m][0]]) ** 0.5)  ) ** 0.5) * ((compare(change_of_base(i), change_of_base(j))[m][2] + 1 )**0.5)
     kij_OH = compare(change_of_base(i), change_of_base(j))[0][0]    
    if (compare(change_of_base(i), change_of_base(j))[m][1] - compare(change_of_base(i), change_of_base(j))[m][2]) == -1:
#######################################################
     if i == 0 and j == 8:
      print("Check4")
#######################################################
     pi = ( (hbar/ (2 * (mass[compare(change_of_base(i), change_of_base(j))[m][0]] * k_OHconstant[compare(change_of_base(i), change_of_base(j))[m][0]]) ** 0.5)  ) ** 0.5) * ((compare(change_of_base(i), change_of_base(j))[m][2])**0.5)
     kij_OH = compare(change_of_base(i), change_of_base(j))[0][0]    
    if a[i,j] == 0:
     a[i,j] = k_coupling[kij_OH] * pi
    else: 
     a[i,j] *= pi
 
#print(a)

#Matrix diagonalization

from numpy import linalg

print("TOTAL ENERGY IS {}!".format(linalg.eigvals(a)[0]))
