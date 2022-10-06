#program that changes the base of a number to another base
#example:
# baseN(number_that_will_be_changed,new_base)

def baseN(num,b):
  return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])


baseN(9,2)
