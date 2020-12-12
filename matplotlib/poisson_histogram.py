import numpy as np
import matplotlib.pyplot as plt

s = np.random.poisson(5,10000)
count = plt.hist(s)
plt.show()
