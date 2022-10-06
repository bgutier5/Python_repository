###########################################################
#                  FULL CI calculation                    #
###########################################################

#  Importing packages and functions

import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(threshold=np.nan,linewidth=1000)
import copy
from func_CI import gen_config, num_of_config, compare, CI_prod_intern, evaluate 
from numpy import linalg
from parameters_CI import n_states, n_oscillators, states_per_oscillator 
from parameters_CI import mass, k_OHconstant, k_coupling, hbar, arbitrary_mass


# Filling up and printing FULL CI matrix

CI_matrix = np.zeros((n_states,n_states))
for i in range(n_states):
	ket_string = gen_config(i)
	for j in range(n_states):
		bra_string = gen_config(j)
		CI_matrix[i,j] = CI_prod_intern(bra_string,ket_string)
#print(CI_matrix)


# Test of symmetry on CI matrix 
#
#mat_T = np.transpose(CI_matrix)
#print(np.sum(np.square(np.subtract(  CI_matrix, mat_T  ))))


# CI Matrix diagonalization and sorting eigenvalues 
#
#sorted_eigenvals = sorted(linalg.eigvals(CI_matrix))
#print("GROUND STATE ENERGY IS {} HARTREES!".format(sorted_eigenvals[0]))
