
variable = 1
global_v = 3.5

def use_this_func(variable):
   if global_v == 3.5:
       global_v = 2.0 # <--- you cannot change the value of a global variable inside a function
   return variable + global_v

#print(use_this_func(variable))
if __name__ == "__main__":
    print(use_this_func(variable)) 
