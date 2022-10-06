import numpy as np

n = np.nan
newarray = np.array([2.44323e+00, 4.00000e+00, 3.11342e+05, 6.00000e+00, 3.22223e+05])
if n == np.nan:
    raise NameError('It should stop here')
newarray *= n
print(n == np.nan)
print(newarray)
