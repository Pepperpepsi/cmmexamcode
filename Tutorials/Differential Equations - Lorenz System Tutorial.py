# -*- coding: utf-8 -*-
"""
CMM Differential Lorenz System Tutorial
Created on Wed Dec  6 22:39:18 2023

@author: otmha
"""


### Edward Lorenz Atmospheric Fluid Dynamics System
# dy1/dt = sigma*(y2 - y1)
# dy2/dt = rho*y1 - y2 - y1*y3
# dy3/dt = -beta*y3 + y1*y2

# Solve For
# Interval 0 <= t <= tf where tf = 30
# Assume sigma = 10, beta = 8/3, rho = 28
# Initial Conditions y1(0)=y2(0)=y3(0)=5 at t=0
# Use solve_ip from scipy
# Plot solution in the planes y1y2 and y1y3
## one plot with y1 in the abscissa (other word for x) and y2 in the ordinate (other word for y)
## one plot with y1 in the abscissa and y3 in the ordinate
# Plot solution for the 3 variables, then for what they are equal to

### Imports
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

### Define Functions
def system(t,y): 
    sigma = 10
    beta = 8/3
    rho = 10
    y1 = y[0]
    y2 = y[1]
    y3 = y[2]
    f1 = sigma*(y2 - y1)
    f2 = rho*y1 - y2 - y1*y3
    f3 = -beta*y3 + y1*y2
    return [f1, f2, f3]

# Initial Conditions
y01 = 5
y02 = 5
y03 = 5
t0 = 0
# Interval
t_final = 30

### Solve
t_eval = np.linspace(0, t_final, num = 5000)
y = solve_ivp(system, [0, t_final], [y01, y02, y03], t_eval = t_eval)

### Plot
# y.t = contains time instants at which sol has been stored
# y.y = constains 2d array with sol
## first index indicates component of solution y1 y2 y3
## second index is time instant
plt.figure(1)
plt.plot(y.t,y.y[0,:] , 'b.', label = "y1 sol")
plt.plot(y.t,y.y[1,:] , 'r-.', label = "y2 sol")
plt.plot(y.t,y.y[2,:] , 'g-', label = "y3 sol")
plt.xlabel('x')
plt.ylabel('y_1(x), y_2(x), y_3(x)')
plt.legend()

### Abscissa and Ordinate Plots
plt.figure(2)
plt.plot(y.y[0,:], y.y[1,:], 'r-.', label = "sol")
plt.xlabel('y_1(x)')
plt.ylabel('y_2(x)')
plt.legend()

plt.figure(3)
plt.plot(y.y[0,:], y.y[2,:], 'b-.', label = "sol")
plt.xlabel('y_1(x)')
plt.ylabel('y_3(x)')
plt.legend()

plt.show()


"""
# print results in a text file (for later use if needed)
file_name= 'output.dat' 
f_io = open(file_name,'w') 
n_step = len(y.t)
for i in range(n_step):
    s1 = str(i)
    s2 = str(y.t[i])
    s3 = str(y.y[0,i])
    s4 = str(y.y[1,i])
    s_tot = s1 + ' ' + s2 + ' ' + s3  + ' ' + s4
    f_io.write(s_tot + '\n')
f_io.close()
"""