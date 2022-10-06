#  Initial inputs for the hamiltonian

states_per_oscillator = 4
number_of_oscillators = 4
mass_primitive        = [1]
k_OH_primitive        = [1]
k_coupling_primitive  = [0.1]
hbar                  = 1.0
arbitrary_mass        = 1

mass                  = number_of_oscillators * mass_primitive
k_OHconstant          = number_of_oscillators * k_OH_primitive
k_coupling            = number_of_oscillators * k_coupling_primitive   


print(mass)
print(k_OHconstant)
print(k_coupling)

# mass                  = [1,1,1]
# k_OHconstant          = [1,1,1]
# k_coupling            = [0.1,0.1,0.1]
# hbar                  = 1.0
# arbitrary_mass        = 1
