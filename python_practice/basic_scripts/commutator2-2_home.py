c1 = 1
e  = 11
f  = 13
d  = 15
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

N  = 3
q  = 'q'
i  = 'i'
a  = 'a'
c1 = 1
c2 = 1

g =[+c1, e, f, d, p, r, q, s]
t2  = [ c2, k, l, h, a, b, i, j]


def commutator (A, B):
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
		self.coeff    = coeff
		self.type     = "composite_operator"
		self.left_op  = left_operator
		self.right_op = right_operator
		self.full_op  = [self.coeff, left_operator, right_operator]


def commutator2(op1, op2):
	if op1.full_op[0] == 0:
		result = operator([0])
		return(result)
	'''
	if op1.type == "composite_operator":
		com1    = commutator2(op1.right_op, op2)
		com2    = commutator2(op1.left_op,  op2)
		num_op1 = len(com1)
		num_op1 = len(com2)
		result  = []
		for i in range(num_op1):
			new_composite = composite_operator( op1.left_op,   com1[i]    )
			result.append(new_composite)
		for j in range(num_op2):
			new_composite = composite_operator(   com2[j],   op1.right_op )
			result.append(new_composite)
		return(result)
	'''
	if op1.type == "two body" and op2.type == "two body":
		if op1.indices[2] == op2.indices[0]:
			w1           = op1.offset[0] + op2.offset[0] - op2.offset[2]
			w2           = op1.offset[1] + op2.offset[0] - op2.offset[2]
			w3           = op1.offset[2] + op2.offset[0] - op2.offset[2]
			new_offsets  = [w1, w2, w3]
			new_2bd_indx = [op1.indices[0], op1.indices[1], op2.indices[3], op1.indices[3] ]
			new_1bd_indx = [ op2.indices[1], op2.indices[2] ]
			new_2bd_op1  = [ +1, new_offsets,   new_2bd_indx  ]
			new_1bd_op1  = [ +1, op2.offset[1], new_1bd_indx ]
			print(new_1bd_op1, "new Boris")
			two_bdy_op1  = operator(new_2bd_op1)
			one_bdy_op1  = operator(new_1bd_op1)
			compost_op1  = composite_operator( -1, two_bdy_op1, one_bdy_op1 )  
		else:
			compost_op1 = operator([0])
		result = [compost_op1]
	return( result )

k = 'k'
l = 'l'
c = 'c'
d = 'd'


g   = [+c1, [e, f, d], [k, l, c, d] ]
h   = [ c1, N, p, q]
t2  = [ c2, [k, l, h], [a, b, i, j] ]
t1  = [ c2, N, a, i]

op1 = operator(g )
op2 = operator(t2)

'''
op3 = operator(h)
op4 = operator(t1)

compost1 = composite_operator(-1, op1, op3)
com3     = commutator2(compost1, op4)
print(com3)
'''

com2 = commutator2(op1, op2)
print(com2[0].full_op[0], com2[0].full_op[1].full_op, com2[0].full_op[2].full_op)	
