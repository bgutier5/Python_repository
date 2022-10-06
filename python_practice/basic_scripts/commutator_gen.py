N  = 3
p  = "i"
q  = 'q'
i  = 'i'
a  = 'a'
c1 = 1
c2 = 1


h  = [+c1, N, p, q]
t1 = [ c2, N, a, i]


def commutator(A, B):
	if A[0] == 0:
		operators = [0]
		return( operators )
	else:
		z = A[1] + B[1]
		if A[3] == B[2]:
			h1 = [+1, z, A[2], B[3] ]
		else:
			h1 = [0]
		if A[2] == B[3]:
			h2 = [-1, z, B[2], A[3] ]
		else:
			h2 = [0]
		operators = [h1, h2]
	return(operators)

com1 = commutator(h, t1)

print(com1)
#print(com1[0])
#print(com1[1])

class operator:
	def __init__(self, parameters):
		if parameters[0] == 0:
			self.full_op = [0]
		else:
			if len(parameters[2]) == 2:
				self.coeff   = parameters[0]
				self.offset  = parameters[1]
				self.indices = parameters[2]
				self.type = "one body"
				self.full_op = [ self.coeff, self.offset, self.indices ]

def commutator2(op1, op2):
	if op1.type == "one body" and op2.type == "one body":
		if op1.full_op == 0:
			result = operator([0])
			return( result )
		else:
			new_offset = op1.offset + op1.offset
			if op1.indices[1] == op2.indices[0]:
				new_op1 = [+1, new_offset, [op1.indices[0], op2.indices[1] ] ]
				one_bdy_op1 = operator(new_op1)
			else:
                        	one_bdy_op1 = operator([0])
			if op1.indices[0] == op2.indices[1]:
				new_op2 = [ -1, new_offset, [ op2.indices[0], op1.indices[1] ] ]
				one_bdy_op2 = operator(new_op2)
			else:
				one_bdy_op2 = operator([0])
			result = [ one_bdy_op1, one_bdy_op2 ]
		return( result )

param1 = [+c1, N, [p, q] ]
param2 = [ c2, N, [a, i] ]

op1 = operator(param1)
op2 = operator(param2)

com2 = commutator2(op1, op2)
print( com2[0].full_op, com2[1].full_op )

#j = 'j'
#b = 'b'
#t1 = [ 1, N, j, b]
#com2 = commutator( com1[1], t1)
#print(com2)
