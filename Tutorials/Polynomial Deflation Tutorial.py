# -*- coding: utf-8 -*-
"""
CMM Polynomial Deflation Tutorial 3
Created on Fri Dec  1 10:57:11 2023

@author: otmha
"""


import numpy as np

# compute q(x) = p(x) / (x-t) and residual r
# A = array of coefficients of p(x)
# t = root
# q = array of coefficients of q(x)
def poly_iter(A, t):
    n = len(A) - 1
    q = np.zeros(n, dtype = np.int8)
    r = A[n]
    for a in reversed(range(n)):
        s = A[a]
        q[a] = r
        r = s + r*t
        
    print("---------------------------------------")
    print("Coefficients a0, a1, a2, ..., an of quotient")
    print(q)
    print("---------------------------------------")
    print("Residual:")
    print(r)
    return []

# Example function x**3 - 12*x**2 - 42 divided by x - 3
# Synthetic division produces quotient x**2 - 9*x - 27, remainder -123


A = np.array([-42,0,-12,1])
t = 3
poly_iter(A,t)
        
