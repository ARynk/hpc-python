"""
Hands-on: Split and combine arrays
This exercise is located in numpy/split-combine/
"""
import numpy as np

#Create a new 8x8 array with some values
a = np.arange(8*8).reshape(8,8)
#Splitting the array into two new 4x8 arrays
b = np.split(a, 2)
print(b)
#Reconstruct the original 8x8 array
ar = np.concatenate(b)
print(ar)

#create now 8x4 subarrays and then combine them
a2 = np.arange(8*8).reshape(8,8)
#Splitting the array into two new 8x4 arrays
b2 = np.split(a2, 2, axis=1)
print(b2)
#Reconstruct the original 8x8 array
ar2 = np.concatenate(b2, axis=1)
print(ar2)
