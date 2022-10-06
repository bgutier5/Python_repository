#List of masses
masses = [1,2,3,4,5,6]

#Setting up and filling up a zero_matrix.

import numpy

a = numpy.zeros((len(masses), len(masses)))

#loop to fill up the Matrix
for i in range(len(masses)):
 for j in range(len(masses)):
  if i == j + 1 or i == j - 1 :
   a[i,j]=masses[i]*masses[j]
  if i == j :
   a[i,j]=masses[i]*masses[j]
print (a)
