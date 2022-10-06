
# encapsulation

def barrier(H,L):
        def v(x):
                if x <= -L/2:
                        return 0
                if x >=  L/2:
                        return 0
                if x > -L/2 and L/2:    
                        return H
        return v 


def HO_centered_at(x0):         # returns a shifted potential function
    kF = 1.                     # force constant
    def v(x):
        x = x - x0
        return kF * x**2 / 2.
    return v

print( HO_centered_at(0) )
print( barrier(5,3) )


# Verifying code/ barrier potential
'''
H = 5
L = 3
def v(x):
	if x <= -L/2:
		return 0
	if x >=  L/2:
		return 0
	if x > -L/2 and L/2:    
		return H
	return v 
'''
# box potential

L = 3

def v(x):
	if x < -L:
		return 100
	elif x >  L:
		return 100
	else:
		return 0



for i in range(-10,10):
	print( v(i) )
