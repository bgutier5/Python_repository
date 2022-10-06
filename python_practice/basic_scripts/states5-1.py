def baseN(num,b):
  return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

for i in range(5):
  mystates = baseN(i,2)
  print(mystates)
  while len(mystates) < 8:
#   print(mystates)
   mystates = "0" + mystates  
  print(mystates)
