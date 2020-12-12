'''
python 中可变（mutable)与不可变（immutable）的数据类型。简单的说，可变（mutable）意味着"可以被改动"，而不可变（immutable）的意思是
"常量（constant）"
'''

def demo_1():
    foo = ['hi']
    print(foo)

def demo_2():
    """
    发现 foo 被改变，这是应为对象可变性（mutability) 在作怪。每当你将一个变量赋值为另一个可变类型的变量时，对这个数据的任意改动会同时
    反映到这两个变量上去。新变量只不过是老变量的一个别名。这个情况只针对可变数据类型。
    :return:
    """
    foo = ['hi']
    bar = foo
    bar += ['bye']
    print(foo)

# demo_2()
def add_to1(num, target=[]):
    target.append(num)
    return target

#
# print(add_to1(1))  # [1]
# print(add_to1(2)) # [1, 2]
# print(add_to1(3)) # [1, 2, 3]
# 这是列表的可变性原因，在 python 中当函数被定义时，默认参数只会运算一次，而不是每次被调用时都会重新运算。
# 所以永远不要定义可变类型的默认参数

#列如：
def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

print(add_to(1))
print(add_to(2))
print(add_to(3))