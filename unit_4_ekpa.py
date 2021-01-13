import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.0, 5.0, 0.1)
y = np.cos(2 * np.pi * x)
plt.plot(x, y)
plt.show()
