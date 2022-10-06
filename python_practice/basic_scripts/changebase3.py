mass = [1,1,1]
states = 2

def change_of_base(x,length):
 ivals = []
 while x > 0:
  ivals.append(x%states)
  x = x // states
 pad = length - len(ivals)
 ivals = ivals + [0]*pad
 print(ivals)
 
change_of_base(856,2)
change_of_base(0,6)
change_of_base(7,len(mass))
