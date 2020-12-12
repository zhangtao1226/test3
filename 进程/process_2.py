'''
创建并开启子进程方式二：继承 Process 类
'''
import time
import random
from multiprocessing import Process

class Piao(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print('%s piaoing' %self.name)
        time.sleep(5)
        print('%s piao end'%self.name)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


if __name__ == '__main__':
    p1 = Piao('a')
    p2 = Piao('b')
    p3 = Piao('c')
    p4 = Piao('d')

    # 调用对象下的方法，开启四个进程
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    p1.start() # start 会自动调用 run

    p2.start()
    p3.start()
    p4.start()
    p1.join()

    print('主')

