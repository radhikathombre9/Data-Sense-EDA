# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:29:58 2024

@author: Radhika
"""

import numpy as np
# Basic Assignments
# Create a 1D Numpy array with 10 elements and access the 5th element.
array = np.array([11,12,13,14,15,16,17,18,19,20])
print(array)
array[4]

# Create a 3x3 identity matrix.
identity_matrix = np.identity(3)
print(identity_matrix)

# Intermediate Assignments
# Given a 2D array, find the sum of all elements in each row.
array_matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(array_matrix)

array_matrix.sum()

total = np.sum(array_matrix, axis = 1)
print(total)

# Generate a 5x5 matrix with random numbers and calculate the mean and standard deviation.
random_matrix = np.random.rand(5,5)
print(random_matrix)

mean = np.mean(random_matrix)
print(mean)

sd = np.std(random_matrix)
print(sd)

# Advanced Assignments
# Perform matrix multiplication on two 3x3 matrices and verify the result manually.

matrix_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix_2 = np.array([[9,8,7],[6,5,4],[3,2,1]])

multiplication = np.dot(matrix_1,matrix_2)
print(multiplication)

# [1*9+2*6+3*3 1*8+2*5+3*2  1*7+2*4+3*1
# 4*9+5*6+6*3 4*8+5*5+6*2  4*7+5*4+6*1
# 7*9+8*6+9*3 7*8+8*5+9*2  7*7+8*4+9*1]

#  [9+12+9   8+10+6    7+8+3
#  36+30+18  32+25+12  28+20+6
#  63+42+27  56+40+18  49+32+9]

# [30 24 18 
#  84 69 54
#  138 114 90]







