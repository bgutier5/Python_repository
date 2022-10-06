
from test_run_program import test_run_lanczos

with open('parameters_trial2.py', 'r') as file :
  filedata = file.read()

# String that will be detected
n_HOs        =  2

# String that will be used to replace
n_HOs        =  2

for i in range(7):
	rep_string = 
	filedata = filedata.replace('mas_in', 'mas_fi')
	with open('parameters_trial2.py', 'w') as file:
		file.write(filedata)
	test_run_lanczos()	



