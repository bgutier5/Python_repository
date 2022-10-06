#Test for H class using CISD matrix

#inputs reduced in number
states = 3
mass = [1,1,1]
k_OHconstant = [1,1,1]
k_coupling = [0.1,0.1,0.1]
hbar = 1.0
arbitrary_mass = 1

import sys
import numpy
#numpy.set_printoptions(threshold=sys.maxsize)
numpy.set_printoptions(threshold=numpy.nan,linewidth=1000)

def change_of_base(x):
 s = 0
 if x == 0:
  ivals = [0]*len(mass)
  return(ivals)
 s += 1

 for i in range(len(mass)):
  for l in range(1, states):
   if s == x:
    ivals = [0]*len(mass)
    ivals[i] = l
    ivals.reverse()
    return(ivals)
   s += 1

 for j in range(len(mass)):
  for i in range(j+1,len(mass)):
   for l in range(1, states):
    for m in range(1, states):
     if s == x:
      ivals = [0]*len(mass)
      ivals[i] = l
      ivals[j] = m
      ivals.reverse()
      return(ivals)
     s += 1

 if s <= x:
  ivals = [0]*len(mass)
  return(ivals)
  



def compare(bra,ket):
 diff = []
 for i in range(len(mass)):
  if bra[i] != ket[i]:
   diff.append((i,bra[i],ket[i]))
 return(diff)
 


a = numpy.zeros((states**len(mass),states**len(mass)))

list_of_states = []
for q in range(states**len(mass)):
 list_of_states.append(change_of_base(q))
#print(list_of_states)
 

for i in range(states**len(mass)):
 e = 0.0
 for k in range(len(mass)):  
  ei = (change_of_base(i)[k] + 0.5) * hbar * numpy.sqrt(k_OHconstant[k]/arbitrary_mass)  
  e += ei
 a[i,i] = e
 for j in range(states**len(mass)):
  if len(compare(change_of_base(i), change_of_base(j))) ==  2 and (compare(change_of_base(i), change_of_base(j))[1][0] - compare(change_of_base(i), change_of_base(j))[0][0] == 1 or compare(change_of_base(i), change_of_base(j))[1][0] - compare(change_of_base(i), change_of_base(j))[0][0] == len(mass) - 1 ):
   p = 0.0
   for m in range(2):
    if abs(compare(change_of_base(i), change_of_base(j))[0][1] - compare(change_of_base(i), change_of_base(j))[0][2]) == 1 and abs(compare(change_of_base(i), change_of_base(j))[1][1] - compare(change_of_base(i), change_of_base(j))[1][2]) == 1 :
     if compare(change_of_base(i), change_of_base(j))[m][1] - compare(change_of_base(i), change_of_base(j))[m][2] == 1:
      pi = ( (hbar/ (2 * (mass[compare(change_of_base(i), change_of_base(j))[m][0]] * k_OHconstant[compare(change_of_base(i), change_of_base(j))[m][0]]) ** 0.5)  ) ** 0.5) * ((compare(change_of_base(i), change_of_base(j))[m][2] + 1 )**0.5)
      kij_OH = compare(change_of_base(i), change_of_base(j))[0][0]    
     if (compare(change_of_base(i), change_of_base(j))[m][1] - compare(change_of_base(i), change_of_base(j))[m][2]) == -1:
      pi = ( (hbar/ (2 * (mass[compare(change_of_base(i), change_of_base(j))[m][0]] * k_OHconstant[compare(change_of_base(i), change_of_base(j))[m][0]]) ** 0.5)  ) ** 0.5) * ((compare(change_of_base(i), change_of_base(j))[m][2])**0.5)
      kij_OH = compare(change_of_base(i), change_of_base(j))[0][0]    
     if a[i,j] == 0:
      a[i,j] = k_coupling[kij_OH] * pi
     else: 
      a[i,j] *= pi
     
#print(a)

# Test if matrix is symmetric
#t = numpy.transpose(a)
#print(numpy.sum(numpy.square(numpy.subtract(a,t))))


#Matrix diagonalization

from numpy import linalg

newlist = sorted(linalg.eigvals(a))

#print("TOTAL ENERGY IS {}!".format(newlist[0]))


class matvec:
 def __init__(self,a):
  self.a = a
 def __call__(self,b):
  return(numpy.dot(a,b))

H = matvec(a)
n_states = states**len(mass)

I = numpy.identity(n_states)
z = numpy.zeros((n_states,n_states))
for i in range(n_states):
 row = I[i]
 for j in range(n_states):
  col = I[:,j]
  z[i,j] = numpy.dot(row,H(col))

#Test to verify the matvec class
print(numpy.sum(numpy.square(numpy.subtract(a,z))))

