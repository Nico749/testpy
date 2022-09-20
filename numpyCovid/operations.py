import numpy as np
# sum between 2 vectors of the same rows and columns
arr2 = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8], 
                 [9, 1, 2, 3]])
arr3 = np.array([[11, 12, 13, 14], 
                 [15, 16, 17, 18], 
                 [19, 11, 12, 13]])

# print(arr2+arr3)

# BROADCASTING allowing arithmetic operations between two arrays with different numbers of dimensions but compatible shapes. 
arr4 = np.array([4, 5, 6, 7])
# print(arr2+arr4)
# When the expression arr2 + arr4 is evaluated, arr4 (which has the shape (4,)) is replicated three times to match the shape (3, 4) of arr2. 
# Numpy performs the replication without actually creating three copies of the smaller dimension array
# Broadcasting only works if one of the arrays can be replicated to match the other array's shape.

# generates random vector of x,y,z dimensions
print(np.random.rand(5,2,2))
# Range with start, end and step
np.arange(10, 90, 3)
