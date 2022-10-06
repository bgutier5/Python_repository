
virtual =  ['a', 'b', 'c', 'd']
occupied = ['i', 'j', 'k', 'l']


# excitation
print("excitation")
def test_t():
	for i in virtual:
		for j in occupied:
			return(i, j)

print( test_t() ) 


'''
# dexcitation
print("dexcitation")
for i in virtual:
	for j in occupied:
		print(j, i)

# no net excitation
print("no net exc virtual")
for i in virtual:
	for j in virtual:
		print(i, j)

print("no net exc occupied")
for i in occupied:
	for j in occupied:
		print(i, j)
'''
