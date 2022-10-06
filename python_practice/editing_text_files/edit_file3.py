# Read in the file
#filedata = None

with open('param_4.py', 'r') as file :
  filedata = file.read()

for i in range(2):
	string = i
	filedata = filedata.replace('1', '2')

# Write the file out again
with open('param_4.py', 'w') as file:
  file.write(filedata)
exec(open("/home/boris/Research/practice/param_4.py").read(), globals())
