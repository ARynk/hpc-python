"""
Hands-on: Input and output
This exercise is located in numpy/input-output/
"""
import numpy as np

FILE_PATH = '../numpy/input-output/xy-coordinates.dat'

#Read the data
xy = np.loadtxt(FILE_PATH)
print(xy)
#Add then 2.5 to all y values
xy[:,1] += 2.5
#Write the new data into a file
np.savetxt('output.dat', xy, fmt='%10.6f', header='new XY coordinates')

