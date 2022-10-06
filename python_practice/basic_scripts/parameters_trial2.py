###########################################################
#                      HO parameters                      #
###########################################################

#  Initial inputs for the hamiltonian
mass         = [1]
k_OHconstant = [1]
k_coupling   = [0.1]
n_HOs        =  2 

states_per_oscillator = 2
mass                  = mass         * n_HOs
k_OHconstant          = k_OHconstant * n_HOs
k_coupling            = k_coupling   * n_HOs
hbar                  = 1.0
arbitrary_mass        = 1

#print(mass)
#print(k_OHconstant)
#print(k_coupling)

# Calculate useful parameters
#
#n_oscillators = len(mass)
#n_states = states_per_oscillator ** n_oscillators
#CI_matrix = np.zeros((n_states,n_states))


