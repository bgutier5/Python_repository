mass = [1,1,1,1,1,1] 
bra = [1,5,4,7,10,22]
ket = [1,5,4,7,10,22]

def compare(bra,ket): 
 diff = []
 for i in range(len(mass)):
  if bra[i] != ket[i]:
   diff.append((i,bra[i],ket[i]))
 print(diff)
 


compare(bra,ket) 
