########################################################
#                       Class module                   #
########################################################
import sys
import numpy
#numpy.set_printoptions(threshold=sys.maxsize)
numpy.set_printoptions(threshold=numpy.nan,linewidth=1000)
import copy
from numpy import linalg
from func_CI import eval_up_up, eval_dwn_dwn, eval_dwn_up, eval_up_dwn, eval_diagonal
from func_CI import gen_config, compare, evaluate, num_of_config, CI_prod_intern


class CI_inner_product:
	def __init__(self, H_param):
		self.H_param        = H_param
	def __call__(self, bra, ket):
		mat_element = CI_prod_intern( bra, ket, self.H_param)
		return(mat_element) 



# This class generates the different non-zero elements using ONLY ONE "for loop"
# and uses MY FUNCTION "evaluate".
#
# Details:
# This class uses MY FUNCTION "evaluate" for redundant lines of code in evaluating 
# each new generated state.
# The FUNCTION "evaluate" does all the arimetic operations each time a new state 
# is generated.
#
class mat_dot_vec4:
	def __init__(self, H_param):
		self.H_param       = H_param
		self.n_oscillators = len(self.H_param["mass"])
		self.n_states      = H_param["states_per_oscillator"] ** self.n_oscillators
	def __call__(self,vec):
		CI_mat_el =  CI_inner_product(self.H_param)
		final_vec =  numpy.zeros((len(vec),1))
		l         =  0
		HO_lim    =  len(self.H_param["mass"])       - 1
		up_lim    =  self.H_param["states_per_oscillator"] - 1
		for i in range(self.n_states):
			ket_str = gen_config(i, self.H_param)
			eval_diagonal( up_lim, final_vec, l, vec, ket_str, i, CI_mat_el)
			for i in range(-1, HO_lim):
				eval_up_up(  up_lim, final_vec, l, vec, ket_str, i, CI_mat_el)
				eval_dwn_dwn(up_lim, final_vec, l, vec, ket_str, i, CI_mat_el)
				eval_dwn_up( up_lim, final_vec, l, vec, ket_str, i, CI_mat_el)
				eval_up_dwn( up_lim, final_vec, l, vec, ket_str, i, CI_mat_el) 
			l += 1
		return(final_vec)

