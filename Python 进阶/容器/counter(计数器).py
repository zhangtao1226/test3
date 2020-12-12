'''
Counter 是一个计数器，它可以帮助我们针对某项数据进行计数。
'''

# 例如计算每个人喜欢多少种颜色
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colours in colours)
print(favs)  # Counter({'Yasoob': 2, 'Ali': 2, 'Arham': 1, 'Ahmed': 1})

# 统计文件

with open('./容器.py', 'rb') as f:
    line_count = Counter(f)
print(line_count)