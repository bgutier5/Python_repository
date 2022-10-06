mass = [1,1,1]
states = 3
s = 11
p = 0
if s == 0:
 ivals = [0]*len(mass)
 print(ivals)
p += 1

for i in range(len(mass)):
 for l in range(1, states):
  if p == s: 
   ivals = [0]*len(mass)
   ivals[i] = l
   ivals.reverse()
   print(ivals)
  p += 1

for j in range(len(mass)):
 for i in range(j+1,len(mass)): 
  for l in range(1, states):
   for m in range(1, states):
    if p == s:
     ivals = [0]*len(mass) 
     ivals[i] = l
     ivals[j] = m
     ivals.reverse()
     print(ivals)
    p += 1

