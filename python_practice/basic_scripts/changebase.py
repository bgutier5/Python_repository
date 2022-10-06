def baseres(x,length):
 ivals = []
 while x > 0:
  ivals.append(x%2)
  x = x // 2
 pad = length - len(ivals)
 ivals = ivals + [0]*pad
 print(ivals)
 
baseres(856,2)
baseres(0,2)
