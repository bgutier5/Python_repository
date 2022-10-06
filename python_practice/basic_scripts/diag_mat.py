import numpy as np
from numpy import linalg

for i in range(2,9):
 print(i)
 mat = np.zeros((i,i))
 mat[0, i-1] = 0.1
 mat[i-1 ,0] = 0.1
 for j in range(i):
   mat[j,j] = j+1 
 print(mat)
 print(linalg.eigvals(mat))

