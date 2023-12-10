# -*- coding: utf-8 -*-
"""
CMM Regression Tutorial 4
Created on Mon Dec  4 16:09:48 2023

@author: otmha
"""
### Linear Regression
import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.array([0.    ,     0.06666667, 0.13333333, 0.2   ,     0.26666667, 0.33333333,
     0.4   ,     0.46666667, 0.53333333, 0.6   ,     0.66666667, 0.73333333,
     0.8   ,     0.86666667, 0.93333333, 1.    ,    ])

y = np.array([2.17312991, 2.19988829, 2.33988149, 2.33940595, 2.41968027, 2.99955891,
     3.04855788, 3.86631749, 3.66009775, 4.42305111, 4.22747852, 4.11717969,
     3.87539822, 4.53121841, 5.52211102, 5.30792203])

# Preview plot
plt.scatter(x,y)
plt.xlabel("x")
plt.ylabel("y")

# 50 points spaced between 0 and 1
x_fit = np.linspace(0, 1, 50)
# Linear Regression with Least Squares
n = len(x)

a1 = ((n*np.sum(x*y) - np.sum(x)*np.sum(y))/(n*np.sum(x**2)-np.sum(x)**2))
a0 = np.mean(y) - a1*np.mean(x)

print("gradient and intercept: ", a1, a0)
lin_reg = a0 + a1*x_fit

# Add regression
plt.plot(x_fit, lin_reg, "b")



### Alternatively
coefficients = np.polyfit(x,y,1) #1 indicates first order
lin_function = np.poly1d(coefficients) #Generate linear function for fit
poly_reg = lin_function(x_fit) #Evaluate regression at points

plt.figure()
plt.plot(x,y, "rh", ms = 5)
plt.plot(x_fit, poly_reg, "r-")
plt.xlabel("x")
plt.ylabel("y")
plt.show()