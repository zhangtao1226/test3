'''
1、Map 会将一个函数映射到一个输入列表的所有元素上。
map(function_to_apply, list_of_inputs)

'''

def map_fun():
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x:x*2, items))
    print(squared)

# map_fun()

def multiply(x):
    return x*x
def add(x):
    return x+x

# funcs = [multiply, add]
#
# for i in range(5):
#     value = map(lambda x: x(i), funcs)
#     print(list(value))

'''
2、filter 过滤列表中的元素，并且返回一个有所有符合要求的元素构成的列表，
符合要求即函数映射到该元素时返回值为 True

注：filter 类似于一个 for 循环，但是它是一个内置函数，并且更快
'''
# numbers_list = range(-5, 5)
# less_thans_zore = filter(lambda x: x<0, numbers_list)
# print(less_thans_zore)
# print(list(less_thans_zore))


'''
3、当需要对一个列表进行一些计算并返回结果时，reduce 是个非常有用的函数。
'''
# 例如：当需要计算一个整数列表的乘积时
from functools import reduce

# product = reduce(lambda x,y : x * y,[1, 2, 3,4])
# print(product)


print(reduce(lambda x,y : x+y, [1,2,3,3]))