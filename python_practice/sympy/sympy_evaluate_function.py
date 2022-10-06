import sympy

x = sympy.symbols('x')

# test function
h = x**2+x+3
print(h.subs(x,2), '<--  evaluating function')
