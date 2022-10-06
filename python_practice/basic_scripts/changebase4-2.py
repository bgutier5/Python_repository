mass = [1,1,1]
states = 3

def change_of_base(x):
 ivals = []
 while x > 0:
  ivals.append(x%states)
  x = x // states
 pad = len(mass) - len(ivals)
 ivals = ivals + [0]*pad
 return(ivals)

y = [0, 0, 0, 1]


def change_back(y):
 N = 0
 for i in range(len(y)):
  n = y[i] * (2 ** i)
  N += n
 return(N)

print(change_of_base(8))
print(change_back(change_of_base(8)))

'''
import copy

ket_string = [1, 1, 1]
ket = ket_string
up_lim = states - 1

for i in range(-1, len(ket) - 1):
 bra = copy.deepcopy(ket)
 if bra[i] < up_lim  and bra[i+1] < up_lim: 
  bra[i] = bra[i] + 1
  bra[i+1] = bra[i+1] + 1
  print(bra)

for i in range(-1, len(ket) -1):
 bra = copy.deepcopy(ket)
 if bra[i] > 0 and bra[i+1] > 0:
  bra[i] = bra[i] - 1
  bra[i+1] = bra[i+1] - 1
  print(bra) 

for i in range(-1, len(ket) - 1):
 bra = copy.deepcopy(ket)
 if bra[i] > 0 and bra[i+1] < up_lim:
  bra[i] = bra[i] - 1
  bra[i+1] = bra[i+1] + 1
  print(bra)

for i in range(-1, len(ket) - 1):
 bra = copy.deepcopy(ket)
 if bra[i] < up_lim  and bra[i+1] > 0:
  bra[i] = bra[i] + 1
  bra[i+1] = bra[i+1] - 1
  print(bra)
'''
'''
def func():
 print("Boris")

func()
'''
