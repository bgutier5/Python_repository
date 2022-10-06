mass = [1,1,1]
states = 2

def change_of_base(x):
 ivals = []
 while x > 0:
  ivals.append(x%states)
  x = x // states
 pad = len(mass) - len(ivals)
 ivals = ivals + [0]*pad
 return ivals 


singles = [] 
i = 3
print(change_of_base(i))
#print(change_of_base(i).count(0))
#if change_of_base(i).count(0) == 3:
# print(1)
#if change_of_base(i).count(0) == 2:
# print(len(mass)*(len(mass)-1)/2) 
#for i in range(5):
# singles.append(change_of_base(i))
#print(singles)
#print(singles[2][1])
