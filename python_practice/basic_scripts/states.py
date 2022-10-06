import numpy

def baseN(num,b):
  return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])
  mystates = baseN(num,b) 
  while len(mystates) <= 8:
    print(mystates)
    mystates = "0" + mystates  
print(baseN(5,2))
