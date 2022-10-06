import numpy as np

a = np.zeros((2,2))
b = np.zeros((2,1))
a[0,0] = 1
a[0,1] = 5
a[1.0] = 3
a[1,1] = 4

b[0] = 2
b[1] = 4
print(a)
print(b)
print(np.dot(a,b))

class matvec:
 def __init__(self,c):
  self.c = c
 def __call__(self,v):
  W = [0] * len(v)
  l = 0
  for i in range(len(a)):
   k = 0
   for j in range(len(a)):
    mat_elem = a[i,j]
    W[l] += mat_elem * v[k]
    k += 1
   l += 1
  return(W)


H = matvec(a)
print(H(b))

I = np.identity(2)
z = np.zeros((2,2)) 
for i in range(2):
 row = I[i]
 for j in range(2):
  col = I[:,j]
  z[i,j] = np.dot(row,H(col))
#print(z)


# Test if matrices are the same

print(np.sum(np.square(np.subtract(np.dot(a,b),H(b)))))
