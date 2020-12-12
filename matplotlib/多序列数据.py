import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y1 = np.sin(2*x)/x
y2 = np.sin(3*x)/x
y3 = np.sin(4*x)/x

plt.plot(x, y1, 'k--')
plt.plot(x, y2, 'k-.')
plt.plot(x, y3, 'k')
plt.show()
