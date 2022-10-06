bra = "001"
ket = "111"
for i in range(3):
 if bra[-i] == ket[-i]:
  print("equal")
 else:
  print("different") 
