# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:42:03 2024

@author: dbtx
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as la
from scipy.fft import fft, fftfreq, ifft 
from pprint import pp

g = 0.5
max_time = 10
step = 0.01

H = np.array([[1j*g, -1],[-1,-1j*g]])

psi_0 = np.array([1,0]).T
psi = []
psi.append(psi_0)
I1 = []
I2 = [] 
I1norm = []
I2norm = []
time = []

 

I1.append(psi[0][0]*np.conj(psi[0][0]))
I2.append(psi[0][1]*np.conj(psi[0][1]))
I1norm.append(I1[0]/(I1[0] + I2[0]))
I2norm.append(I2[0]/(I1[0] + I2[0]))
time.append(0)

G = []
G.append(np.eye(2))


for t in np.arange(step, max_time, step):
        time.append(t)
        newG = la.expm(-1j*H*t)
        newpsi = np.matmul(newG,psi_0)
        #print(newpsi)
        G.append(newG)
        psi.append(newpsi)
        I1.append(newpsi[0]*np.conj(newpsi[0]))
        I2.append(newpsi[1]*np.conj(newpsi[1]))
        I1norm.append(newpsi[0]*np.conj(newpsi[0])/(newpsi[0]*np.conj(newpsi[0])
                                                    + newpsi[1]*np.conj(newpsi[1]))) 
        I2norm.append(newpsi[1]*np.conj(newpsi[1])/(newpsi[0]*np.conj(newpsi[0])
                                                    + newpsi[1]*np.conj(newpsi[1]))) 
        
#pp(psi)   
#print(I2)

plt.plot(time,I1norm)
plt.plot(time,I2norm)
plt.show()

'''I1normfft = fft(I1norm)
freq = fftfreq(len(I1norm),step)
#I2normfft = fft(I2norm)
plt.xlim([-1,1])
plt.plot(freq, I1normfft)
plt.show()

#print(I1normfft)'''

'''
# Number of sample points
N = len(I1norm)
# sample spacing'''
'''T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = I1norm
yf = fft(y)
xf = fftfreq(N, T)[:N//2]
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()'''  '''
plt.stem(freq, np.abs(I1norm), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, 10)

plt.subplot(122)
plt.plot(t, ifft(X), 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()'''
     