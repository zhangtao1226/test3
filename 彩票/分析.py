# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 22:20
# @Author  : zhangtao
# @File    : 分析.py
# @Software: PyCharm

number_list = []
def read_file():
    with open('luck_number.txt', 'r') as file:
        # print(file.readlines())
        for line in file.readlines():
            number_list.append(line[1:-2])


read_file()
print(number_list)