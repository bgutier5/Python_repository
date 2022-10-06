from math import pi

# General parameters

h    = 6.62606e-34
hbar = h/(2*pi)
m    = 9.1095e-31
D    = 0.5206 * 1.6022e-19 

def Energy_out(a):
	E1 = ( -(hbar**2) * (a**2) )/ (2*m)
	return E1

def Energy_in(v_nu):
	T  =  (hbar**2) * ( (2*pi*v_nu)**2 )  / (2*m) 
	V  = -0.5206 * 1.6022e-19
	E2 = T + V
	return E2

# First set 

A_v_nu = 4.07e8
A_a    = 8.55e9

print("Set a")
print( "Energy outside", Energy_out(A_a)   )
print( "Energy inside ", Energy_in(A_v_nu) )
print( Energy_out(A_a)/ Energy_in(A_v_nu) )

# Second set
B_v_nu = 3.18e8
B_a    = 3.11e9

print("Set b")
print( "Energy outside", Energy_out(B_a)   )
print( "Energy inside ", Energy_in(B_v_nu) )
print( Energy_out(B_a)/ Energy_in(B_v_nu)  )

alfa = ( - (2*pi*A_v_nu)**2 + 2*m*D/( (hbar)**2 ) )**0.5
print("Alfa = ", alfa)
