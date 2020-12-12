'''
在 multiprocessing 中，通过创建一个 Process 对象然后调用它的 start() 方法来生成进程。Process 和 threading.Thread
API 相同。
'''

from multiprocessing import Process
import os

def demo_process(name):
    print('hello', name)

# if __name__ == '__main__':
#     p = Process(target=demo_process, args=('bob',))
#     p.start()
#     p.join()

def info(title):
    print(title)
    print('module name', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getppid())

def f(name):
    info('function f')
    print('hello', name)

def f_2(name):
    info('function f_2')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p2 = Process(target=f_2,args=('tao',))

    p.start()
    p2.start()
    p2.join()
    p.join()
