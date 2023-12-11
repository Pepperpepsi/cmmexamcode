# -*- coding: utf-8 -*-
"""
CMM Newton-Raphson, Secant, and SciPy Tutorial 2
Created on Thu Nov 30 19:46:36 2023

@author: otmha
"""


import math
import numpy as np
import matplotlib.pyplot as plt
import scipy 

x = np.arange(-10, 10, 0.2)
y = x**2 + 4*x - 12

def false_pos(f,a,b,N):
    # f = function [manually define]
    # a, b = search interval
    # N = Number of iterations
    '''
    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> secant(f,1,2,5)
    1.6180257510729614
    '''
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

f = lambda x: x**2 + 4*x - 12
solution = false_pos(f,0,10,25)
print(f'The solution of regula falsi is: {solution}')

def secant(f, x1, x2, N):
    y1, y2 = f(x1), f(x2)
    while True:
        root = (x1*y2 - x2*y1)/(y2 - y1)
        y_root = f(root)
        if y_root == 0:
            return y_root
        yield root
        x1 = x2
        y1 = y2
        x2 = root
        y2 = y_root
    
f = lambda x: x**2 + 4*x - 12
solution = false_pos(f,0,10,25)
print(f'The solution of secant method is: {solution}')


def newton(f,Df,x0,epsilon,max_iter):
    # f = function [manually define]
    # Df = derivative of f(x) [manually define]
    # x0 = initial solution guess
    # epsilon =  stopping criteria
    # max_iter = max number of iteratiosn
    '''
    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> Df = lambda x: 2*x - 1
    >>> newton(f,Df,1,1e-8,10)
    Found solution after 5 iterations.
    1.618033988749989
    '''
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        # Error control
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

f = lambda x: x**2 + 4*x - 12
df = lambda x: 2*x + 4
x0 = 1
epsilon = 0.001
max_iter = 100
solution = newton(f,df,x0,epsilon,max_iter)
print(f'The solution of the Newtown method is: {solution}')



def newton_raphson_complex(func, derivative, initial_guess, max_iter=100, tolerance=1e-6):

    root = initial_guess
    
    for _ in range(max_iter):
        f_value = func(root)
        f_prime_value = derivative(root)
        
        # Avoid division by zero if the derivative is zero.
        if f_prime_value == 0:
            new_root = root
        else:
            new_root = root - f_value / f_prime_value
        
        # Check if the change in the root estimate is within the tolerance.
        if abs(new_root - root) < tolerance:
            return new_root
        
        root = new_root
    
    return root

# Define the complex function and its derivative based on the polynomial and its derivative.
def complex_function(ω):
    return np.polyval(coeffs, ω)

def complex_derivative(ω):
    return np.polyval(np.polyder(coeffs), ω)

# Initial guess for the roots - these are complex numbers chosen to start the iteration.
initial_guesses = [complex(-10, 0), complex(0, -1), complex(2, 10), complex(-1, 0)]

# Coefficients of the characteristic polynomial.
coeffs = [1, 24, 4500, 18000, 2250000]

# Call the Newton-Raphson method to find the roots of the polynomial.
roots = []
for initial_guess in initial_guesses:
    root = newton_raphson_complex(complex_function, complex_derivative, initial_guess)
    roots.append(root)

# Print the found roots to the console.
print('The roots of the fourth order polynomial are', roots)




### SciPy
from scipy import optimize
def f(x):
    return x**2 + 4*x - 12

# First root
first_root = optimize.newton(f, -10)
print(first_root)
# Second root
second_root = optimize.newton(f, 1.5)
print(second_root)

# or

ddf = lambda x: 2

scipy.optimize.newton(f, x0, fprime = df, tol = 0.001, maxiter = 3, fprime2 = ddf)
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html

plt.plot(x, y)
plt.show()


