
class A(object):
    def __init__(self):
        print('这是 __init__ 方法', self)

    def __new__(cls, *args, **kwargs):
        print('这是 cls 的 ID:', id(cls))
        print('这是 new 方法', object.__new__(cls))
        return object.__new__(cls)

A()
print('这是类 A 的 ID', id(A))