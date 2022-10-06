#inputs reduced in number
states = 6
mass = [1,1,1,1,1]
k_OHconstant = [1,1,1,1,1]
k_coupling = [0.1,0.1,0.1,0.1,0.1]
hbar = 1.0
arbitrary_mass = 1

import sys
import numpy
#numpy.set_printoptions(threshold=sys.maxsize)
numpy.set_printoptions(threshold=numpy.nan,linewidth=1000)

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

list_of_states = []
for x in range(len(mass),-1,-1):
 for y in range(states**len(mass)):
  if change_of_base(y).count(0) == x:
   list_of_states.append(change_of_base(y))

for i in range(states**len(mass)):
 e = 0.0
 for k in range(len(mass)):  
  ei = (list_of_states[i][k] + 0.5) * hbar * numpy.sqrt(k_OHconstant[k]/arbitrary_mass)  
  e += ei
 a[i,i] = e
 for j in range(states**len(mass)):
  if len(compare(list_of_states[i], list_of_states[j])) ==  2 and (compare(list_of_states[i], list_of_states[j])[1][0] - compare(list_of_states[i], list_of_states[j])[0][0] == 1 or compare(list_of_states[i], list_of_states[j])[1][0] - compare(list_of_states[i], list_of_states[j])[0][0] == len(mass) - 1 ):
   p = 0.0
   for m in range(2):
    if abs(compare(list_of_states[i], list_of_states[j])[0][1] - compare(list_of_states[i], list_of_states[j])[0][2]) == 1 and abs(compare(list_of_states[i], list_of_states[j])[1][1] - compare(list_of_states[i], list_of_states[j])[1][2]) == 1 :
     if compare(list_of_states[i], list_of_states[j])[m][1] - compare(list_of_states[i], list_of_states[j])[m][2] == 1:
      pi = ( (hbar/ (2 * (mass[compare(list_of_states[i], list_of_states[j])[m][0]] * k_OHconstant[compare(list_of_states[i], list_of_states[j])[m][0]]) ** 0.5)  ) ** 0.5) * ((compare(list_of_states[i], list_of_states[j])[m][2] + 1 )**0.5)
      kij_OH = compare(list_of_states[i], list_of_states[j])[0][0]    
     if (compare(list_of_states[i], list_of_states[j])[m][1] - compare(list_of_states[i], list_of_states[j])[m][2]) == -1:
      pi = ( (hbar/ (2 * (mass[compare(list_of_states[i], list_of_states[j])[m][0]] * k_OHconstant[compare(list_of_states[i], list_of_states[j])[m][0]]) ** 0.5)  ) ** 0.5) * ((compare(list_of_states[i], list_of_states[j])[m][2])**0.5)
      kij_OH = compare(list_of_states[i], list_of_states[j])[0][0]    
     if a[i,j] == 0:
      a[i,j] = k_coupling[kij_OH] * pi
     else: 
      a[i,j] *= pi
     
#print(a)

## Test if matrix is symmetric
t = numpy.transpose(a)
print(numpy.sum(numpy.square(numpy.subtract(a,t))))


##Matrix diagonalization

from numpy import linalg

newlist = sorted(linalg.eigvals(a))

print("TOTAL ENERGY IS {}!".format(newlist[0]))
