
l = 5*[1]

def inc_list(list):
	new = 5*[list]
	return new

print(l)
print(inc_list(l))
print(inc_list( inc_list(l) ))

def nested_list(number, list):
	for i in range(number):
		list = inc_list(list)
	return list



print( nested_list(5, 1) )
print( nested_list(5, 1)[0][0][0][0][0] )
