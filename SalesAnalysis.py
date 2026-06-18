import numpy as np

sales = np.array([1200,1500,900,2000,1800,1700,1600])

print(np.sum(sales))
print(np.mean(sales))
print(np.argmin(sales))
print(np.argmax(sales))
print(np.std(sales))
avg = np.mean(sales)

print(sales[sales>avg])
