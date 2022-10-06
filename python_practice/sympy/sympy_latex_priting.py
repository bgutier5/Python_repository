import sympy
from sympy import latex

x, n, l = sympy.symbols('x n l')
f = x**2 + 1
g = n**2 + 1
h = l**2 + 1
#print(sympy.diff(f, x))
#print(sympy.diff(g, n))
#print(sympy.diff(h, l))
print(f + g)
print(latex(f+g))

