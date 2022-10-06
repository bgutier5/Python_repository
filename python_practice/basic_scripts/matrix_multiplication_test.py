import numpy as np

A = np.array([[2,3],[5,8],[7,9]])
B = np.array([[9,5],[10,1]])

C = A.dot(B)
print(C)

lenght_A = len(A)
lenght_B = len(B[0])
length_side_multiplication = len(A[0])
Cp = np.zeros( (lenght_A,lenght_B) )
length_side_result = len(Cp)
for n in range(lenght_A):
    for p in range(lenght_B):
        for k in range(length_side_multiplication):
            Cp[n,p] += A[n,k]*B[k,p]

print(Cp, "Boris") 
