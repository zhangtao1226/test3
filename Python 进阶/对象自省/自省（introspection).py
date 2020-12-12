'''
自省（introspection) 在计算机编程领域里，是指在运行时来判断一个对象的类型的能力。它是 Python 的强项之一。
Python 中所有一切都是一个对象，而且我们可以仔细勘察安心对象
'''

'''
1、dir : 它是用于自省的最重要的函数之一。它返回一个列表，列出了一个对象所拥有的属性和方法。
'''

my_list = [1, 2, 3]
dir(my_list)

"""
返回 ： ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
        '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', 
        '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
        '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
        '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 
        'insert', 'pop', 'remove', 'reverse', 'sort']
"""

'''
2、type 和 id : type函数返回一个对象的类型；id 函数返回对象的唯一 ID。
'''

'''
3、inspect 模块：用来获取活跃对象的信息。
'''
import inspect

print(inspect.getmembers(str))