import numpy as np

x = np.linspace(-5, 5, 11)

y = x ** 2 + 2 * x -3

print(x)
print(y)
print(y[y > 10])
print(y.max())