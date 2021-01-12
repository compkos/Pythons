import matplotlib.pyplot as plt
import numpy as np
p = 3.14
x = np.arange(0.0, 5.0, 0.1)
y = np.cos(2 * p * x)
plt.plot(x, y)
plt.show()
