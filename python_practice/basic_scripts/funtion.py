#file that contains fuctions

def my_func1():
 print("Boris")

def my_func2(x):
 y = x*3
 return(y)

def factorial(n):
    if n == 1:
        return 1
    else:
        print( n )
        return n * factorial(n-1)

print( factorial(5) )
