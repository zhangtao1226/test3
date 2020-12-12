'''
使用 pyplot 的 bar() 函数绘制的条形图根直方图类似，只不过 x 轴表示的不是数值而是类别
bar() 函数语法：
bar(left, height, width=0.8, color, align, orientation)
参数说明：
left：x轴的位置序列，即条形的起始位置。
height：y轴的数值序列，也就是条形图的高度，也就是需要展示的数据。
width: 条形图的宽度，默认为 0.8
color：条形图的填充颜色
align：{'center'，'edge'}，可选参数，默认为'center'，如果是'edge'，通过左边界（条形图垂直）和底边界（条形图水平）来使条形图对齐，如果是
'center' ，将left参数解释为条形图中心坐标。
orientation：{'vertical','horizontal'},垂直还是水平，默认垂直
'''

import matplotlib
import matplotlib.pyplot as plt
xvalues = [0,1,2,3]
GDP = [13,12,9,5]
matplotlib.rcParams['font.family'] = 'Arial Unicode MS'
matplotlib.rcParams['font.size'] = 15
plt.bar(range(4), GDP, align='center', color='black')
plt.ylabel('GDP')
plt.title('GDP-排名')
plt.xticks(range(4),['上海','北京','广州','深圳'])
plt.ylim([0, 15])
for x,y in enumerate(GDP):
    print(x,y)
    plt.text(x,y+100,'%s'%round(y,1),ha='center')
plt.show()