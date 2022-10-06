from math import pi, sin, cos, exp

# General parameters

h    = 6.62606e-34
hbar = h/(2*pi)
m    = 9.1095e-31
L    = 1e-9


def value(a, nu):
	A = cos(pi*nu*L)/ (exp( -(a*L)/2 ))
	return A

def deriv(a, nu):
	A = 2*pi*nu*sin(pi*nu*L)/(a*exp( -a*L/2 ))
	return A

a_nu = 4.07e8
a_a  = 8.55e9

b_nu = 3.18e8
b_a  = 3.11e9

print("Set a)")
print(value( a_a, a_nu ))
print(deriv( a_a, a_nu ))

print("Set b")
print(value( b_a, b_nu ))
print(deriv( b_a, b_nu ))
