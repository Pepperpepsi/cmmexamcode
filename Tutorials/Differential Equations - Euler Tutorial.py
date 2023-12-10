# -*- coding: utf-8 -*-
"""
CMM Differential Equations - Euler Tutorial
Created on Wed Dec  6 19:58:05 2023

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

### Euler
# Number of steps
n_step = math.ceil(x_final/h)

# Definition of arrays to store the solution
y_eul = np.zeros(n_step+1)
x_eul = np.zeros(n_step+1)

# Initialize first element of solution arrays with IC
y_eul[0] = y0
x_eul[0] = x0 

# Populate the x array
for i in range(n_step):
    x_eul[i+1]  = x_eul[i]  + h

# Apply Euler method n_step times
for i in range(n_step):
    # compute the slope using the differential equation
    slope = model(y_eul[i],x_eul[i]) 
    # use the Euler method
    y_eul[i+1] = y_eul[i] + h * slope  

# Exact Solution Storage Array
n_exact = 1000
x_exact = np.linspace(0,x_final,n_exact+1) 
y_exact = np.zeros(n_exact+1)

# Exact Sol
for i in range(n_exact+1):
    y_exact[i] = math.exp(x_exact[i]-4)/(math.exp(x_exact[i]-4)+1)


### Result Print
print ('Solution: step x y-eul y-exact error%')
for i in range(n_step+1):
    print("Step: ", i,"x: ", x_eul[i], "Euler Sol: ", y_eul[i],"Exact Sol: ", math.exp(x_exact[i]-4)/(math.exp(x_exact[i]-4)+1),
            "% Error: ", (y_eul[i]- math.exp(x_exact[i]-4)/(math.exp(x_exact[i]-4)+1))/ 
            (math.exp(x_exact[i]-4)/(math.exp(x_exact[i]-4)+1)) * 100)

"""
# print results in a text file (for later use if needed)
file_name= 'output_h' + str(h) + '.dat' 
f_io = open(file_name,'w') 
for i in range(n_step+1):
    s1 = str(i)
    s2 = str(x_eul[i])
    s3 = str(y_eul[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()
"""

### Plot
plt.figure()
plt.plot(x_eul, y_eul, 'b.-', label = "Euler")
plt.plot(x_exact,y_exact, "r-",  label = "Ex")
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.show()
# ------------------------------------------------------