"""
问题：将 N 个元素的元组或序列，分解为 N 个单独的变量。

解决方法：
任何序列（或可迭代的对象）都可以通过一个简单的赋值操作来分解为单独的变量。
唯一的要求是变量的总数和结构要与序列相吻合。
实际上：不仅仅是元组或列表，只要对象可迭代，那么都可执行分解操作，比如：字符串、文件、迭代器以及生成器。
"""
p = [2, 4]
x, y = p

print(x, y)

data = ['tao', 30, 20.11, (2020, 8, 10)]
name, age, many, date = data
print(name, age, many, date)
name, age, many, (year, mon, day) = data


# 字符串
str = 'hello'
a, b, c, d, e = str
print(a, b, c, d, e)

# 如果分解时想丢弃某些值或者值获取某些特定值
date = ['Acme', 50, 90.1, (2020, 8, 23)]
_, shares, price, _ = date
print(shares, price)

