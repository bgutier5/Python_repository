
class occupied:
	def __init__(self, number):
		self.type   = "occupied"
		self.number =  number

class virtual:
	def __init__(self, number):
		self.type   = "virtual"
		self.number =  number

a = virtual("a")
i = occupied("i")
b = virtual("b")
j = occupied("j")
'''
print(a.type)
print(i.type)
print(b.type)
print(j.type)
'''
l = [a.type,   i.type,   b.type,   j.type]
v = [a.number, i.number, b.number, j.number]
print(l)
print(v)


def compare_del(A, B):
	if A.type !=  B.type:
		return("different")
	if A.type ==  B.type:
		return("equal")	

print( compare_del(a, b) )
print( compare_del(a, i) )
print( compare_del(i, j) )


'''
for a in range(N_vir):
	for i in range(N_occ):
		dexc_op = [ virtuals[a], occupied[i]]
		for b in range(N_vir):
			for j in range(N_occ):
				exc_op  = [ virtuals[b], occupied[j]]
				print(dexc_op, exc_op)
	
def commutator_class(op1, op2):
	if op1.type == "one body" and op2.type == "one body":
		return( commutator1-1(op1, op2) )
	if op1.type == "one body" and op2.type == "two body":
		return( commutator1-2(op1, op2) )
	if op1.type == "two body" and op2.type == "one body":
		return( commutator2-1(op1, op2) )
	if op1.type == "two body" and op2.type == "two body":
		return( commutator2-2(op1, op2) )
'''
