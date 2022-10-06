import numpy as np
# from tempfile import TemporaryFile
# outfile = TemporaryFile()

x = np.arange(10)
np.savetxt('array.npy', x)

# array.npy.seek(0) # Only needed here to simulate closing & reopening file
b = np.loadtxt("array.npy")

print(x == b)

