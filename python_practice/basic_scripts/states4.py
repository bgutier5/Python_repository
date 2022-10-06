def baseN(num,b):
  return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

num = 11
b = 2 

mystates = baseN(num,b) 
print(int(str(mystates)[0]) + 5)
while len(mystates) <= 8:
 print(mystates)
 mystates = "0" + mystates  

