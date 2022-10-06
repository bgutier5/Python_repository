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
from class_CI import CI_inner_product


# Filling up and printing FULL CI matrix

def CI_mat(H_param):
	n_oscillators = len(H_param["mass"])
	n_states = H_param["states_per_oscillator"] ** n_oscillators
	CI_matrix = np.zeros((n_states,n_states))
	CI_mat_element = CI_inner_product(H_param)
	for i in range(n_states):
		ket_string = gen_config(i, H_param)
		for j in range(n_states):
			bra_string = gen_config(j, H_param)
			CI_matrix[i,j] = CI_mat_element(bra_string,ket_string)
	return(CI_matrix)


