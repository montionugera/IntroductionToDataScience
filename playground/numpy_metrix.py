__author__ = 'montionugera'
import numpy as np
from scipy import linalg
A = np.array([[1,2],[3,4]])
linalg.inv(A)
b = np.array([[5,6]]) #2D array
b.T
A*b #not matrix multiplication!
A.dot(b.T) #matrix multiplication
b = np.array([5,6]) #1D array
b.T  #not matrix transpose!
A.dot(b)  #does not matter for multiplication