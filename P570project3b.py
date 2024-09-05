# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:23:20 2024

@author: dbtx
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

g = 0.5
H = np.array([[1j*g, -1], [-1, -1j*g]])

evalues, evectors = np.linalg.eig(H)
#print(evalues)
#print(evectors)

D = np.array([[evalues[0], 0],[0,evalues[1]]])
#print(D)

time = []
U = []
V = evectors
X = []
psi_0 = np.array([1,0]).T

for t in np.arange(0,10, 0.01):
    time.append(t)
    #U.append(scipy.linalg.expm(-1j*D*t))
    X.append(np.matmul(V,np.matmul(scipy.linalg.expm(-1j*D*t),np.linalg.inv(V))))
    
#print(U)
psi = []

for t in time:
    psi.append(np.matmul(X, psi_0))
print(psi)    
    

    

