# -*- coding: utf-8 -*-
"""
CMM Symbolic Mathematics Tutorial
Created on Fri Dec  8 13:59:01 2023

@author: otmha
"""


# Compute first and second derivative of y(x) = c*sin(a*x)
# Print z(x) = dy/dx + d^2/dx^2
# Simplify and expand Taylor series s(x) = (1/y) (dy/dx)
import sympy as sym

# define some symbols
x = sym.Symbol("x")
y = sym.Symbol("y")
a = sym.Symbol("a")
c = sym.Symbol("c")
dydx = sym.Symbol("dydx")
ddydxx = sym.Symbol("ddyddx")
#z = sym.Symbol("z") # Not necessary
s = sym.Symbol("s")


# define function
y = c*sym.sin(a*x)

# compute derivative
dydx = sym.diff(y,x)

# compute second derivative
ddydxx = sym.diff(dydx,x)

# define function
z = dydx + ddydxx

# define function
s = dydx/y

# simplify
simplified = sym.simplify(s)

# taylor
taylor = sym.series(simplified,x) #could also use s

# print
print("function y(x): ", y)
print("derivative dy/dx: ", dydx)
print("second derivative d^2y/dx^2: ", ddydxx)
print("z(x) = ",z)
print("s(x) simplified =", simplified)
print("s(x) taylor = ", taylor)

