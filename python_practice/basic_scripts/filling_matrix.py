#Setting up and filling up a zero_matrix.

import numpy
ring_number = 2
a = numpy.zeros((ring_number, ring_number))

#loop to fill up the Matrix
for j in range(ring_number):
    for i in range(ring_number):
        a[i,j]= 1
print (a)
