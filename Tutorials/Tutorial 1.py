# -*- coding: utf-8 -*-
"""
CMM Tutorial 1
Created on Sun Nov 26 16:35:23 2023

@author: otmha
"""

### Exercise 1: Squaresum
# Return the sum of the square of the first n natural numbers 
def squaresum(n) : 
  
    # Iterate i from 1  
    # to n finding  
    # the square of i and 
    # add to sum. 
    sm = 0
    for i in range(1, n+1) : 
        sm = sm + (i * i) 
      
    return sm 
  
# Main Program 
n = 20
sum_numbers = squaresum(n)
print(sum_numbers) 

# Return the sum of the square of the first n odd natural numbers
def odd_squaresum(n):
    sm = 0
    for i in range(1, n*2):
        if i % 2 == 1: 
            sm = sm + (i * i)
    return sm

n = 20
sum_odd_numbers = odd_squaresum(n)
print(sum_odd_numbers)


### Exercise 2: Arrays
# Create array with 20 elements, all zeroes
import numpy as np
np.array([0]*20)
# Change the values with random numbers in the range (0,10)
import random
array = []
for i in range(20):
    x = random.randint(0,10)
    array.append(x) 
        
# Print all elements
print(array)
# Find the index of the elements larger than 5 and smaller than 6, print them on the console

# Alternatively (solution)
n = 20
x = np.zeros(n)
random_min = 0
random_max = 10
for i in range(0, n):
    x[i] = random.uniform(random_min, random_max)
print(x)
a = 5
b = 6
for i in range(0,n):
    if x[i] > a and x[i] < b:
        print(i)
        
### Plotting
# Create an array x of equispaced coordinates in range (0,2pi)
# Create an array y, where the elements of y are the sine of elements x
# Plot y vs x
import math
import matplotlib.pyplot as plt
import numpy as np

n = 20
x = np.linspace(0, 2.0*math.pi, num = n)
y = np.sin(x)
plt.plot(x,y, ".") #dot makes it dots
plt.xlabel("x")
plt.ylabel("y")
plt.show()
    