import numpy as np
import matplotlib.pyplot as plt

factor = 1

while factor < 1000:
    x = np.linspace(-10, 10, factor)

    y = x**3 - 4 * x**2 - 3 * x + 10

    maximum = np.max(y)
    minimum = np.min(y)
    average = np.mean(y)

    plt.plot(x, y)
    plt.title(f"(Max: {maximum})  (Min: {minimum})  (Avg: {avg})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.show()
    factor += 1