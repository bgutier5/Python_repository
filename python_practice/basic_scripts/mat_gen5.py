# Initial inputs 
states_per_oscillator = 2
mass = [1,1,1]
k_OHconstant = [1,1,1]
k_coupling = [0.1,0.1,0.1]
hbar = 1.0
arbitrary_mass = 1

import sys
import numpy
#numpy.set_printoptions(threshold=sys.maxsize)
numpy.set_printoptions(threshold=numpy.nan,linewidth=1000)
import copy
from numpy import linalg

n_oscillators = len(mass)
n_states = states_per_oscillator ** n_oscillators


def change_of_base(x):
 ivals = []
 while x > 0:
  ivals.append(x%states_per_oscillator)
  x = x // states_per_oscillator
 pad = len(mass) - len(ivals)
 ivals = ivals + [0]*pad
 return(ivals)

def change_back(y):
 N = 0
 for i in range(len(y)):
  n = y[i] * (2 ** i)
  N += n
 return(N)

def compare(bra,ket):
 diff = []
 for i in range(len(mass)):
  if bra[i] != ket[i]:
   diff.append((i,bra[i],ket[i]))
 return(diff)
 

def H_matrix(bra,ket):
  v = 0
  diffs = compare(bra,ket)
  if len(diffs) ==  0:
   for k in range(n_oscillators):
    ei = (ket[k] + 0.5) * hbar * numpy.sqrt(k_OHconstant[k]/arbitrary_mass)
    v += ei
   return v
  if len(diffs) ==  2:
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

def evaluate(bra, W, l, v, ket_string):
 k = change_back(bra)
 bra_string = bra
 mat_elem = H_matrix(bra_string,ket_string)
 W[l] += mat_elem*v[k]
