#this program uses the delta de Kroenecker to fill up the matrix

def delta_Kronecker(i,j):
 if (i==j):
  return(1)
 else:
  return(0)

import numpy

a = numpy.zeros((5,5))
for n in range(5):
 for m in range(5):
   a[n,m]=5*delta_Kronecker(n,m)
print (a)
