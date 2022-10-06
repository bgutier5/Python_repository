import sympy
from sympy import nsimplify, integrate, exp, oo

x = sympy.symbols('x')

# test integration
print(integrate(exp(-x), (x, 0, oo)))


a_string = "abc"

fixed_string = "{0:>5}".format(a_string)

print(fixed_string)
