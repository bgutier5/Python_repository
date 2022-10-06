class one_body_op:
	def __init__(self, coef): 
		self.list = [coef]
	def __call__(self, variable):
		self.variable = variable
	def spacial_boris_func(x, y):
		return(x+y)

op = one_body_op(2)
op('boris')
#op.operation_func(3+4)

methods_list = [method_name for method_name in dir(op) if callable(getattr(op, method_name))]

print(op.variable, "lists")
print(methods_list)
