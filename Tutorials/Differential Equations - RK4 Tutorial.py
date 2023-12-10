# -*- coding: utf-8 -*-
"""
CMM Differential Equations - RK4 Tutorial
Created on Wed Dec  6 21:35:03 2023

@author: otmha
"""

### Logistic Differential Equation
# dy/dx = y(1-y)

import numpy as np
import math
import matplotlib.pyplot as plt

# Initial Conditions
x0 = 0
y0 = math.exp(-4)/(math.exp(-4)+1)

# Step Size
h = 0.01

# Solution Interval
x_final = 10

# Define ODE
def model(y,x):
    dydx = y*(1-y)
    return dydx

### RK4
# Number of steps
n_step = math.ceil(x_final/h)

# Method Solution Storage Array
y_rk = np.zeros(n_step+1)
x_rk = np.zeros(n_step+1)

# Initialize first element of solution arrays with IC
y_rk[0] = y0
x_rk[0] = x0 

# Populate the x array
for i in range(n_step):
    x_rk[i+1]  = x_rk[i]  + h

# Apply RK method n_step times
for i in range(n_step):
   
    # Compute the four slopes
    x_dummy = x_rk[i]
    y_dummy = y_rk[i]
    k1 =  model(y_dummy,x_dummy)
    
    x_dummy = x_rk[i]+h/2
    y_dummy = y_rk[i] + k1 * h/2
    k2 =  model(y_dummy,x_dummy)

    x_dummy = x_rk[i]+h/2
    y_dummy = y_rk[i] + k2 * h/2
    k3 =  model(y_dummy,x_dummy)

    x_dummy = x_rk[i]+h
    y_dummy = y_rk[i] + k3 * h
    k4 =  model(y_dummy,x_dummy)

    # compute the slope as weighted average of four slopes
    slope = 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4 

    # use the RK method
    y_rk[i+1] = y_rk[i] + h * slope  


# Exact Solution Storage Array
n_exact = 1000 # should match x_final/step size
x_exact = np.linspace(0,x_final,n_exact+1) 
y_exact = np.zeros(n_exact+1)

# Exact Solution
for i in range(n_exact+1):
    y_exact[i] = math.exp(x_exact[i]-4)/(math.exp(x_exact[i]-4)+1)

### Result Print
print ('Solution: step x y-rk y-exact error%')
for i in range(n_step+1):
    # Change based on order above
    print("step: ", i, "x: ", x_rk[i], "RK4 sol:", y_rk[i],"Exact sol: ", (math.exp(x_exact[i]-4)/(math.exp(x_exact[i]-4)+1)), "% Error: ", (y_rk[i]- math.exp(x_exact[i]-4)/(math.exp(x_exact[i]-4)+1))/(math.exp(x_exact[i]-4)/(math.exp(x_exact[i]-4)+1)) * 100)

"""
# print results in a text file (for later use if needed)
file_name= 'output_h' + str(h) + '.dat' 
f_io = open(file_name,'w') 
for i in range(n_step+1):
    s1 = str(i)
    s2 = str(x_rk[i])
    s3 = str(y_rk[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()
"""

### Plot
plt.figure()
plt.plot(x_rk, y_rk, 'b.-', label = "RK4")
plt.plot(x_exact,y_exact, "r-",  label = "Ex")
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.show()
# ------------------------------------------------------