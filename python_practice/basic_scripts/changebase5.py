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


singles = []
for x in range(len(mass),-1,-1): 
 for y in range(states**len(mass)):
  if change_of_base(y).count(0) == x:
   singles.append(change_of_base(y))
print(singles)
print(len(singles))
print(singles[3][0])
print(len(singles[0]))
