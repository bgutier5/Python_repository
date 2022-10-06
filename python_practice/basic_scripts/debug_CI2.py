import numpy as np
import code_CI
from class_CI import mat_dot_vec0, mat_dot_vec, mat_dot_vec2, mat_dot_vec4 
from class_CI import mat_dot_vec5, mat_dot_vec3
from code_CI  import CI_matrix, n_states

# Arbitrary vector

vec = np.zeros( (n_states,1) )
for i in range(n_states):
	vec[i] = i
#print(vec)


# This block generates instances of each class

E  = mat_dot_vec0(CI_matrix)
H  = mat_dot_vec()
h  = mat_dot_vec2()
H2 = mat_dot_vec3()
H3 = mat_dot_vec4()
H4 = mat_dot_vec5()

# Printing each instance of the class and feeding it the
# arbitrary vector (vec)
#

#print( E(vec) )
#print( H(vec) )
#print( h(vec) )
#print( H2(vec) )
#print( H3(vec) )
#print( H4(vec) )

# This block TESTS if each instance of correspoding classes gives the same 
# vector as the matrix multiplication of the FULL CI matrix by an arbitrary  
# vector (vec)

dif_vec0 = np.sum(np.square(np.subtract(np.dot(CI_matrix,vec),H(vec))))
dif_vec1 = np.sum(np.square(np.subtract(np.dot(CI_matrix,vec),h(vec))))
dif_vec2 = np.sum(np.square(np.subtract(np.dot(CI_matrix,vec),H2(vec))))
dif_vec3 = np.sum(np.square(np.subtract(np.dot(CI_matrix,vec),H3(vec))))
dif_vec4 = np.sum(np.square(np.subtract(np.dot(CI_matrix,vec),H4(vec))))

print("The difference between the vectors is {}".format( dif_vec0 ))
print("The difference between the vectors is {}".format( dif_vec1 ))
print("The difference between the vectors is {}".format( dif_vec2 ))
print("The difference between the vectors is {}".format( dif_vec3 ))
print("The difference between the vectors is {}".format( dif_vec4 ))

# Test to check matrix generated from class

I = np.identity(n_states)
cls_mat = np.zeros((n_states,n_states))
for i in range(n_states):
	row = I[i]
	for j in range(n_states):
		col = I[:,j]
		cls_mat[i,j] = np.dot(row,H3(col))


diff= np.sum( np.square( np.subtract( CI_matrix,cls_mat ) ) )
print("Difference between matrices is {}".format(diff))
