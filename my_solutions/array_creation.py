"""
Hands-on exercise: Array creation
This exercise is located in numpy/array-creation/
"""

import numpy as np

list1 = [2, 3, 4.5, 6.7]
x = np.array(list1)
print(x)

b = np.arange(-2.0, 2.2, 0.2)
print(b)

c = np.linspace(0.5, 1.5, 11)
print(c)

w = 'something'
d = np.array(w, dtype='c')
print(d)
