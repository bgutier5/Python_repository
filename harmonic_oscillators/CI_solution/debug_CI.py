import numpy as np
import code_CI
from class_CI import mat_dot_vec4 
from  code_CI import CI_mat 
from parameters_CI import states_per_oscillator, mass, k_OHconstant
from parameters_CI import k_coupling, hbar, arbitrary_mass


H_param = {
            "mass":                  mass,
	    "states_per_oscillator": states_per_oscillator,
	    "k_OHconstant":          k_OHconstant,
	    "k_coupling":            k_coupling,
            "hbar":                  hbar,
            "arbitrary_mass":        arbitrary_mass}

# This block generates the correspoding classes to compare

H  =  mat_dot_vec4( H_param )
CI_matrix = CI_mat( H_param )

# Test to check matrix generated from class mat_dot_vec

n_states   = states_per_oscillator ** len(mass)
I          = np.identity( n_states )
CLS_matrix = np.zeros(( n_states,n_states ))
for j in range( n_states ):
	row = I[j]
	for i in range( n_states ):
		col = I[:,i]
		CLS_matrix[i,j] = np.dot(row,H(col))


diff = np.sum( np.square( np.subtract( CI_matrix, CLS_matrix) ) )
print("Difference between matrices is {}".format( diff ))
