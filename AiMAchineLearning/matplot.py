import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1, 2, 5, 10, 17, 26])

plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
