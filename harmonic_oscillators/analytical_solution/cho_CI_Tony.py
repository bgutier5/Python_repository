#inputs reduced in number
states = 6
mass = [1.0,1.0,1.0,1,1]
k_OHconstant = [1.0,1.0,1.0,1,1]
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
 
states_per_oscillator = len(mass)


a = numpy.zeros((states**len(mass),states**len(mass)))

for i in range(states**len(mass)):
 state_string = change_of_base(i)
 e = 0.0
 for k in range(len(mass)):  
  ei = (state_string[k] + 0.5) * hbar * numpy.sqrt(k_OHconstant[k]/arbitrary_mass)  
  e += ei
 a[i,i] = e
 for j in range(states**len(mass)):
  if len(compare(state_string, change_of_base(j))) ==  2 and (compare(state_string, change_of_base(j))[1][0] - compare(state_string, change_of_base(j))[0][0] == 1 or compare(state_string, change_of_base(j))[1][0] - compare(state_string, change_of_base(j))[0][0] == len(mass) - 1 ):
   p = 0.0
   for m in range(2):
    if abs(compare(state_string, change_of_base(j))[0][1] - compare(state_string, change_of_base(j))[0][2]) == 1 and abs(compare(state_string, change_of_base(j))[1][1] - compare(state_string, change_of_base(j))[1][2]) == 1 :
     if compare(state_string, change_of_base(j))[m][1] - compare(state_string, change_of_base(j))[m][2] == 1:
      pi = ( (hbar/ (2 * (mass[compare(state_string, change_of_base(j))[m][0]] * k_OHconstant[compare(state_string, change_of_base(j))[m][0]]) ** 0.5)  ) ** 0.5) * ((compare(state_string, change_of_base(j))[m][2] + 1 )**0.5)
      kij_OH = compare(state_string, change_of_base(j))[0][0]    
     if (compare(state_string, change_of_base(j))[m][1] - compare(state_string, change_of_base(j))[m][2]) == -1:
      pi = ( (hbar/ (2 * (mass[compare(state_string, change_of_base(j))[m][0]] * k_OHconstant[compare(state_string, change_of_base(j))[m][0]]) ** 0.5)  ) ** 0.5) * ((compare(state_string, change_of_base(j))[m][2])**0.5)
      kij_OH = compare(state_string, change_of_base(j))[0][0]    
     if a[i,j] == 0:
      a[i,j] = k_coupling[kij_OH] * pi
     else: 
      a[i,j] *= pi
     
#print(a)

# Test if matrix is symmetric
t = numpy.transpose(a)
print(numpy.sum(numpy.square(numpy.subtract(a,t))))


#Matrix diagonalization

from numpy import linalg

newlist = sorted(linalg.eigvals(a))

print("TOTAL ENERGY IS {}!".format(newlist[0]))
