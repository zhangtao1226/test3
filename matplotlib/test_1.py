import numpy as np
from matplotlib import pyplot as plt
import matplotlib
a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
for i in a:
    print(i)
# x = np.arange(1,11)
# y = x*2 + 5
# plt.title('matplotlib_test')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.plot(x,y)
# plt.show()