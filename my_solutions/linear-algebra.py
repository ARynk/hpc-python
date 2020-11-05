"""
Hands-on: Linear algebra
This exercise is located in numpy/linear-algebra/
"""
import numpy as np

#Construct two symmetric 2x2 matrices A and B
A = np.array([[1,2], [3,4]])
print('A\n', A)
Asym = A + A.T
print('Asym = A + A^T\n', Asym)
B = np.array([[5,6], [7,8]])
print('B\n', B)
Bsym = B + B.T
print('Bsym = B + B^T\n', Bsym)

#Calculate the dot product
C = np.dot(Asym, Bsym)
print('C = Asym*Bsym\n', C)
#Calculate the eigenvalues of matrix C
ev = np.linalg.eigvals(C)
print('The eigenvalues of matrix C:', ev)
