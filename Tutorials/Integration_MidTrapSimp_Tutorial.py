# -*- coding: utf-8 -*-
"""
CMM Numerical Integration Tutorial
Created on Thu Dec  7 12:46:41 2023

@author: otmha
"""


import numpy as np

def calculate_dx(a,b,n):
    return (b-a)/float(n)

def rectangle_rule(f, a, b, n):
    total = 0.0
    dx = calculate_dx(a,b,n)
    for k in range(0,n):
        total = total + f(a + k*dx + 0.5*dx)
    return dx*total

def trapezoid_rule(f, a, b, N):
    x = np.linspace(a, b, N+1)
    y = f(x)
    y_right = y[1:]
    y_left = y[:-1]
    dx = calculate_dx(a,b,N)
    T = (dx/2) * np.sum(y_right + y_left)
    return T

def simp_third_rule(f, a, b, N):
    if N % 2 == 1:
        raise ValueError("N must be even")
    dx = calculate_dx(a,b,N)
    x = np.linspace(a,b, N+1)
    y = f(x)
    S = (dx/3)*np.sum(y[0:-1:2]+4*y[1::2]+y[2::2])
    return S

def simp_three_eighth_rule(f,a,b,N):
    dx = calculate_dx(a,b,N)
    sum = f(a) + f(b);
    for i in range(1, N):
        if i % 3 == 0 :
            sum += 2*f(a + i*dx)
        else:
            sum += 3*f(a + i*dx)
    return float((3*dx/8)*sum)
    

f = lambda x: x**2 + 4*x - 12 #function
a = -10 #lower bound
b = 10 #upper bound
n = 10000 #iterations or divisions
N = 30 #iterations or divisions, or interval limit??
# interval limit for 3/8 rule = 30


print("Rectangle rule area calculation result of: ", rectangle_rule(f,a,b,n))
print("Trapezoid rule area calculation result of: ", trapezoid_rule(f,a,b,N))
print("Simpson's 1/3 rule area calculation result of: ", simp_third_rule(f,a,b,N))
print("Simpson's 3/8 rule area calculation result of: ", simp_three_eighth_rule(f,a,b,N))