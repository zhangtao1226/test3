# 在函数中定义函数,在函数外不可调用函数中的函数

def hi(name='tao'):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def wecome():
        return "now you are in the welcome() function"
    print(greet())
    print(wecome())
    print("now you are back in the hi() function")

# hi()

# 从函数中返回函数
def hi_1(name='tao'):
    def greet():
        return "now you are in the greet() function"
    def welcome():
        return "now you are in the welcome() function"
    if name == 'tao':
        return greet
    else:
        return welcome
print('第一次打印：',hi_1('zhangtao')())
a = hi_1()
print('第二次打印：', a())

# 将函数作为参数传给另一个函数
def hi_2():
    return "hi tao"
def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi_2)