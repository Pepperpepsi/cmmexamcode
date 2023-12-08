import numpy as np
import matplotlib.pyplot as plt

def function(x):
    y = 2*np.sin(x)-(x**2/10)
    return y

R = (5**0.5-1)/2
iteration = 1

def golden_search(xlow, xhigh, iter, es, fx):
    xl = xlow
    xu = xhigh
    d = R + (xu - xl)
    x1 = xl + d
    x2 = xu - d
    f1 = fx(x1)
    f2 = fx(x2)
    
    
    


# plt.plot(xrange,yrange)    
# plt.scatter(xrange[np.argmin(yrange)], yrange[np.argmin(yrange)])

# plt.show()