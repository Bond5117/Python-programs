import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-100, 100, 1000)

x = np.sin(np.cos(t))
y = np.cos(np.sin(t))


plt.plot(x, y)
plt.axis("equal")
plt.title("Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()