"""
Hands-on: Finite difference
Derivatives calculated numerically with the finite-difference method.
This exercise is located in numpy/finite-difference/
"""

import numpy as np
import math
import matplotlib.pyplot as plt

#array containing the values of xi in the interval [0,π/2] with spacing Δx=0.1
delta = 0.1
x = np.arange(0, np.pi/2, delta)
#the derivative of sin in this interval
y = np.sin(x)
derivative = (y[2:] - y[:-2])/(2*delta)
print(derivative)

#Compare the result to function cos in the same interval
yc = np.cos(x[1:-1])
plt.plot(x[1:-1], derivative, label="sin'")
plt.plot(x[1:-1], yc, label="cos")
plt.legend()
plt.show()
