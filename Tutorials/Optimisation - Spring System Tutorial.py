# -*- coding: utf-8 -*-
"""
CMM Optimisation - Spring System Tutorial
Created on Fri Dec  8 14:48:19 2023

@author: otmha
"""


# Calculate displacement of point (x1,x2) that minimises potential energy of spring system

# Imports
import numpy as np
import matplotlib.pyplot as plt
import sympy

# Variables
ka = 9 #N/cm
kb = 2 #N/cm
La = 10 #cm
Lb = 10 #cm
F1 = 2 #N
F2 = 4 #N
x1p = np.linspace(-10,10, 1000)
x2p = np.linspace(-10,10, 1000)
x1, x2 = np.meshgrid(x1p, x2p, indexing = "ij")

# Given function
PE = 0.5*ka*((x1**2 + (La - x2)**2)**0.5 - La)**2 + 0.5*kb*((x1**2 + (Lb + x2)**2)**0.5 - Lb)**2 - F1*x1 - F2*x2
# If the function was less annoying, you could use Newton Twodimensional Optimisation.py

# Visualise
plt.figure()
plt.contour(x1,x2,PE,100)
plt.colorbar()
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()


# Newton
x,y = sympy.symbols("x,y")
from sympy.utilities.lambdify import lambdify
from sympy import symbols, Matrix, Function, simplify, exp, hessian, solve, init_printing
init_printing()

X = Matrix([x,y])
f = Matrix([0.5*(ka*((x**2+(La-y)**2)**0.5 - La)**2)+0.5*(kb*((x**2+(Lb+y)**2)**0.5 - Lb)**2)-F1*x-F2*y])
print(np.shape(f))

gradf = simplify(f.jacobian(X)).transpose()
fgradf = lambdify([x,y],gradf)

hessianf = simplify(hessian(f,X))
fhessianf = lambdify([x,y], hessianf)

def Newton_Raphson_Optimize(Grad, Hess, x,y, epsilon=0.000001, nMax = 200):
    #Initialization
    i = 0
    iter_x, iter_y, iter_count = np.empty(0),np.empty(0), np.empty(0)
    error = 10
    X = np.array([x,y])

    #Looping as long as error is greater than epsilon
    while np.linalg.norm(error) > epsilon and i < nMax:
        i +=1
        iter_x = np.append(iter_x,x)
        iter_y = np.append(iter_y,y)
        iter_count = np.append(iter_count ,i)
        print(X)

        X_prev = X
        #X had dimensions (2,) while the 2nd term (2,1), so it had to be converted to 1D
        X = X - np.matmul(np.linalg.inv(Hess(x,y)), Grad(x,y)).flatten()
        error = X - X_prev
        x,y = X[0], X[1]

    return X, iter_x,iter_y, iter_count

root,iter_x,iter_y, iter_count = Newton_Raphson_Optimize(fgradf,fhessianf,1,1)
print(root)