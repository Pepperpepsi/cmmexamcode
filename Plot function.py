import numpy as np
import matplotlib.pyplot as plt

L = 800
E = 40000
I = 40000
w0 = 3.5
xrange = np.linspace(0,800,1000) #(0, L, interval)


def y_coords(x):
    y = (w0/120*E*I*L)*((-x**5)+2*(L**2)*(x**3)-(L**4)*x)
    return y

yrange = y_coords(xrange)


plt.plot(xrange,yrange)    
plt.scatter(xrange[np.argmin(yrange)], yrange[np.argmin(yrange)])

plt.show() 
        



