mass = [1,1,1]
states = 3

for i in range(len(mass)):
 for l in range(1, states):
  ivals = [0]*len(mass)
  ivals[i] = l
  print(ivals)

for j in range(len(mass)):
 for i in range(j+1,len(mass)):
  ivals = [0]*len(mass) 
  for l in range(1, states):
   for m in range(1, states): 
    ivals[i] = l
    ivals[j] = m
    print(ivals)
