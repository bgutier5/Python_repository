###########################################################
#          Code belonging to FULL CI calculation          #
###########################################################
#
#  Initial inputs for the hamiltonian
#
states_per_oscillator = 2
mass = [1,1,1]
k_OHconstant = [1,1,1]
k_coupling = [0.1,0.1,0.1]
hbar = 1.0
arbitrary_mass = 1

#  Importing necessary packages and functions
#
import sys
import numpy
#numpy.set_printoptions(threshold=sys.maxsize)
numpy.set_printoptions(threshold=numpy.nan,linewidth=1000)
import copy
from mat_gen5 import change_of_base, change_back, compare, H_matrix, evaluate 
from numpy import linalg

# Calculate useful parameters
#
n_oscillators = len(mass)
n_states = states_per_oscillator ** n_oscillators
a = numpy.zeros((n_states,n_states))


# Filling up full CI matrix
#
for i in range(n_states):
 ket_string = change_of_base(i)
 for j in range(n_states):
  bra_string = change_of_base(j)
  a[i,j] = H_matrix(bra_string,ket_string)

# Printing full CI matrix
#
print(a)

# Test ot check if CI matrix is symmetric
#
#t = numpy.transpose(a)
#print(numpy.sum(numpy.square(numpy.subtract(a,t))))


# CI Matrix diagonalization and printing of ground state energy
#
#newlist = sorted(linalg.eigvals(a))
#print("TOTAL ENERGY IS {}!".format(newlist[0]))

######################################################
#    Code to define and test the different classes   #
######################################################

# Defining an arbitrary matrix to test the different classes
#
A = numpy.zeros((2,2))
A[0,0] = 1
A[0,1] = 2
A[1.0] = 3
A[1,1] = 4

# Defining a arbitrary vector to test the different classes
#
v = numpy.zeros((n_states,1))
for i in range(n_states):
 v[i] = i

# Printing the arbitrary vector(v) and arbitrary matrix(A) 
#
print(v)
#print(A)

# Printing the matrix product of FULL CI matrix and an arbitrary vector(v)
#
print(numpy.dot(a,v))

######################################################
#          Definition of different kinds of classes  #
######################################################

# This class STORES a  matrix and uses NUMPY to do matrix multiplication 
# and returns a vector using the STORED matrix
#
class matvec0:
 def __init__(self,a):
  self.a = a
 def __call__(self,b):
  return(numpy.dot(a,b))

#################################################################################
# All these next classes DOES NOT STORE a matrix. 
# A VECTOR IS FED into an instance of each class and it RETURNS a NEW vector.
# The effect on the NEW vector is the same as MULTIPLYNG it by an FULL CI matrix.
#################################################################################

 
# This class CHECKS EVERY SINGLE  element in the matrix to see if its zero or non-zero
# Uses ARRAY FORMAT to return the NEW vector
#
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
    
# This class CHECKS EVERY SINGLE element in the matrix to see if its zero or non-zero
# Uses NUMPY.MATRIX format to return the NEW vector
#
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

# This class generates the non-zero elements from each state
# It uses four independent "for loops" to generate them
#
# Details:
# Each time it generates a new non-zero state and evaluates the matrix element; it 
# gets the the numbering that corresponds to the NEW state in decimal base ; it mul-
# tiplys the obtained matrix element  by the corresponding coefficient from the FED vector. 

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

# This class generates the different non-zero elements using ONLY ONE "for loop"
# and uses MY FUNCTION "evaluate".
#
# Details:
# This class uses MY FUNCTION "evaluate" for redundant lines of code in evaluating 
# each new generated state.
# The FUNCTION "evaluate" does all the arimetic operations each time a new state 
# is generated.
#

class matvec4:
 def __call__(self,v):
  W = [0]*len(v)
  l = 0
  HO_lim = len(mass) - 1
  up_lim = states_per_oscillator - 1
  for i in range(n_states):
   ket_string = change_of_base(i)
   bra = copy.deepcopy(ket_string)
   evaluate(bra, W, l, v, ket_string)
   for i in range(-1, HO_lim):
    bra = copy.deepcopy(ket_string)
    if bra[i] < up_lim  and bra[i+1] < up_lim:
     bra[i] = bra[i] + 1
     bra[i+1] = bra[i+1] + 1
     evaluate(bra, W, l, v, ket_string)
    bra = copy.deepcopy(ket_string)
    if bra[i] > 0 and bra[i+1] > 0:
     bra[i] = bra[i] - 1
     bra[i+1] = bra[i+1] - 1
     evaluate(bra, W, l, v, ket_string)
    bra = copy.deepcopy(ket_string)
    if bra[i] > 0 and bra[i+1] < up_lim:
     bra[i] = bra[i] - 1
     bra[i+1] = bra[i+1] + 1
     evaluate(bra, W, l, v, ket_string)
    bra = copy.deepcopy(ket_string)
    if bra[i] < up_lim  and bra[i+1] > 0:
     bra[i] = bra[i] + 1
     bra[i+1] = bra[i+1] - 1
     evaluate(bra, W, l, v, ket_string)
   l += 1
  return(W)

# This class is almost a copy of "matvec3". 
# There is NO DIFFERENCE in the NEW vector
#
# Details:
# The ONLY difference is that it uses a "k" index instead of a 
# "i" index to identify the element of the FED vector(v) that mul-
# tiplys its corresponding matrix element. In the end there is no 
# difference of new generated vector. 
# 

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

# This block generates instances of each class
#

E  = matvec0(a)
H  = matvec()
h  = matvec2()
H2 = matvec3()
H3 = matvec4()
#H4 = matvec5()

# This block prints each instance of the class by calling it and feeding it the
# arbitrary vector (v)
#

#print(E(v))
#print(H(v))
#print(h(v))
#print(H2(v))
print(H3(v))
#print(H4(v))

# This block TESTS if each instance of correspoding classes gives the same 
# vector as the matrix multiplication of the FULL CI matrix by an arbitrary  
# vector (v)

#print(numpy.sum(numpy.square(numpy.subtract(numpy.dot(a,v),H(v)))))
#print(numpy.sum(numpy.square(numpy.subtract(numpy.dot(a,v),h(v)))))
#print(numpy.sum(numpy.square(numpy.subtract(numpy.dot(a,v),H2(v)))))
print(numpy.sum(numpy.square(numpy.subtract(numpy.dot(a,v),H3(v)))))
#print(numpy.sum(numpy.square(numpy.subtract(numpy.dot(a,v),H4(v)))))
#############################################

I = numpy.identity(n_states)
z = numpy.zeros((n_states,n_states))
for i in range(n_states):
 row = I[i]
 for j in range(n_states):
  col = I[:,j]
  z[i,j] = numpy.dot(row,H3(col))

#Test to verify the matvec class
print(numpy.sum(numpy.square(numpy.subtract(a,z))))

#import qode

#vec = numpy.matrix( numpy.zeros((a.shape[0],1)) )
#vec[0,0] = 1.0

#a = numpy.matrix(a)

#HAM     = qode.math.numpy_space.operator(a)
#guess = qode.math.numpy_space.vector(vec )
#evalue,evec = qode.math.lanczos.lowest_eigen(HAM,guess,1e-6,50)
#print("eigen =", evalue)
