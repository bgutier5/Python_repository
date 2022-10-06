def baseres(x,states):
 ivals = []
 while x > 0:
  ivals.append(x%states)
  x = x // states
 pad = states - len(ivals)
 ivals = ivals + [0]*pad
 print(ivals)
 
baseres(856,2)
baseres(0,5)
