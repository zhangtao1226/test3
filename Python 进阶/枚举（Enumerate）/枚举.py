'''
枚举（enumerate) 是 Python 内置函数。它允许我们遍历数据并自动计数
'''

my_list = ['apple', 'banana', 'grapes', 'pear', 'apple']
for c, value in enumerate(my_list, 1):
    print(c, value)


counter_list = list(enumerate(my_list, 1))
print(counter_list)