'''
列表[1, 2, 3, 4, 5] ，请使用 map() 函数输出 [1, 4, 9, 16, 25], 并使用列表推导式提取
大于10的数，最终输出 [16，25]

map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function
函数返回值的新列表。
语法：
map(function, iterable, ....)
参数：
1、function 函数
2、iterable 一个或多个序列

注： Python 2.x 返回列表
    Python 3.x 返回迭代器
'''

li = [1, 2, 3, 4, 5]

res = map(lambda x: x**2, li)
print(res)
res = [i for i in res if i > 10]


print(res)
