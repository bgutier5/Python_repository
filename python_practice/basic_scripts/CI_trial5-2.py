#inputs reduced in number
states = 2
mass = [1,1,1]
k_OHconstant = [1,1,1]
hbar = 1
arbitrary_mass = 1

import numpy

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
  if len(compare(change_of_base(i), change_of_base(j))) ==  2:
   p = hbar + 0.3
   for m in range(2):
    if compare(change_of_base(i), change_of_base(j))[m][1] - compare(change_of_base(i), change_of_base(j))[m][2] == 1:
     pi = (compare(change_of_base(i), change_of_base(j))[m][2] + 1 )**0.5
     p *= pi
     a[i,j] = p 
######################################
     if i == 4 and j == 2:
      print(a[i,j])
      print(pi)
      print(p)
######################################
#    print(compare(change_of_base(i), change_of_base(j))[m][2] + 1 )
    if (compare(change_of_base(i), change_of_base(j))[m][1] - compare(change_of_base(i), change_of_base(j))[m][2]) == -1:
     pj  = (compare(change_of_base(i), change_of_base(j))[m][2])**0.5    
     p *= pj
     a[i,j] = p
 
print(a)
