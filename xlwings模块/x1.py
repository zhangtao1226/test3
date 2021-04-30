# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 19:43
# @Author  : zhangtao
# @File    : x1.py
# @Software: PyCharm

import xlwings as xw

wb = xw.Book('/Users/zhangtao/Desktop/xlwings-test.xlsx')
sht = wb.sheets("Sheet1")
sht.name = 'test'
sht.range("A1").options(index=False).value = 1