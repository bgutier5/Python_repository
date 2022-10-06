def gen_name(i):
	output_str = ""
	output_str = "r_data_{}.txt".format(i)
	return(output_str)

def func1(i,j):
	output_str  = ""
	output_str += "Boris {},".format(i)
	output_str += "{}\n".format(j)
	output_str += "\n"
	output_str += "\n"
	output_str += "missed two lines"
	return(output_str)

dim = 4
for i in range(dim):
	for j in range(dim):
	 f = open(gen_name(i), 'a')
	 f.write( func1(i,j) )
	 f.close()

