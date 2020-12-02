from numpy import array
from scipy.linalg import svd
# define a matrix
import numpy as np
A = np.array([[307, -142], [144, -60], [-60, 25]])
# SVD
U, s, VT = svd(A)
print(" U = ")
print(U)
print("\n S = ")
print(s)
print("\n V = ")
print(VT)