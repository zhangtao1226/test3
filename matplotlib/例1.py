"""
定义一个后端，将 Figure 连接至该后端，然后使用 numpy 库创建 10000个泊松分布的随机数，最后在 Figure 对象中绘制出它们的直方图
"""

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

fig = Figure()  # 创建一个 Figure 实例
canvas = FigureCanvas(fig)  # 将 fig 连接至后端
x = np.random.poisson(5, 10000)
# 不能通过空 Figure 绘图，必须调用 add_subplot() 方法创建一个或多个 subplot，在 subplot 上绘图
ax = fig.add_subplot(1,1,1)  # 添加子图，将画布分隔成 1行1列，图像将画在从左到右，从上到下的第1块子图上
# y = [1,2,3,4,45,6]
# ax.hist(y)                     # 绘制直方图
ax.hist(x)                       # 绘制直方图
ax.set_title('poisson distribution with lam=5') # 为子图设置标题
fig.savefig('poisson_histogram_2.png')
