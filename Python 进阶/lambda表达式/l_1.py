"""
lambda 表达式是一行函数。
他们在其他语言中也被称为匿名函数。如果不想在程序中对一个函数使用两次，也许会想用 lambda 表达式，它们和普通函数完全一样
原型：lambda 参数：操作（参数）
"""
# 例子：
add = lambda x, y : x + y
print(add(3,5))

# 列表排序
def list_sort():
    a = [(1, 2), (4, 1), (9, 10), (13, -3)]
    a.sort(key=lambda x: x[0])
    print(a)

# list_sort()

# 列表并行排序

def list_demo():
    list1 = [1, 5, 10,2, 3]
    list2 = ['a', 'e', 'g', 'b', 'c']
    data = zip(list1, list2)
    print(data)

    list1, list2 = map(lambda t:list(t), zip(*data))
    print(list1, list2)
list_demo()
