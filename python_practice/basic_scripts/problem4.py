from math import pi

h = 6.62606e-34
c = 2.99792458e10
m1 = 12.000000
m2 = 15.994915
uma_kg = 1.660539e-27
B0 = 1.9314
B1 = 1.6116
B_rv = 1.91375
m_eff = m1*m2/(m1+m2)

#r0 = (h/(8*(pi**2)*c*m_eff *uma_kg*B0) )**0.5
#r1 = (h/(8*(pi**2)*c*m_eff *uma_kg*B1) )**0.5
r2 = (h/(8*(pi**2)*c*m_eff *uma_kg*B_rv) )**0.5

print(r2)
#print(r1)
#k = m_eff*uma_kg*(2*pi*c*2143.26)**2
#print(k)
