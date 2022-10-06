#Setting up and filling up a zero_matrix.

import numpy
ring_number = 5
a = numpy.zeros((ring_number, ring_number))

#loop to fill up the Matrix
for i in range(ring_number):
	for j in range(ring_number):
		if i == j + 1 or i == j - 1 :
			a[i,j]=8
		if i == j :
			a[i,j]=1
print (a)
