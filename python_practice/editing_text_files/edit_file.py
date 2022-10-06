# Read in the file
#filedata = None

with open('textfile2.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('This', 'this')

# Write the file out again
with open('textfile2.txt', 'w') as file:
  file.write(filedata)
