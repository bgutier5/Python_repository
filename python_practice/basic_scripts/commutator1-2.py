c1 = 1
N  = 3
p  = "i"
q  = 'q'

c2 = 1
k  = 2
l  = 5
h  = 7
a  = 'a'
b  = 'b'
i  = 'i'
j  = 'j'


h1  = [+c1, N, p, q]
t2  = [ c2, k, l, h, a, b, i, j]


def commutator(A, B ):
	if A[0] == 0:
		operators = [0]
		return( operators )
	else:
		w1 = A[1] + B[1]
		w2 = B[3] - A[1]
		w3 = B[2] + A[1]
		w4 = A[1] + B[3]
		if A[3] == B[4]:
			g1 = [+1, w1, B[2], B[3], A[2], B[5], B[6], B[7] ]
		else:
			g1 = [0]
		if A[2] == B[7]:
			g2 = [-1, B[1], B[2], w2, B[4], B[5], B[6], A[3] ]
		else:
			g2 = [0]
		if A[3] == B[5]:
			g3 = [+1, B[1], w3, B[3], B[4], A[2], B[6], B[7] ]
		else:
			g3 = [0]
		if A[2] == B[6]:
			g4 = [-1, w1, w3, w4, B[4], B[5], A[3], B[7]]
		else:
			g4 = [0] 
		operators = [g1, g2, g3, g4]
	return(operators)

com1 = commutator(h1, t2)

print(com1)

class operator:
        def __init__(self, parameters):
                if parameters[0] == 0:
                        self.full_op = [0]
                else:
                        if len(parameters[2]) == 2:
                                self.type    = "one body"
                                self.coeff   = parameters[0]
                                self.offset  = parameters[1]
                                self.indices = parameters[2]
                                self.full_op = [ self.coeff, self.offset, self.indices ]
                        if len(parameters[2]) == 4:
                                self.type    = "two body"
                                self.coeff   = parameters[0]
                                self.offset  = parameters[1]
                                self.indices = parameters[2]
                                self.full_op = [self.coeff, self.offset, self.indices ]

def commutator2(op1, op2):
	if op1.type == "one body" and op2.type == "two body":
		if op1.full_op == 0:
			result = operator([0])
			return(result)
		else:
			if op1.indices[1] == op2.indices[0]:
				w1          = op1.offset + op2.offset[0]
				new_offset  = [w1, op2.offset[1], op2.offset[2] ]
				new_indices = [op1.indices[0], op2.indices[1], op2.indices[2], op2.indices[3] ]
				new_op1     = [+1, new_offset, new_indices ]
				two_bdy_op1 = operator(new_op1)
			else:
				two_bdy_op1 = operator([0])
			if op1.indices[0] == op2.indices[3]:
				w2          = op2.offset[2] - op1.offset
				new_offset  = [ op2.offset[0], op2.offset[1], w2 ]
				new_indices = [ op2.indices[0], op2.indices[1], op2.indices[2], op1.indices[1] ]
				new_op2     = [-1, new_offset, new_indices ]
				two_bdy_op2 = operator(new_op2)
			else:
				two_bdy_op2 = operator([0])
			if op1.indices[1] == op2.indices[1]:
				w3          = op2.offset[1] + op1.offset
				new_offset  = [ op2.offset[0],w3 ,op2.offset[2] ]
				new_indices = [ op2.indices[0], op1.indices[0], op2.indices[2], op2.indices[3] ]
				new_op3     = [+1, new_offset, new_indices ]
				two_bdy_op3 = operator(new_op3)
			else:
				two_bdy_op3 = operator([0])
			if op1.indices[0] == op2.indices[2]:
				w1          = op1.offset + op2.offset[0]
				w3          = op2.offset[1] + op1.offset
				w4          = op2.offset[2] + op1.offset
				new_offset  = [ w1, w3, w4]
				new_indices = [ op2.indices[0], op2.indices[1], op1.indices[1], op2.indices[3] ]
				new_op4     = [-1, new_offset, new_indices ]
				two_bdy_op4 = operator(new_op4)
			else:
				two_bdy_op4 = operator([0])
			result = [two_bdy_op1, two_bdy_op2, two_bdy_op3, two_bdy_op4]
		return( result )


h1 = [+c1, N, [p, q] ]
t2 = [ c2, [k, l, h], [a, b, i, j] ]

op1 = operator(h1)
op2 = operator(t2)

com2 = commutator2(op1, op2)
print(com2[0].full_op, com2[1].full_op, com2[2].full_op, com2[3].full_op)	




#j = 'j'
#b = 'b'
#t1 = [ 1, N, j, b]
#com2 = commutator( com1[1], t1)
#print(com2)
