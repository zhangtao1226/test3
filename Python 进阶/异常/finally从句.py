"""
finally 从句：包裹在 finally 语句块中的代码不管是否异常都会被执行。这可以被用来在脚本执行之后做清理工作。
"""
def finally_demo():
    try:
        file = open('text.txt', 'rb')
    except IOError as e:
        print('An error: {}'.format(e.args[-1]))
    finally:
        print('this woruld be printed whether or not an exception')
finally_demo()