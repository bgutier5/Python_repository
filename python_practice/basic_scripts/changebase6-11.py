mass = [1,1,1]
states = 3

def change_of_base(x):
 p = 0
 if x == 0:
  ivals = [0]*len(mass)
  return(ivals)
 p += 1

 for i in range(len(mass)):
  for l in range(1, states):
   if p == x: 
    ivals = [0]*len(mass)
    ivals[i] = l
    ivals.reverse()
    return(ivals)
   p += 1

 for j in range(len(mass)):
  for i in range(j+1,len(mass)): 
   for l in range(1, states):
    for m in range(1, states):
     if p == x: 
      ivals = [0]*len(mass) 
      ivals[i] = l
      ivals[j] = m
      ivals.reverse()
      return(ivals)
     p += 1
 if p < x: 
  ivals = [0]*len(mass)
  return(ivals)

print(change_of_base(states ** len(mass)))
