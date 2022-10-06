
import numpy as np

m = np.array([[]])
mylist = [(2,4), (6,3), (4,5)]
for i, j in mylist:
    new = np.array([[i, j]])
    if len(m[0])  == 0:
        m = np.append(m, new, axis=1)
    else:
        m = np.append(m, new, axis=0)
print('------')
print(m)
