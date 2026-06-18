import numpy as np

array1 = np.array([10,20,30,40])
array2 = np.array([1,2,3,4])

print(np.add(array1,array2))
print(np.subtract(array1,array2))
print(np.multiply(array1,array2))
print(np.divide(array1,array2))
print(np.power(array1,2))


values = np.array([2,4,6,8,10])
print(np.sqrt(values))
print(np.exp(values))
print(np.log(values))
print(np.sum(values))
print(np.cumsum(values))