# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:21:13 2024

@author: dabuch
"""

import numpy as np  
import random
N = 8
J = 1
h = 1
PBC_vertical = True
PBC_horizontal = True
spins = np.zeros((N,N))

def hamiltonian(spins):
    energy = 0
    for y in range(0,N):
        for x in range(0,N):
            
            energy += h*spins[x][y]
            
            if x != N-1:
                energy += J*(spins[x][y])*(spins[x+1][y])
            elif PBC_horizontal == True:
                energy += J*(spins[x][y])*(spins[0][y])
                
            if y != N-1:
                energy += J*(spins[x][y])*(spins[x][y+1])
            elif PBC_vertical == True:
                energy += J*(spins[x][y])*(spins[x][0])
                    
                
            
            
           
    return energy

for width in range(0,N):
    for height in range(0,N):
        spins[height][width] = random.choice([-1,1])
        
print(spins)   
print(hamiltonian(spins)) 


        
            
            
            