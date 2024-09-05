# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:22:37 2024

@author: dbtx
"""

import numpy as np
import matplotlib.pyplot as plt

x = [1]
y = [0]
I_x = [1]
I_y = [0]

prev_x = x[0]
prev_y = y[0]
time_array = [0]
step = 0.01
max_time = 10
g = 0.5

for time in np.arange(time_array[0] + step, max_time, step):
    next_x = prev_x - 1j*step*(1j*g*prev_x - prev_y)
    next_y = prev_y - 1j*step*(-prev_x - 1j*g*prev_y)
    x.append(next_x)
    y.append(next_y)
    I_x.append(next_x*np.conj(next_x))
    I_y.append(next_y*np.conj(next_y))
    time_array.append(time)
    prev_x= next_x
    prev_y = next_y
    
plt.plot(time_array, I_x)
plt.plot(time_array, I_y)
plt.show()    
    

