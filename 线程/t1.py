'''
Python线程
python中使用线程有两种方式：函数或者用类来包装线程对象

函数式：调用 _thread 模块中的 start_new_thread() 函数产生新线程。
语法：
_thread.start_new_thread(function, args[, kwargs])
参数说明：
1、function 线程函数
2、args     传递给线程函数的参数，必须为 tuple 类型
3、kwargs   可选参数

'''

import _thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s : %s" %(threadName, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Error: 无法启动线程")

while 1:
    pass