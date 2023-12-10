# -*- coding: utf-8 -*-
"""
CMM Integration, Error, and Plot Tutorial
Created on Thu Dec  7 16:11:04 2023

@author: otmha
"""


# Compare analytical value with technique values
# Calculate true relative error for each technique for same number of integration intervals
# Plot evolution of the integral value as function of the number of integration intervals for each technique

import matplotlib.pyplot as plt
import sys
sys.path.append("C:/Users/otmha/Desktop/CMM/Examples")
import Integration_MidTrapSimp_Tutorial as inttech

# Function
def f(x):
    return x**2 + 4*x - 12

# Integral of Function, manually defined
def integral_f(x):
    return (1/3)*x**3 + 2*x**2 - 12*x

# Interval and Max Subdivisions
a = -10
b = 10
n = 200

# Definite Integral Calculation
Definite_Integral = integral_f(b) - integral_f(a)

# Storage Arrays
x = []
rectangle = []
ra_error = []
rr_error = []
trapezoid = []
ta_error = []
tr_error = []
simpson = []
sa_error = []
sr_error = []
simpson38 = []
s38a_error = []
s38r_error = []

# Program

for n in range(2,n,2): # simpson's rule requires even number
    x.append(n)
    
    rectangle.append(inttech.rectangle_rule(f, a, b, n))
    ra_error.append(inttech.rectangle_rule(f, a, b, n) - Definite_Integral)
    rr_error.append(100*(inttech.rectangle_rule(f, a, b, n) - Definite_Integral)/Definite_Integral)
    
    trapezoid.append(inttech.trapezoid_rule(f, a, b, n))
    ta_error.append(inttech.trapezoid_rule(f, a, b, n) - Definite_Integral)
    tr_error.append(100*(inttech.trapezoid_rule(f, a, b, n) - Definite_Integral)/Definite_Integral)
    
    simpson.append(inttech.simp_third_rule(f, a, b, n))
    sa_error.append(inttech.simp_third_rule(f, a, b, n) - Definite_Integral)
    sr_error.append(100*(inttech.simp_third_rule(f, a, b, n) - Definite_Integral)/Definite_Integral)
    
    simpson38.append(inttech.simp_three_eighth_rule(f,a,b,n))
    s38a_error.append(inttech.simp_three_eighth_rule(f,a,b,n) - Definite_Integral)
    s38r_error.append(100*(inttech.simp_three_eighth_rule(f,a,b,n) - Definite_Integral)/Definite_Integral)
    
# Plot
plt.figure()
plt.plot(x,rectangle,x,trapezoid,x,simpson,x,simpson38)
plt.legend(['MidPoint Rule','Trapezoidal','Simpson Rule','3/8 Simpson'])
plt.ylim(400,450)

plt.figure()
plt.semilogy(x,ra_error,x,ta_error,x,sa_error, x,  s38a_error)
plt.legend(['MidPoint Rule','Trapezoidal','Simpson Rule',"S38 Rule"])

plt.figure()
plt.semilogy(x,rr_error,x,tr_error,x,sr_error, x,  s38r_error)
plt.legend(['MidPoint Rule','Trapezoidal','Simpson Rule',"S38 Rule"])


plt.show()

    