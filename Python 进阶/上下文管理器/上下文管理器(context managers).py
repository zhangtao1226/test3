"""
上下文管理器（Context managers)
上下文管理器允许在有需要的时候，精确地分配和释放资源
使用上下文管理器最广泛的案例就是 with 语句。
"""

'''
基于类的实现
'''
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()

with File('text.txt', 'w') as open_file:
    open_file.write('tao')
'''
通过定义 __enter__ 和 __exit__ 方法，其中 __exit__ 函数接收三个参数。这些
参数对于每个上下文件管理类中的 __exit__ 方法都是必须的。底层发生了如下过程：
1、with 语句先暂存了 File 类的 __exit__方法
2、然后调用 File 类的 __enter__ 方法
3、__enter__ 方法打开文件并返回给 with语句
4、打开的文件句柄被传递给 opend_file 参数
5、使用 .write() 来写文件
6、with 语句调用之前暂存的 __exit__ 方法
7、__exit__ 方法关闭了文件
'''


"""
异常处理
__exit__方法的三个参数：exc_type, exc_val 和 exc_tb。
在 第4步和第6步之间，如果发生异常，Python 会将异常的 exc_type, exc_val 和 exc_tb
传递给 __exit__ 方法。它让 __exit__ 方法来决定如何关闭文件以及是否需要其他步骤。
"""


