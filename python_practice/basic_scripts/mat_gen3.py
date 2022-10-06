#inputs reduced in number
states_per_oscillator = 3
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
 

n_oscillators = len(mass)
n_states = states_per_oscillator ** n_oscillators

a = numpy.zeros((n_states,n_states))


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


# Filling up matrix

for i in range(n_states):
 ket_string = change_of_base(i)
 for j in range(n_states):
  bra_string = change_of_base(j)
  a[i,j] = H_matrix(bra_string,ket_string)

print(a)

# Test if matrix is symmetric
#t = numpy.transpose(a)
#print(numpy.sum(numpy.square(numpy.subtract(a,t))))


#Matrix diagonalization

from numpy import linalg

#newlist = sorted(linalg.eigvals(a))

#print("TOTAL ENERGY IS {}!".format(newlist[0]))

##########################################################
A = numpy.zeros((2,2))

v = numpy.zeros((n_states,1))
A[0,0] = 1
A[0,1] = 2
A[1.0] = 3
A[1,1] = 4

for i in range(n_states):
 v[i] = i


print(v)
#print(A)

print(numpy.dot(a,v))


class matvec0:
 def __init__(self,a):
  self.a = a
 def __call__(self,b):
  return(numpy.dot(a,b))


class matvec:
 def __call__(self,v):
  W = [0]*len(v)
  l = 0
  for i in range(n_states):
   ket_string = change_of_base(i)
   k = 0
   for j in range(n_states):
    bra_string = change_of_base(j)
    mat_elem = H_matrix(bra_string,ket_string)
    W[l] += mat_elem*v[k]
    k += 1
   l += 1
  return(W)
    

class matvec2:
 def __call__(self,v):
  W = numpy.zeros((len(v),1))
  l = 0
  for i in range(n_states):
   ket_string = change_of_base(i)
   for j in range(n_states):
    bra_string = change_of_base(j)
    mat_elem = H_matrix(bra_string,ket_string)
    W[l] += mat_elem*v[j]
   l += 1
  return(W) 


class matvec3:
 def __call__(self,v):
  W = [0]*len(v)
  l = 0
  for i in range(n_states):
   ket_string = change_of_base(i)
   HO_lim = len(ket_string) - 1
   up_lim = states_per_oscillator - 1
   bra_string = copy.deepcopy(ket_string)
   mat_elem = H_matrix(bra_string,ket_string)
   W[l] += mat_elem*v[i]   
   for i in range(-1, HO_lim):
    bra = copy.deepcopy(ket_string)
    if bra[i] < up_lim  and bra[i+1] < up_lim:
     bra[i] = bra[i] + 1
     bra[i+1] = bra[i+1] + 1
     k = change_back(bra)
     bra_string = bra
     mat_elem = H_matrix(bra_string,ket_string)
     W[l] += mat_elem*v[k]
   for i in range(-1, HO_lim):
    bra = copy.deepcopy(ket_string)
    if bra[i] > 0 and bra[i+1] > 0:
     bra[i] = bra[i] - 1
     bra[i+1] = bra[i+1] - 1
     k = change_back(bra)
     bra_string = bra
     mat_elem = H_matrix(bra_string,ket_string)
     W[l] += mat_elem*v[k]
   for i in range(-1, HO_lim):
    bra = copy.deepcopy(ket_string)
    if bra[i] > 0 and bra[i+1] < up_lim:
     bra[i] = bra[i] - 1
     bra[i+1] = bra[i+1] + 1
     k = change_back(bra)
     bra_string = bra
     mat_elem = H_matrix(bra_string,ket_string)
     W[l] += mat_elem*v[k]     
   for i in range(-1, HO_lim):
    bra = copy.deepcopy(ket_string)
    if bra[i] < up_lim  and bra[i+1] > 0:
     bra[i] = bra[i] + 1
     bra[i+1] = bra[i+1] - 1
     k = change_back(bra)
     bra_string = bra
     mat_elem = H_matrix(bra_string,ket_string)
     W[l] += mat_elem*v[k]  
   l += 1
  return(W)

def evaluate(bra, W, l, ket_string):
 k = change_back(bra)
 bra_string = bra
 mat_elem = H_matrix(bra_string,ket_string)
 W[l] += mat_elem*v[k]

class matvec4:
 def __call__(self,v):
  W = [0]*len(v)
  l = 0
  HO_lim = len(mass) - 1
  up_lim = states_per_oscillator - 1
  for i in range(n_states):
   ket_string = change_of_base(i)
   bra = copy.deepcopy(ket_string)
   evaluate(bra, W, l, ket_string)
   for i in range(-1, HO_lim):
    bra = copy.deepcopy(ket_string)
    if bra[i] < up_lim  and bra[i+1] < up_lim:
     bra[i] = bra[i] + 1
     bra[i+1] = bra[i+1] + 1
     evaluate(bra, W, l, ket_string)
    bra = copy.deepcopy(ket_string)
    if bra[i] > 0 and bra[i+1] > 0:
     bra[i] = bra[i] - 1
     bra[i+1] = bra[i+1] - 1
     evaluate(bra, W, l, ket_string)
    bra = copy.deepcopy(ket_string)
    if bra[i] > 0 and bra[i+1] < up_lim:
     bra[i] = bra[i] - 1
     bra[i+1] = bra[i+1] + 1
     evaluate(bra, W, l, ket_string)
    bra = copy.deepcopy(ket_string)
    if bra[i] < up_lim  and bra[i+1] > 0:
     bra[i] = bra[i] + 1
     bra[i+1] = bra[i+1] - 1
     evaluate(bra, W, l, ket_string)
   l += 1
  return(W)

class matvec5:
 def __call__(self,v):
  W = [0]*len(v)
  l = 0
  for i in range(n_states):
   ket_string = change_of_base(i)
   HO_lim = len(ket_string) - 1
   up_lim = states_per_oscillator - 1
   bra = copy.deepcopy(ket_string)
   k = change_back(bra)
   bra_string = bra
   mat_elem = H_matrix(bra_string,ket_string)
   W[l] += mat_elem*v[k]   
   for i in range(-1, HO_lim):
    bra = copy.deepcopy(ket_string)
    if bra[i] < up_lim  and bra[i+1] < up_lim:
     bra[i] = bra[i] + 1
     bra[i+1] = bra[i+1] + 1
     k = change_back(bra)
     bra_string = bra
     mat_elem = H_matrix(bra_string,ket_string)
     W[l] += mat_elem*v[k]
   for i in range(-1, HO_lim):
    bra = copy.deepcopy(ket_string)
    if bra[i] > 0 and bra[i+1] > 0:
     bra[i] = bra[i] - 1
     bra[i+1] = bra[i+1] - 1
     k = change_back(bra)
     bra_string = bra
     mat_elem = H_matrix(bra_string,ket_string)
     W[l] += mat_elem*v[k]
   for i in range(-1, HO_lim):
    bra = copy.deepcopy(ket_string)
    if bra[i] > 0 and bra[i+1] < up_lim:
     bra[i] = bra[i] - 1
     bra[i+1] = bra[i+1] + 1
     k = change_back(bra)
     bra_string = bra
     mat_elem = H_matrix(bra_string,ket_string)
     W[l] += mat_elem*v[k]     
   for i in range(-1, HO_lim):
    bra = copy.deepcopy(ket_string)
    if bra[i] < up_lim  and bra[i+1] > 0:
     bra[i] = bra[i] + 1
     bra[i+1] = bra[i+1] - 1
     k = change_back(bra)
     bra_string = bra
     mat_elem = H_matrix(bra_string,ket_string)
     W[l] += mat_elem*v[k]  
   l += 1
  return(W)

E  = matvec0(a)
H  = matvec()
h  = matvec2()
H2 = matvec3()
H3 = matvec4()
H4 = matvec5()

#print(E(v))
#print(H(v))
#print(h(v))
#print(H2(v))
#print(H3(v))
print(H4(v))

#print(numpy.sum(numpy.square(numpy.subtract(numpy.dot(a,v),H(v)))))
print(numpy.sum(numpy.square(numpy.subtract(numpy.dot(a,v),h(v)))))
#print(numpy.sum(numpy.square(numpy.subtract(numpy.dot(a,v),H2(v)))))
#print(numpy.sum(numpy.square(numpy.subtract(numpy.dot(a,v),H3(v)))))
print(numpy.sum(numpy.square(numpy.subtract(numpy.dot(a,v),H4(v)))))
#############################################

#I = numpy.identity(n_states)
#z = numpy.zeros((n_states,n_states))
#for i in range(n_states):
# row = I[i]
# for j in range(n_states):
#  col = I[:,j]
#  z[i,j] = numpy.dot(row,H(col))

#Test to verify the matvec class
#print(numpy.sum(numpy.square(numpy.subtract(a,z))))

#import qode

#vec = numpy.matrix( numpy.zeros((a.shape[0],1)) )
#vec[0,0] = 1.0

#a = numpy.matrix(a)

#HAM     = qode.math.numpy_space.operator(a)
#guess = qode.math.numpy_space.vector(vec )
#evalue,evec = qode.math.lanczos.lowest_eigen(HAM,guess,1e-6,50)
#print("eigen =", evalue)
