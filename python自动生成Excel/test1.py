# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 19:28
# @Author  : zhangtao
# @File    : test1.py
# @Software: PyCharm

import pandas as pd
import xlwings as xw
import matplotlib.pyplot as plt

# 对齐数据
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_with', True)


def create_excel():
    wb = xw.Book()
    sht = wb.sheets["Sheet1"]
    sht.name = "fruit_and_veg_sales"
    sht.range("A1").options(index=False).value = d
