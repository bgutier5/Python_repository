# Read in the file
#filedata = None

with open('param_3.py', 'r') as file :
  filedata = file.read()

# Replace the states
filedata = filedata.replace('oscillator = 3', 'oscillator = 4')

# Replace the Oscillators
filedata = filedata.replace('oscillators = 3', 'oscillators = 4')

# Write the file out again
with open('param_3.py', 'w') as file:
  file.write(filedata)
