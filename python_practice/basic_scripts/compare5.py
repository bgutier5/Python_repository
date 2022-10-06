mass = [1,1,1,1,1,1] 
bra = [1,5,4,7,11,22]
ket = [1,5,3,7,10,22]

def compare(bra,ket): 
 diff = []
 for i in range(len(mass)):
  if bra[i] != ket[i]:
   diff.append((i,bra[i],ket[i]))
 return(diff)
 


print(compare(bra,ket)) 
#print(compare(bra,ket)[0][1] - compare(bra,ket)[0][2])
#print(compare(bra,ket)[1][1] - compare(bra,ket)[1][2])
for i in range(2):
 if abs(compare(bra,ket)[i][1] - compare(bra,ket)[i][2]) == 1:
  print(abs(compare(bra,ket)[i][1] - compare(bra,ket)[i][2])) 
