from decimal import Decimal

def fexp(number):
    (sign, digits, exponent) = Decimal(number).as_tuple()
    return len(digits) + exponent - 1

def fman(number):
    return Decimal(number).scaleb(-fexp(number)).normalize()

variable = 1.423e-9
print(variable)
print(fexp(variable))
print(fman(variable))
print(variable/float(fman(variable)))
