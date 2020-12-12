'''
*args 和 **kwargs 主要用于函数定义。可以将不定数量的参数传递给一个函数。
'''

# *args 用法， *args 是用来发送一个非键值对的可变数量的参数列表给一个函数。
def test_var_args(f_arg, *args):
    print('first normal arg:', f_arg)
    for arg in args:
        print("another arg through *argv:", arg)

# test_var_args('yasoob', 'python', 'eggs', 'test')

# **kwargs 的用法
# **kwargs 允许将不定长度的键值对，作为参数传递给一个函数。如果想要在一个函数里处理带名字的
#参数，应该使用 **kwargs。
def greet_me(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

# greet_me(name='aaa', age=16)

# 示例
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

aaa = ('aaa', 2, 8)

# test_args_kwargs(*aaa)

# **kwargs 示例
kwargs = {'arg3':3, 'arg2':"two", 'arg1':1}
# test_args_kwargs(**kwargs)

