"""
Hands-on: Random numbers
This exercise is located in numpy/random-numbers/
"""
import numpy as np
import matplotlib.pyplot as plt

#Generate a one dimensional 1000 element array of uniformly distributed random numbers
print('Uniform distribution')
a = np.random.random(1000)

#Calculate the mean and standard deviation of the array
mean_arr_a = np.mean(a)
std_arr_a = np.std(a)
print('mean:', mean_arr_a)
print('standard deviation:', std_arr_a)

#Choose some other random distribution and calculate its mean and standard deviation
print('Normal distribution')
b = np.random.normal(size=1000)

#Calculate the mean and standard deviation of the array
mean_arr_b = np.mean(b)
std_arr_b = np.std(b)
print('mean:', mean_arr_b)
print('standard deviation:', std_arr_b)

#Visualize the random distributions
plt.hist(a, 50)
plt.title('Uniform distribution')
plt.figure()
plt.hist(b, 50)
plt.title('Normal distribution')
plt.show()
