"""
问题：需要从某个可迭代对象中分解出 N 个元素，但这个可迭代对象的长度可能超过 N，这会导致出现 " 分解的值过多
    （too many values to unpack）的异常。

解决方案：
    Python 的"*表达式" 可以用来解决这个问题。
"""


# 例如，假设开设了一门课程，并决定在期末的作业成绩中去掉第一个和最后一个，只对中间剩下的成绩做平均统计。
from audioop import avg

grades = [67, 70, 78, 82, 85, 90, 93]

def average_score(grades):
    first, *middle, last = grades
    return middle

print(average_score(grades))  # [70, 78, 82, 85, 90]

record = ('Tao', 'zhangtao@outlook.com', '777-555-1212', '847-555-1212')
name, email, *phone_numbers = record

print(name, email, phone_numbers)  # Tao zhangtao@outlook.com ['777-555-1212', '847-555-1212']


# * 式的语法在迭代一个变长的元组序列时尤其有用
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# * 式 的语法支持字符串分解操作，字符串拆分（splitting)

line = 'nobody:*:-2:-2:Unprovileged User:/var/empty:/usr/bin/false'
uname, *fields, homdir, sh = line.split(':')

print(uname, fields, homdir, sh)

