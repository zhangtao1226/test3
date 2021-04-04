# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 18:51
# @Author  : zhangtao
# @File    : 常用函数.py
# @Software: PyCharm

import numpy as np

"""
1、np.random.normal(loc=0.0, scale=1.0, size=None) 
作用：生成高斯分布的概率密度随机数
loc: float  此概率分布的均值（对应着整个分布的中心centre
scale: float  此概率分布的标准差（对应一分布的宽度，scale越大越矮胖，scale越小，越瘦高
size:  int or tuple of ints  输出的shape，默认为None，只输出一个值
"""
x = np.random.normal(1, 2, 2)
print(x)  # [-0.12059345 -2.38150808]


