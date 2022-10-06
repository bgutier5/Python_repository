N  = 3 
c1 = 1
e  = 11
f  = 13
d  = 15
p  = 'k'
r  = 'l'
q  = 'a'
s  = 'd'

c2 = 1
k  = 2
l  = 5
h  = 7
a  = 'a'
b  = 'b'
i  = 'i'
j  = 'j'


g   = [+c1, e, f, d, p, r, q, s]
t2  = [ c2, k, l, h, a, b, i, j]


def commutator(A, B ):
	if A[0] == 0:
		operators = [0]
		return( operators )
	else:
		if A[6] == B[4]:
			w1  = A[1] + B[1] - B[3]
			w2  = A[2] + B[1] - B[3]
			w3  = A[3] + B[1] - B[3]
			g   = [ +1, w1, w2, w3, A[4], A[5], B[7], A[7] ]
			h   = [ +1, B[2], B[5], B[6] ]
			gh1 = [-1, g, h ]
		else:
			gh1 = [0]
		if A[7] == B[4]:
			w1  = B[1] - A[3] + A[1]
			w2  = B[1] - A[3] + A[2]
			w3  = B[1] - A[3]
			g   = [+1, w1, w2, w3, A[4], A[5], B[7], A[6] ]
			h   = [+1, B[2], B[5], B[6] ]
			gh2 = [+1, g, h]
		else:
			gh2 = [0]
		if A[6] == B[5]:
			w1  = B[2] - B[3] + A[1]
			w2  = B[2] - B[3] + A[2]
			w3  = B[2] - B[3] + A[3]
			g   = [+1, w1, w2, w3, A[4], A[5], B[7], A[7] ]
			h   = [+1, B[1], B[4], B[6] ]
			gh3 = [+1, g, h]
		else:
			gh3 = [0]
		if A[7] == B[5]:
			w1  = B[2] - A[3] - B[3] + A[1]
			w2  = B[2] - A[3] - B[3] + A[2]
			w3  = B[2] - A[3] - B[3] 
			g   = [+1, w1, w2, w3, A[4], A[5], B[7], A[6] ]
			h   = [+1, B[1], B[4], B[6] ]
			gh4 = [-1, g, h]
		else:
			gh4 = [0]
		if A[5] == B[7]:
			w1  = B[1]
			w2  = B[2]
			w3  = B[3] - A[2] + A[3]
			g   = [+1, w1, w2, w3, B[4], B[5], B[6], A[7] ]
			h   = [+1, A[1], A[4], A[6] ]
			gh5 = [-1, g, h]
		else:
			gh5 = [0]
		if A[4] == B[7]:
			w1  = B[1]
			w2  = B[2]
			w3  = B[3] - A[1] + A[3]
			g   = [+1, w1, w2, w3, B[4], B[5], B[6], A[7] ]
			h   = [+1, A[2], A[5], A[6] ]
			gh6 = [+1, g, h]
		else: 
			gh6 = [0]
		if A[4] == B[6]:
			w1  = A[1] - A[3] + B[1]
			w2  = A[1] - A[3] + B[2]
			w3  = A[1] - A[3] + B[3]
			g   = [+1, w1, w2, w3, B[4], B[5], A[7], B[7] ]
			h   = [+1, A[2], A[5], A[6] ]
			gh7 = [+1, g, h]
		else:
			gh7 = [0]
		if A[5] == B[6]:
			w1  = A[2] - A[3] + B[1]
			w2  = A[2] - A[3] + B[2]
			w3  = A[2] - A[3] + B[3]
			g   = [+1, w1, w2, w3, B[4], B[5], A[7], B[7] ]
			h   = [+1, A[1], A[4], A[6] ]
			gh8 = [-1, g, h]
		else:
			gh8 = [0]
		operators = [gh1, gh2, gh3, gh4, gh5, gh6, gh7, gh8]
	return(operators)

com1 = commutator(g, t2)
print(com1)


#j = 'j'
#b = 'b'
#t1 = [ 1, N, j, b]
#com2 = commutator( com1[1], t1)
#print(com2)


class operator:
	def __init__(self, parameters):
		if parameters[0] == 0:
			self.type    = 0
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
			
class composite_operator:
	def __init__(self, coeff, left_operator, right_operator):
		self.coeff             = coeff
		self.type              = "composite_operator"
		self.left_operator     = left_operator
		self.right_operator    = right_operator
		self.full_op           = [self.coeff, self.left_operator.full_op, self.right_operator.full_op]


def commutator2(op1, op2):
	if op1.type == 0 or op2.type == 0:
		result = operator([0])
	if op1.type == "composite_operator":
		com1    = commutator2(op1.right_operator, op2)
		com2    = commutator2(op1.left_operator,  op2)
		num_op1 = len(com1)
		num_op2 = len(com2)
		result  = []
		for i in range(num_op1):
			new_composite = composite_operator( +1, op1.left_operator,   com1[i]    )
			result.append(new_composite)
		for j in range(num_op2):
			new_composite = composite_operator(   +1, com2[j],   op1.right_operator )
			result.append(new_composite)
		return(result)
	if op1.type == "two body" and op2.type == "two body":
		if op1.full_op == 0:
			result = operator([0])
			return(result)
		else:
			if op1.indices[2] == op2.indices[0]:
				w1           = op1.offset[0] + op2.offset[0] - op2.offset[2]
				w2           = op1.offset[1] + op2.offset[0] - op2.offset[2]
				w3           = op1.offset[2] + op2.offset[0] - op2.offset[2]
				new_offsets  = [w1, w2, w3]
				new_2bd_indx = [op1.indices[0], op1.indices[1], op2.indices[3], op1.indices[3] ]
				new_1bd_indx = [ op2.indices[1], op2.indices[2] ]
				new_2bd_op1  = [ +1, new_offsets,   new_2bd_indx  ]
				new_1bd_op1  = [ +1, op2.offset[1], new_1bd_indx ]
				two_bdy_op1  = operator(new_2bd_op1)
				one_bdy_op1  = operator(new_1bd_op1)
				compost_op1  = composite_operator( -1, two_bdy_op1, one_bdy_op1 )  
			else:
				compost_op1 = operator([0])
			if op1.indices[3] == op2.indices[0]:
				w1            = op2.offset[0] - op1.offset[2] + op1.offset[0]
				w2            = op2.offset[0] - op1.offset[2] + op1.offset[1]
				w3            = op2.offset[0] - op1.offset[2]
				_2bdy_offsets = [w1, w2, w3]
				_2bdy_indx    = [op1.indices[0], op1.indices[1], op2.indices[3], op1.indices[2] ]
				_1bdy_indx    = [op2.indices[1], op2.indices[2] ]
				_2bdy_op2     = [+1, _2bdy_offsets, _2bdy_indx ]
				_1bdy_op2     = [+1, op2.offset[1], _1bdy_indx ]
				two_bdy_op2   = operator(_2bdy_op2)
				one_bdy_op2   = operator(_1bdy_op2)
				compost_op2   = composite_operator( +1, two_bdy_op2, one_bdy_op2 )
			else:
				compost_op2   = operator([0])
			if op1.indices[2] == op2.indices[1]:
				w1            = op2.offset[1] - op2.offset[2] + op1.offset[0]
				w2            = op2.offset[1] - op2.offset[2] + op1.offset[1]
				w3            = op2.offset[1] - op2.offset[2] + op1.offset[2]
				_2bdy_offsets = [w1, w2, w3]
				_2bdy_indx    = [op1.indices[0], op1.indices[1], op2.indices[3], op1.indices[3]]
				_1bdy_indx    = [op2.indices[0], op2.indices[2] ]
				_2bdy_op3     = [+1, _2bdy_offsets, _2bdy_indx]
				_1bdy_op3     = [+1, op2.offset[0], _1bdy_indx]
				two_bdy_op3   = operator(_2bdy_op3)
				one_bdy_op3   = operator(_1bdy_op3)
				compost_op3   = composite_operator(+1, two_bdy_op3, one_bdy_op3)
			else:
				compost_op3   = operator([0])
			if op1.indices[3] == op2.indices[1]:
				w1            =  op2.offset[1] - op1.offset[2] - op2.offset[2] + op1.offset[0]
				w2            =  op2.offset[1] - op1.offset[2] - op2.offset[2] + op1.offset[1]
				w3            =  op2.offset[1] - op1.offset[2] - op2.offset[2]
				_2bdy_offsets = [w1, w2, w3]
				_2bdy_indx    = [op1.indices[0], op1.indices[1], op2.indices[3], op1.indices[2] ]
				_1bdy_indx    = [op2.indices[0], op2.indices[2] ]
				_2bdy_op4     = [+1, _2bdy_offsets, _2bdy_indx]
				_1bdy_op4     = [+1, op2.offset[0], _1bdy_indx]
				two_bdy_op4   = operator(_2bdy_op4)
				one_bdy_op4   = operator(_1bdy_op4) 
				compost_op4   = composite_operator(-1, two_bdy_op4, one_bdy_op4)
			else:
				compost_op4   = operator([0])
			if op1.indices[1] == op2.indices[3]:
				w1            =  op2.offset[0] 
				w2            =  op2.offset[1] 
				w3            =  op2.offset[2] - op1.offset[1] + op1.offset[2]
				_2bdy_offsets = [w1, w2, w3]
				_2bdy_indx    = [op2.indices[0], op2.indices[1], op2.indices[2], op1.indices[3] ]
				_1bdy_indx    = [op1.indices[0], op1.indices[2] ]
				_2bdy_op5     = [+1, _2bdy_offsets, _2bdy_indx]
				_1bdy_op5     = [+1, op1.offset[0], _1bdy_indx]
				two_bdy_op5   = operator(_2bdy_op5)
				one_bdy_op5   = operator(_1bdy_op5)
				compost_op5   = composite_operator(-1, two_bdy_op5, one_bdy_op5)
			else:
				compost_op5   = operator([0])
			if op1.indices[0] == op2.indices[3]:
				w1            =  op2.offset[0]
				w2            =  op2.offset[1]
				w3            =  op2.offset[2] - op1.offset[0] + op1.offset[2]
				_2bdy_offsets = [w1, w2, w3]
				_2bdy_indx    = [op2.indices[0], op2.indices[1], op2.indices[2], op1.indices[3] ]
				_1bdy_indx    = [op1.indices[1], op1.indices[2] ]
				_2bdy_op6     = [+1, _2bdy_offsets, _2bdy_indx]
				_1bdy_op6     = [+1, op1.offset[1], _1bdy_indx]
				two_bdy_op6   = operator(_2bdy_op6)
				one_bdy_op6   = operator(_1bdy_op6)
				compost_op6   = composite_operator(+1, two_bdy_op6, one_bdy_op6)
			else:
				compost_op6   = operator([0])
			if op1.indices[0] == op2.indices[2]:
				w1            =  op1.offset[0] - op1.offset[2] + op2.offset[0]
				w2            =  op1.offset[0] - op1.offset[2] + op2.offset[1]
				w3            =  op1.offset[0] - op1.offset[2] + op2.offset[2]
				_2bdy_offsets = [w1, w2, w3]
				_2bdy_indx    = [op2.indices[0], op2.indices[1], op1.indices[3], op2.indices[3] ]
				_1bdy_indx    = [op1.indices[1], op1.indices[2] ]
				_2bdy_op7     = [+1, _2bdy_offsets, _2bdy_indx]
				_1bdy_op7     = [+1, op1.offset[1], _1bdy_indx]
				two_bdy_op7   = operator(_2bdy_op7)
				one_bdy_op7   = operator(_1bdy_op7)
				compost_op7   = composite_operator(+1, two_bdy_op7, one_bdy_op7)
			else:
				compost_op7   = operator([0])
			if op1.indices[1] == op2.indices[2]:
				w1            =  op1.offset[1] - op1.offset[2] + op2.offset[0]
				w2            =  op1.offset[1] - op1.offset[2] + op2.offset[1]
				w3            =  op1.offset[1] - op1.offset[2] + op2.offset[2]
				_2bdy_offsets = [w1, w2, w3]
				_2bdy_indx    = [op2.indices[0], op2.indices[1], op1.indices[3], op2.indices[3] ]
				_1bdy_indx    = [op1.indices[0], op1.indices[2] ]
				_2bdy_op8     = [+1, _2bdy_offsets, _2bdy_indx]
				_1bdy_op8     = [+1, op1.offset[0], _1bdy_indx]
				two_bdy_op8   = operator(_2bdy_op8)
				one_bdy_op8   = operator(_1bdy_op8)
				compost_op8   = composite_operator(-1, two_bdy_op8, one_bdy_op8)
			else:
				compost_op8   = operator([0])
			result = [compost_op1, compost_op2, compost_op3, compost_op4, compost_op5, compost_op6, compost_op7, compost_op8]
		return( result )
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


g   = [+c1, [e, f, d], [p, r, q, s] ]
t2  = [ c2, [k, l, h], [a, b, i, j] ]

op1 = operator(g )
op2 = operator(t2)

com2 = commutator2(op1, op2)

A = 'A'
B = 'B'
I = 'I'
J = 'J'

T2  = [ c2, [k, l, h], [A, B, I, J] ]
op3 = operator(T2)

com3 = commutator2(com2[0], op3)
print( len(com3) )
print(com3[0].full_op)

#print(com2[0].full_op, com2[1].full_op,  com2[2].full_op, com2[3].full_op, com2[4].full_op, com2[5].full_op, com2[6].full_op, com2[7].full_op)
#print(com2[1].full_op[1].full_op, com2[1].full_op[2].full_op, "Boris")
#print(com2[0].full_op[0], com2[0].full_op[1].full_op, com2[0].full_op[2].full_op)	
