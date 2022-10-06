import numpy as np
import time
import timeit

A = np.array([[1,2,3],[3,4,1], [7,3,1]])
B = np.array([[1,2,3],[3,4,1], [7,3,1]])

start_method2 = timeit.default_timer()
start = time.time()
#A[:] = 0.0
b = 0
end = time.time()
elapsed = timeit.default_timer() - start_method2
print('method [:] =', end - start)
print('method 2   =', elapsed)
print('--------------')


start = time.time()
B.fill(0.0)
for i in range(3):
    for j in range(3):
        B[i,j] = 3*4+2-3+6+i-j
e, v = np.linalg.eig(B)
end = time.time()

elapsed2 = timeit.default_timer() - start_method2

print('method fill=', end - start)
print('method 2   =', elapsed2)
