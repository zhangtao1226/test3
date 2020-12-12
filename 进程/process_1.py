import time
import random
from multiprocessing import Process

def demo(name):
    print('%s demoing' %name)
    time.sleep(random.randrange(1,4))
    print('%s demo end' %name)

if __name__ == '__main__':
    '''实例化得到四个对象'''
    p1 = Process(target=demo,args=('a',))
    p2 = Process(target=demo, args=('b',))
    p3 = Process(target=demo, args=('c',))
    p4 = Process(target=demo, args=('d',))


    # 调用对象的方法，开始四个进程
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    print('主')