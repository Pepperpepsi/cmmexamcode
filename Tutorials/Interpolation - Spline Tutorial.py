# -*- coding: utf-8 -*-
"""
CMM Spline Tutorial 4
Created on Mon Dec  4 17:38:31 2023

@author: otmha
"""
import numpy as np
import matplotlib.pyplot as plt


### Given Data
x = np.array([0.  , 0.06666667, 0.13333333, 0.2 ,  0.26666667, 0.33333333,
     0.4 , 0.46666667, 0.53333333, 0.6 ,  0.66666667, 0.73333333,
     0.8 , 0.86666667, 0.93333333, 1.  , ])

y = np.array([ 0.00000000e+00,  7.78309056e-01,  1.24040577e+00,  1.24494914e+00,
      8.90566050e-01,  4.33012702e-01,  1.12256994e-01,  4.54336928e-03,
     -4.54336928e-03, -1.12256994e-01, -4.33012702e-01, -8.90566050e-01,
     -1.24494914e+00, -1.24040577e+00, -7.78309056e-01, -4.89858720e-16])

### Preview Plot
plt.figure()
plt.plot(x,y)

from scipy import interpolate
x_int = np.linspace(0,1, 128)
f_lin = interpolate.interp1d(x, y, kind = "linear")
y_int = f_lin(x_int)

# Generate spline
f_spline = interpolate.splrep(x,y, s=0) #s=0 no weights applied
y_spline = interpolate.splev(x_int, f_spline, der = 0) #der = order of derivative

plt.figure()
plt.plot(x,y, "bh", ms = 10)
plt.plot(x_int,y_int,'b',x_int,y_spline,'b') #add . or - etc. to change 
plt.xlabel('x')
plt.ylabel('y')

# zoom in with
# plt.xlim(0.05,0.3)
# plt.ylim(0.5,1.5)

plt.show()