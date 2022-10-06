import numpy as np
import matplotlib.pyplot as plt

# time function
t_values = np.linspace(0,100, 1000)
n=8
f1 = (1/n)*np.cos(t_values)    + (2/n)*np.cos(2*t_values)  + (1/n)* np.cos(3*t_values) 
f2 = (3/24)*np.cos(7*t_values) + (3/24)*np.cos(8*t_values) + (1/24)*np.cos(9*t_values) 
f3 = (1/6)*np.cos(15*t_values)
f_t = f1 + f2 + f3
time_coef = 10
A   = np.exp(-t_values/time_coef)
y_values = A*f_t

# freq function
freq = np.fft.fftfreq(len(t_values))
FFT_yvalues = np.fft.fft(y_values)


#plt.plot(t_values, y_values) # time function
plt.plot(freq, FFT_yvalues)
plt.ylabel('some numbers')
plt.show()
