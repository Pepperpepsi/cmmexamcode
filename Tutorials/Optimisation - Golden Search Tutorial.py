# -*- coding: utf-8 -*-
"""
CMM Optimisation Tutorial
Created on Fri Dec  8 14:33:33 2023

@author: otmha
"""


### Maximise function f(x) = 2*sin(x) - x*2/10

### Imports
import numpy as np
import matplotlib.pyplot as plt

### Plot
xplot = np.linspace(-5,2.5, 50)
y = 2*np.sin(xplot) - 0.1*xplot**2
plt.plot(xplot,y)
plt.show()


def goldensection(ftn, xl, xm, xr, tol = 1e-9):
    # applies the golden-section algorithm to maximise ftn
    # we assume that ftn is a function of a single variable
    # and that x.l < x.m < x.r and ftn(x.l), ftn(x.r) <= ftn(x.m)
    
    # In this context, xm is an initial guess x-value for the optimum point
    # The algorithm iteratively refines x.l, x.r, and x.m and
    # terminates when x.r - x.l <= tol
    
    gr1 = 1 + (1 + np.sqrt(5))/2
    # successively refine x.l, x.r, and x.m
    fl = ftn(xl)
    fr = ftn(xr)
    fm = ftn(xm)
    while ((xr - xl) > tol):
        if ((xr - xm) > (xm - xl)): #switch sign to convert search
            y = xm + (xr - xm)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xl = xm
                fl = fm
                xm = y
                fm = fy
            else:
                xr = y
                fr = fy
        else:
            y = xm - (xm - xl)/gr1
            fy = ftn(y)
            if (fy >= fm): #switch sign to convert search
                xr = xm
                fr = fm
                xm = y
                fm = fy
            else:
                xl = y
                fl = fy     
    return(xm, ftn(xm))
    
# left, right, and middle x values
xl=0
xm=2
xr=10

# function being optimised
def ftn(x):
    return 2*np.sin(x)-(x**2/10)
print(goldensection(ftn, xl, xm, xr, tol = 1e-9))
# Seems to check out with the plot 
