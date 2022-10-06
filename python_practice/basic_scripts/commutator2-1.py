c1 = 1
N  = 3
p  = 'p'
r  = 'r'
q  = 'a'
s  = 's'

c2 = 1
k  = 2
l  = 5
h  = 7
a  = 'a'
b  = 'b'
i  = 'i'
j  = 'j'


g   = [+c1, k, l, h, p, r, q, s]
t1  = [ c2, N, a, i]


def commutator(A, B ):
	if A[0] == 0:
		operators = [0]
		return( operators )
	else:
		w1 = A[1] + B[1]
		w2 = A[2] + B[1]
		w3 = A[3] - B[1]
		w4 = A[3] + B[1]
		if A[4] == B[3]:
			g1 = [-1, w1, A[2], A[3], B[2], A[5], A[6], A[7] ]
		else:
			g1 = [0]
		if A[5] == B[3]:
			g2 = [-1, A[1], w2, A[3], A[4], B[2], A[6], A[7] ]
		else:
			g2 = [0]
		if A[7] == B[2]:
			g3 = [+1, A[1], A[2], w3, A[4], A[5], A[6], B[3] ]
		else:
			g3 = [0]
		if A[6] == B[2]:
			g4 = [+1, w1, w2, w4, A[4], A[5], B[3], A[7]]
		else:
			g4 = [0] 
		operators = [g1, g2, g3, g4]
	return(operators)

com1 = commutator(g, t1)
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
	if op1.type == "two body" and op2.type == "one body":
		if op1.full_op == 0:
			result = operator([0])
			return(result)
		else:
			if op1.indices[0] == op2.indices[1]:
				w1          = op1.offset[0] + op2.offset
				new_offset  = [w1, op1.offset[1], op1.offset[2] ]
				new_indices = [op2.indices[0], op1.indices[1], op1.indices[2], op1.indices[3] ]
				new_op1     = [-1, new_offset, new_indices ]
				two_bdy_op1 = operator(new_op1)
			else:
				two_bdy_op1 = operator([0])
			if op1.indices[3] == op2.indices[0]:
				w3          = op1.offset[2] - op2.offset
				new_offset  = [ op1.offset[0], op1.offset[1], w3 ]
				new_indices = [ op1.indices[0], op1.indices[1], op1.indices[2], op2.indices[1] ]
				new_op2     = [+1, new_offset, new_indices ]
				two_bdy_op2 = operator(new_op2)
			else:
				two_bdy_op2 = operator([0])
			if op1.indices[1] == op2.indices[1]:
				w2          = op1.offset[1] + op2.offset
				new_offset  = [ op1.offset[0],w2 ,op1.offset[2] ]
				new_indices = [ op1.indices[0], op2.indices[0], op1.indices[2], op1.indices[3] ]
				new_op3     = [-1, new_offset, new_indices ]
				two_bdy_op3 = operator(new_op3)
			else:
				two_bdy_op3 = operator([0])
			if op1.indices[2] == op2.indices[0]:
				w1          = op1.offset[0] + op2.offset
				w2          = op1.offset[1] + op2.offset
				w4          = op1.offset[2] + op2.offset
				new_offset  = [ w1, w2, w4]
				new_indices = [ op1.indices[0], op1.indices[1], op2.indices[1], op1.indices[3] ]
				new_op4     = [+1, new_offset, new_indices ]
				two_bdy_op4 = operator(new_op4)
			else:
				two_bdy_op4 = operator([0])
			result = [two_bdy_op1, two_bdy_op2, two_bdy_op3, two_bdy_op4]
		return( result )

#h1 = [+c1, N, [p, q] ]
#t2 = [ c2, [k, l, h], [a, b, i, j] ]

g  = [c1, [k, l, h], [p, r, q, s]]
t1 = [c1, N, [a, i]]


op1 = operator(g)
op2 = operator(t1)

com2 = commutator2(op1, op2)
print(com2[0].full_op, com2[1].full_op, com2[2].full_op, com2[3].full_op) 	




#j = 'j'
#b = 'b'
#j = 'j'
#b = 'b'
#t1 = [ 1, N, j, b]
#com2 = commutator( com1[1], t1)
#print(com2)
