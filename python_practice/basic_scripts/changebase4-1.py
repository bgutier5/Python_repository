mass = [1,1,1]
states = 2

def change_of_base(x):
 ivals = []
 while x > 0:
  ivals.append(x%states)
  x = x // states
 pad = len(mass) - len(ivals)
 ivals = ivals + [0]*pad
 return(ivals)

print(change_of_base(8))
