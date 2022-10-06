#inputs reduced in number
states = 2
mass = [1,1,1,1,1,1,1,1]

def baseN(num,b):
  return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

for i in range(5):
  mystates = baseN(i,states)
  print(mystates)
  while len(mystates) <= len(mass):
#  print(mystates)
   mystates = "0" + mystates  
  print(int(str(mystates)[8]) + 0.5)
