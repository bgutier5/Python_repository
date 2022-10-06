bra = [1,5,4,7,10,22]
ket = [0,5,3,7, 8,22]
 
diff = []
for i in range(6):
 if bra[i] != ket[i]:
  diff.append((i,bra[i],ket[i]))
print(diff)
print(len(diff)) 
