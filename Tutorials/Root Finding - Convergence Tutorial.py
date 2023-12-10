# -*- coding: utf-8 -*-
"""
CMM Root Finding Convergence Tutorial 3
Created on Fri Dec  1 10:33:19 2023

@author: otmha
"""


import math
import numpy as np
import matplotlib.pyplot as plt

def newton(f, Df, x0, N):
    xn = x0
    for n in range(0,N):
        fxn = f(xn)
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    return xn

def secant(f, a, b, N):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

# Number of iterations
n_max = 20

# Array to collect NR results
n_array_NR = np.zeros(n_max-1)
sol_array_NR = np.zeros(n_max-1)
fun_array_NR = np.zeros(n_max-1)

# Array to collect S results
n_array_S = np.zeros(n_max-1)
sol_array_S = np.zeros(n_max-1)
fun_array_S = np.zeros(n_max-1)

# Variables
f = lambda x: x**2 + 4*x - 12
df = lambda x: 2*x + 4
x0 = 1
a = 1
b = 3

# Program
for i in range(1, n_max):
    solution = newton(f, df, x0, i)
    n_array_NR[i-1] = i
    sol_array_NR[i-1] = solution
    fun_array_NR[i-1] = np.absolute(f(solution))
    
    solution = secant(f, a, b, i)
    n_array_S[i-1] = i
    sol_array_S[i-1] = solution
    fun_array_S[i-1] = np.absolute(f(solution))

# Plot showing convergence of solution
# Orange is secant, blue is NR
plt.figure()
plt.plot(n_array_NR, sol_array_NR, "-.", n_array_S, sol_array_S, "-.")
plt.xlabel("Iterations")
plt.ylabel("Solution")

# Error plot
plt.figure()
# Plot error defined as a function
# Blue is NR
plt.semilogy(n_array_NR,fun_array_NR, '-.',n_array_S,fun_array_S, '-.')
# plot a couple of scaling lines to assess convergence rate
#plt.semilogy(n_array_S,np.exp(-2.0*n_array_S))
#plt.semilogy(n_array_S,np.exp(-2.5*n_array_S))
plt.xlabel("Iterations")
plt.ylabel("Error, defined as f(solution)")

# NR converges far faster

