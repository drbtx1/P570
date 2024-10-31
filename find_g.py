# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:44:04 2024

@author: dabuch
"""

import pandas as pd
import re
import numpy as np
import random as rd
import matplotlib.pyplot as plt

filename = "C:/users/dabuch/downloads/coord14000.dat"

# Read the file line by line to understand its structure
with open(filename, 'r') as file:
    lines = file.readlines()
    print("First few lines:")
    for i, line in enumerate(lines[:5]):
        print(f"Line {i}: {line.strip()}")

# Try reading with more flexible parsing
df = pd.read_csv(filename, 
                 sep='\s+',      # One or more whitespace characters
                 engine='python', # More flexible parsing
                 header=None,    # No header row
                 error_bad_lines=False,  # Skip problematic lines
                 warn_bad_lines=True)    # Warn about skipped lines

# If the above fails, try manual parsing
import io

def clean_line(line):
    """Split line and clean whitespace"""
    return [x.strip() for x in line.split()]

# Manually parse the file, skipping problematic lines
data = []
with open(filename, 'r') as file:
    for line in file:
        try:
            # Try to parse each line
            parts = clean_line(line)
            if len(parts) == 5:  # Ensure exactly 5 columns
                data.append(parts)
        except Exception as e:
            print(f"Skipping problematic line: {line.strip()}")

# Create DataFrame from parsed data
df = pd.DataFrame(data, columns=['run', 'molecule', 'x', 'y', 'z'])

# Convert columns to appropriate types if needed
df['run'] = pd.to_numeric(df['run'], errors='coerce')
df['x'] = pd.to_numeric(df['x'], errors='coerce')
df['y'] = pd.to_numeric(df['y'], errors='coerce')
df['z'] = pd.to_numeric(df['z'], errors='coerce')

# Remove rows with missing x values
df_cleaned = df[df['x'].notna()]
display(df_cleaned)


#determine how far to find g, find wall closest to origin 
Max = max(df_cleaned["x"].max(), df_cleaned["y"].max(), df_cleaned["z"].max())
Min = min(df_cleaned["x"].min(), df_cleaned["y"].min(), df_cleaned["z"].min())
Range = max(Max, np.abs(Min))
print(Range)
L2 = 3*Range**2
L = L2**(0.5)
print(L) 
step = 0.01

center_atom = rd.randint(0,len(df_cleaned))
print(center_atom) 
distance_to_center_atom = []
centervalues = df_cleaned.iloc[center_atom]
display(centervalues)
while(abs(centervalues["x"]) > Range/3 or abs(centervalues["y"]) > Range/3 or abs(centervalues["z"]) > Range/3):
    center_atom = rd.randint(0,len(df_cleaned))
    print(center_atom) 
    centervalues = df_cleaned.iloc[center_atom]
    display(centervalues)
    
#max_distance = min(abs(Range - abs(centervalues["x"])), abs(Range - abs(centervalues["y"])), abs(Range - abs(centervalues["z"])))
#print(max_distance)

for atom in range(0, len(df_cleaned) ):
    atom_values =  df_cleaned.iloc[atom]
    distance_to_center_atom.append(np.sqrt((centervalues["x"] - atom_values["x"])**2 + 
                                           (centervalues["y"] - atom_values["y"])**2 +
                                           (centervalues["z"] - atom_values["z"])**2))
print(distance_to_center_atom)    
R = []
for r in np.arange(step, max(distance_to_center_atom), step):
    R.append(r)
print(R) 

neighbors = []
for distance in R:
    sum = 0
    for atom in distance_to_center_atom:
        if atom < distance:
            sum += 1
    neighbors.append(sum - 1)   #account for center atom

print(neighbors)   

g = []

for r in R:
    volume = 4*np.pi*(r**3)/3
    g.append(neighbors[R.index(r)]/volume)     
print(g)    

plt.plot(R,g)
plt.show()