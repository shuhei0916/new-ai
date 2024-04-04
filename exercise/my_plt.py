import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4)
y = x**3 - 12*x 

plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()