

for i in range(9):
     try:
         x = i+5-2*i
         y = i/x
         print(x, y)
     except ZeroDivisionError:
         print("You encounter a zero, move on!!")

