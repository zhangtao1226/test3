"""
deque 提供了一个双端队列，可以从头/尾两端添加或删除元素。用法类似 python 的 list
"""
from collections import deque

d = deque()
d.append('1')
d.append('2')
print(d, len(d), type(d))