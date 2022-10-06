
from test_run_program import test_run_lanczos

with open('parameters_trial2.py', 'r') as file :
  filedata = file.read()

# String that will be detected
mas_in   = []

# String that will be used to replace
mas_fi  = [1]

for i in range(7):
	mas_in.append(1)
	mas_fi.append(1)
	str(mas_in)
	str(mas_fi)
	filedata = filedata.replace('mas_in', 'mas_fi')
	with open('parameters_trial2.py', 'w') as file:
		file.write(filedata)
	test_run_lanczos()	



