kF1 = 1.
kF2 = 1.  
x0  = 0
y0  = 0
def v(x,y):
	x = x - x0
	y = y - y0
	return ( (kF1 * x**2 / 2.) + (kF2 * y**2 / 2.) )

origin = 0
delta  = 0.1

print(v(1,4))

for i in range(5):
	for j in range(5):
		result = v(origin + i*delta, origin + j*delta)
		print(result)
