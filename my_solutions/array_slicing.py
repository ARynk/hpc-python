"""
Hands-on exercise: Array slicing
This exercise is located in numpy/array-slicing/
"""
import numpy as np

#Create a 4x4 array with arbitrary values
e = np.full((4, 4), 1.5)
#Extract every element from the second row
print(e[1,:])
#Extract every element from the third column
print(e[:,2])
#Assign a value of 0.21 to upper left 2x2 subarray
e[:2, :2] = 0.21
#create a 8x8 array with chequerboard pattern, i.e. alternating zeros and ones
f = np.ones((8, 8))
f[::2, ::2] = 0
f[1::2, 1::2] = 0
print(f)
