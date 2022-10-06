mass = [1,1,1,1,1]

import numpy

def baseN(num,b):
  return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

Energy_HOS = []

for j in range(len(mass)):
 e = (int(str(baseN(16,2))[j]) + 0.5) *  1
 Energy_HOS.append(e)
print(Energy_HOS) 
print(sum(Energy_HOS))
