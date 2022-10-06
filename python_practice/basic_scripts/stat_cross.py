#inputs of the hamiltoninan (reduced in number)
states = 2
mass = [1,1,1]

import numpy
ring_number = 8
a = numpy.zeros((ring_number, ring_number))

def baseN(num,b):
  return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

#loop to fill up the Matrix
for j in range(ring_number):
 for i in range(ring_number):
   bra = baseN(i,states)     
   ket = baseN(j,states)
   while len(bra) < len(mass):
    bra = "0" + bra
   while len(ket) < len(mass):
    ket = "0" + ket
# a[i,j]= 1
#        print (a)
