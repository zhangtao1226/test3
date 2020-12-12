"""
异常：
最基本的异常语句处理 ： try/except ，可能触发异常产生的代码会放到 try 语句块中，
而处理异常的代码块会在 except 语句块里实现。
"""
# 例：
def demo_errro():
    try:
        file = open('text.txt', 'rb')
        print(file)
    except IOError as e:
        print('An IOError occurrede: {}'.format(e.args[-1]))

# demo_errro()

# 处理多个异常

def error_more():
    try:
        file = open('text.txt', 'rb')
    except (IOError, EOFError) as e:
        print('An error occurred: {}'.format(e.args[-1]))
        return None
# error_more()

'''
当未知程序会抛出什么异常，可以使用 Exception
'''

def all_error():
    try:
        file = open('text.txt', 'rb')
    except Exception:
        print('error')
all_error()