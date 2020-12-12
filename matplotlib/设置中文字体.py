import numpy as np
import matplotlib.pyplot as plt


a = np.arange(0.0, 5.0,0.02)
plt.plot(a, np.sin(2*np.pi*a), 'k--')
plt.xlabel('横轴：时间', fontproperties='Arial Unicode MS', fontsize=18)
plt.ylabel('纵轴：振幅', fontproperties='Arial Unicode MS', fontsize=18)
plt.title('正弦线', fontproperties='Arial Unicode MS', fontsize=18)

# 添加注解
'''
xy(2.25,1)指定箭头的位置，xytext(1,1) 自定箭头的注解文本的位置， facecolor='black' 指定
箭头填充的颜色，shrink=0.1 指定箭头的长度，width=1 指定箭头的宽度，fontsize=15指定箭头尺寸
'''
plt.annotate(r'$\mu=100$', fontsize=15, xy=(2.25,1), xytext=(1,1),
             arrowprops=dict(facecolor='black', shrink=0.1, width=1))

plt.text(1, 1.5, '正弦波曲线', fontproperties='Arial Unicode MS', fontsize=20)

plt.axis([0,3,-2,2])  # x轴取值范围
plt.grid(True)  # 在绘图区域添加网格线


plt.show()