'''
1、map 函数；
map(fun, sqe):fun为函数，sqe：为可迭代序列
'''

def mapfunc(x):
    '''
    自定义函数，map 调用
    :param x:
    :return:
    '''
    return x**2 + 2*x + 1

print(map(mapfunc, [1, 2, -2, -1]))
# print(list(map(mapfunc, [1, 2, -2, -1])))

'''
map 函数使用匿名函数 lambda
'''
l = [1, 2, 3, 4]
a = list(map(lambda x: x+2, l))
print(a)
print(list(a))

print(list(map(lambda x, y: x+y, [1, 3, 5], [5, 3, 1])))
