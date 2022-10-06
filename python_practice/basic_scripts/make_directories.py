from os import mkdir

for i in range(3):
	for j in range(3):
		output_str = ''
		output_str += 'directory_{}'.format(str(i).zfill(2))
		output_str += '_{}'.format(j)
		mkdir output_str
