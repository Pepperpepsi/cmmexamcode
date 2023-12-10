# -*- coding: utf-8 -*-
"""
CMM Gauss Elimination Tutorial 5
Created on Tue Dec  5 17:41:49 2023

@author: otmha
"""


### Cord Tension in Tandem Team of Parachutists

# Parachutists conencted by weightless chord, free falling v = 5 m/s
v = 5
g = 9.81
# Parachutist 1 (bottom), 70 kg, drag coefficient 10 kg/s
m1 = 70
c1 = 10
# Parachutist 2 (middle), 60 kg, drag coefficient 14 kg/s
m2 = 60
c2 = 14
# Parachutist 3 (top), 40 kg, drag coefficient 17 kg/s
m3 = 40
c3 = 17

# Use FBD, express drag force as ci*v
## P1 experiences downwards gravity, upwards drag and tension
## P2 experiences downwards gravity and tension, upwards drag and other tension
## P3 experiences downwards gravity and other tension, upwards drag
# Resulting system

"""
m1*g - T - c1*v = m1*a
m2*g + T - c2*v - R = m2*a
m3*g - c3*v + R = m3*a

[70 1 0    {a     {m1*g-c1*v
 60 -1 1    T  =   m2*g - c2*v
 40 0 -1]   R}     m3*g - c3*v}
"""

import numpy as np

# returns a, T, R in case of parachute, based on above set up
def linearsolver(A,b):
    n = len(A)

    #Initialise solution vector as an empty array
    x = np.zeros(n)

    #Join A and use concatenate to form an augmented coefficient matrix
    M = np.concatenate((A,b.T), axis=1)

    for k in range(n):
        for i in range(k,n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[[k,i]] = M[[i,k]]
            else:
                pass
                for j in range(k+1,n):
                    q = M[j][k] / M[k][k]
                    for m in range(n+1):
                        M[j][m] +=  -q * M[k][m]

    #Python starts indexing with 0, so the last element is n-1
    x[n-1] =M[n-1][n]/M[n-1][n-1]

    #We need to start at n-2, because of Python indexing
    for i in range (n-2,-1,-1):
        z = M[i][n]
        for j in range(i+1,n):
            z = z  - M[i][j]*x[j]
        x[i] = z/M[i][i]

    return x

# A array for masses and chord directions
A=np.array([[70., 1., 0],[60., -1., 1.], [40, 0, -1]])
# B array for the difference between mg and cv
b=np.array([[636.7, 518.6, 307.4]])
print(linearsolver(A,b))