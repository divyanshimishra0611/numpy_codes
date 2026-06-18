import numpy as np
array_1D = np.array([1,2,3,4,5,6,7,8,9,10])
print(array_1D)
print(array_1D.ndim)
print(array_1D.shape)
print(array_1D.dtype)

array_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2D)
print(array_2D.ndim)
print(array_2D.shape)
print(array_2D.dtype)

list = [10,20,30,40,50]
array = np.array(list)
print(array)
print(array.shape)
print(array.dtype)