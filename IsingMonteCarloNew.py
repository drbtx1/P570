# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:26:40 2024

@author: dbtx
"""



import numpy as np  
import random
import matplotlib.pyplot as plt
N = 50
J = 1
h = 1
B= 0.01 #0.3*np.log(2)
PBC_vertical = True
PBC_horizontal = True
spins = np.zeros((N,N))

def hamiltonian(spins):
    energy = 0
    for y in range(0,N):
        for x in range(0,N):
            
            energy += h*spins[y][x]
            
            if x != N-1:
                energy += J*(spins[y][x])*(spins[y][x+1])
            elif PBC_horizontal == True:
                energy += J*(spins[y][x])*(spins[y][0])
                
            if y != N-1:
                energy += J*(spins[y][x])*(spins[y+1][x])
            elif PBC_vertical == True:
                energy += J*(spins[y][x])*(spins[0][x])
    return energy


for width in range(0,N):
    for height in range(0,N):
        #spins[height][width] = random.choice([-1,1])
        spins[height][width] = 1
        
print(spins)   
#print(hamiltonian(spins)) 
startE = hamiltonian(spins)
print(startE)
step = 0
steps = [step]
E = [startE]


            
count = N**3
for turn in range(1,count):
    x = random.randrange(0,N)
    y = random.randrange(0,N)
    tempspins = spins
    tempspins[y][x] = -1*tempspins[y][x]
    oldH = hamiltonian(spins)
    newH = hamiltonian(tempspins)
    deltaE = newH - oldH 
    r = random.random()
    print(r)
    flipped = False
    if np.exp(-B*deltaE) > r:
        spins = tempspins
        flipped = True
    steps.append(turn)
    if flipped:
        E.append(newH)
    else:
        E.append(oldH)            

plt.ylim([-2*J*N**2 - h*N**2, 2*J*N**2 + h*N**2])   
plt.ylabel("Energy")
plt.xlabel("Step")     
plt.plot(steps,E)
plt.show() 

energyvalues = []
cutoff = int((N**3)/5)
for energyvalue in range(-2*J*N**2 - h*N**2, 2*J*N**2 + h*N**2 + 1):
    energyvalues.append(energyvalue)
energycount = np.zeros(len(energyvalues))
for e in E[cutoff:]:
    energycount[int(e + 2*J*N**2 + h*N**2)] += 1
    
    
plt.xlabel("Energy")
plt.ylabel("Count")     
plt.plot(energyvalues,energycount)
plt.show()   
    
    
    
    
           
        
        
             
        
        
        