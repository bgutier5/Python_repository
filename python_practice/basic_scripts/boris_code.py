#inputs reduced in number
states_per_oscillator = 3
mass = [1,1,1,1]
k_OHconstant = [1,1,1,1]
k_coupling = [0.1,0.1,0.1,0.1]
hbar = 1.0
arbitrary_mass = 1

import sys
import numpy
#numpy.set_printoptions(threshold=sys.maxsize)
numpy.set_printoptions(threshold=numpy.nan,linewidth=1000)

def change_of_base(x):
 ivals = []
 while x > 0:
  ivals.append(x%states_per_oscillator)
  x = x // states_per_oscillator
 pad = len(mass) - len(ivals)
 ivals = ivals + [0]*pad
 return(ivals)

def compare(bra,ket):
 diff = []
 for i in range(len(mass)):
  if bra[i] != ket[i]:
   diff.append((i,bra[i],ket[i]))
 return(diff)
 

n_oscillators = len(mass)
n_states = states_per_oscillator ** n_oscillators

a = numpy.zeros((n_states,n_states))


def H_matrix(bra,ket):
  v = 0
  diffs = compare(ket,bra)
  if len(diffs ==  2):
   pos1 = diffs[0][0]
   pos2 = diffs[1][0]
   bra1 = diffs[0][1] 
   ket1 = diffs[0][2]
   bra2 = diffs[1][1]
   ket2 = diffs[1][2]
   if (pos2 - pos1 == 1) or (pos2 - pos1 == n_oscillators - 1 ):
    p = 0.0
    for m in range(2):
     if abs(bra1 - ket1) == 1 and abs(bra2 - ket2) == 1 :
      pos_m = diffs[m][0]
      bra_m = diffs[m][1]
      ket_m = diffs[m][2]
      if bra_m - ket_m == 1:
       pi = ( (hbar/ (2 * (mass[pos_m] * k_OHconstant[pos_m]) ** 0.5)  ) ** 0.5) * ((ket_m + 1 )**0.5)
       kij_OH = pos1    
      if (bra_m- ket_m) == -1:
       pi = ( (hbar/ (2 * (mass[pos_m] * k_OHconstant[pos_m]) ** 0.5)  ) ** 0.5) * ((ket_m)**0.5)
       kij_OH = pos1    
      if v == 0:
       v = k_coupling[kij_OH] * pi
      else: 
       v *= pi
  return v



for i in range(n_states):
 ket_string = change_of_base(i)
 for j in range(n_states):
  bra_string = change_of_base(j)
  a[i,j] = H_matrix(bra_string,ket_string)
 e = 0.0
 for k in range(n_oscillators):  
  ei = (ket_string[k] + 0.5) * hbar * numpy.sqrt(k_OHconstant[k]/arbitrary_mass)  
  e += ei
 a[i,i] = e

     
#print(a)

# Test if matrix is symmetric
t = numpy.transpose(a)
print(numpy.sum(numpy.square(numpy.subtract(a,t))))


#Matrix diagonalization

from numpy import linalg

newlist = sorted(linalg.eigvals(a))

print("TOTAL ENERGY IS {}!".format(newlist[0]))

vec = numpy.matrix( numpy.zeros((a.shape[0],1)) )
vec[0,0] = 1.0

HAM     = qode.math.numpy_space.operator(a)
guess = qode.math.numpy_space.vector(vec )
evalue,evec = qode.math.lanczos.lowest_eigen(HAM,guess,1e-6,50)


