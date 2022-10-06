wavelength = 1e-10
mass       = 1.67252e-27
h          = 6.62606e-34
Ep         = 5e-21

E_kinetic = ( 1/(2*mass) )*(h/wavelength)**2
print(E_kinetic)

delta_E = E_kinetic - Ep
print(delta_E)

new_wav_lenght = (  (1/(2*mass)  )*( (h**2)/delta_E ) )**0.5
print(new_wav_lenght)

result = (1/( (1/wavelength**2) - ( (2*mass*Ep)/(h**2) )  ) )**0.5
print(result)
