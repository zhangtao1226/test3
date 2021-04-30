# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 16:59
# @Author  : zhangtao
# @File    : 练习.py
# @Software: PyCharm
"""
1、编写一个Python函数 is_multiple(n, m)，用来接收两个整数值n和m，如果n是m的倍数，即存在整数i使得n=mi，那么函数返回True，否则返回False
"""

def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False
# print(is_multiple(6, 6))

"""
2、编写一个Python函数 is_even(k),用来接收一个整数k，如果k是偶数返回True，否则返回False，但是函数中不能使用乘法、除法或取余操作
"""
def is_even(k):
    if k & 1:
        return False
    else:
        return True

# print(is_even(4))
# print(is_even(5))

"""
3、编写一个Python函数 minmax(data) ，用来在数的序列中找出最小和最大数，并以一个长度为2的元组的形式返回。注意：不能通过内置函数 min 和 max来实现
"""
def minmax(data):
    # data.sort()
    # return data[0], data[len(data)-1]
    pass