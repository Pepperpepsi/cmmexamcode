# -*- coding: utf-8 -*-
"""
CMM Root Finding - Bisection Tutorial
Created on Wed Nov 29 11:08:44 2023

@author: otmha
"""


### Bisection Method
import math

def bisection(f,a,b,N):
    # f = function trying to approximate sol
    # a, b = solution interval
    # N = number of iterations
   
#    Re = 13,743
#    D = 0.005
#    e = 0.000005
      
    if f(a)*f(b) >= 0:
        print("Bisection method fails, no root within bound")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
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
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2

# example function
f = lambda x: x**2 + 4*x - 12
# first root
approx_phi = bisection(f, -10, -3, 5)
print(approx_phi)
# second root
approx_phi = bisection(f, 0, 10, 5)
print(approx_phi)

# compare results with quadratic formula
def quad_formula_pos(a, b, c):
    return (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
def quad_formula_neg(a, b, c):
    return (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

print(quad_formula_neg(1,4,-12))
print(quad_formula_pos(1,4,-12))

def error(exp, theor):
    e = 100*(exp - theor)/theor
    return e

exp = bisection(f, -10, -3, 5)
theor = quad_formula_neg(1,4,-12)

print(error(exp, theor))

### Apply to different wonky function
# Will help if we plot
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.2)
y = np.sin(x)*np.e**(x**0.1)
plt.plot(x, y)
plt.show()

# Plot shows its between 2 and 4
f = lambda x: np.sin(x)*np.e**(x**0.1)
approx_phi = bisection(f, 2, 4, 1000)
print(approx_phi)
# Tends towards pi