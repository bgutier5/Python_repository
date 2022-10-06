import os
#
# os.system calls the linux command.

for i in range(3):
	for j in range(3):
		output_str = ''
		output_str += 'directory_{}'.format(str(i).zfill(2))
		output_str += '_{}'.format(j)
		os.system( 'mkdir ' + output_str )
		os.system( 'cp test_file.txt '  + output_str + '/' )
