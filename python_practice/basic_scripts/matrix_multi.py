import numpy as np

a = np.zeros((2,2))
b = np.zeros((2,1))
a[0,0] = 2
a[0,1] = 1
a[1.0] = 1
a[1,1] = 2

b[0] = 1
b[1] = 1
#print(a)
#print(b)
#print(np.dot(a,b))

class matvec:
 def __init__(self,a):
  self.a = a
 def __call__(self,b):
  return(np.dot(a,b))

H = matvec(a)
print(H(b))

