
# Python program showing  
# a use of raw_input()  
# g = input("Enter your name : ") 
# print( g )

import sys
arguments_list = sys.argv
arguments_count = len(arguments_list) - 1
print ("the script is called with {} arguments".format(arguments_count))
if arguments_count == 0 :
    print('There are no arguments given')
else:
    print('The argument is:', arguments_list[1])
