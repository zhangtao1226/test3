# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 18:42
# @Author  : zhangtao
# @File    : 统计汇总函数.py
# @Software: PyCharm

import pandas as pd
import numpy as np

x = pd.Series(np.random.normal(2, 3, 10000))
y = 3*x + 10 + pd.Series(np.random.normal(1, 2, 1000))


# 计算x与y的相关系数
# print(x.corr(y))

# 计算y的偏度
# print(y.skew())

# 计算y的统计描述值
# print(y.describe())

z = pd.Series(['A', 'B', 'C']).sample(n=1000, replace=True)
# print(pd.Series(['A', 'B', 'C']))
# print(z)
# 重新修改z的行索引
z.index = range(1000)
# print(z)

# 按照z分组，统计y的组内平均值
a = y.groupby(by=z).aggregate(np.mean)
# print(a)

# 统计z中个元素的频次
# print(z.value_counts())

a = pd.Series([1, 5, 10, 25, 30])
# 计算a中各个元素的累计百分比
# print(a.cumsum() / a.cumsum()[a.size - 1])

x = pd.Series([10, 13, np.nan, 17, 28, 19, 33, np.nan, 27])

# 检验序列中是否存在缺失值
# print(x.hasnans)

# 缺失值填充为平均值
# print(x.fillna(value=x.mean()))
# print(x.hasnans)

# 向前填充缺失值
# print(x.ffill())
# print(x.hasnans)

income = pd.Series(['12500元', '8000元', '8500元', '15000元', '9000元'])

# 将收入转换为整型
# print(income.str[:-1].astype(int))

gender = pd.Series(['男', '女', '女', '女', '男', '女'])

# 性别因子化处理
# print(gender.factorize())

house = pd.Series(['大宁金茂府 | 3室2厅 | 158.32平米 | 南 | 精装',
                   '昌里花园 | 2室2厅 | 104.73平米 | 南 | 精装',
                   '纺大小区 | 3室1厅 | 68.38平米 | 南 | 简装'])

# 取出二手房的面积，并转换为浮点型
# print(house.str.split('|').str[2].str.strip().str[:-2].astype(float))

np.random.seed(1234)
x = pd.Series(np.random.randint(10, 20, 10))
print(x)

# 筛选出16以上的元素
print(x.loc[x > 16])

# print(x.com(x < 16))


