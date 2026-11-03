import numpy as np
import matplotlib.pyplot as plt

plt.ion()

fig, ax = plt.subplots()

factor = 2
flip = False

while factor > 0:
    x = np.linspace(-10, 10, factor)
    y = x**2

    ax.clear()

    ax.plot(x, y)
    ax.set_title(f"Number of points: {factor}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid()

    if factor == 100:
        flip = True

    if flip:
        factor -= 1
    else:
        factor += 1

    plt.pause(0.001)

plt.ioff()
plt.show()