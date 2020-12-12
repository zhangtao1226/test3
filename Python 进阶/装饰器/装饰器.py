'''
装饰器
'''

# 授权（Authorization）
'''
装饰器能有助于检查某个人是否被授权去使用一个 web 应有的端点（endpoint）。
它们被大量使用与 Flask 和 Django web 框架中。
'''
# 基于装饰器的授权
from functools import wraps
import request

# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username, auth.password):
#             authenticate()
#         return f(*auth, **kwargs)
#     return decorated

# 日志（Logging）

from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        # print(dir(func)) # 查看该方法的所有属性
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
    """Do some math."""
    return x + x

# result = addition_func(4)
# print(result)

# 在函数中嵌入装饰器
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opend_file:
                # 将日志写到指定日志文件
                opend_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

# myfunc1()

@logit(logfile='func2.log')
def myfunc2():
    pass
# myfunc2()

# 装饰器类
from functools import wraps

class Logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func, *args, **kwargs):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            with open(self.logfile, 'a') as file:
                file.write(self.logfile + '\n')
            self.notify()
            return func(*args, **kwargs)
        return wrapped_func

    def notify(self):
        pass

@Logit(logfile='log2.log')
def myfunc():
    pass
