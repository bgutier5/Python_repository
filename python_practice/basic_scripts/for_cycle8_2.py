from interruptingcow import timeout 


for j in range(3,7):
	for i in range(3,7):	
		if j != 3 or i > 4:
			l = [j, i]
			if j ==  5 and i == 3:
			 print("I skipped [5,3]")
			 pass
			else:
			 print(l)
