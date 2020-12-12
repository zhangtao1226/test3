'''
线程模块：

python3 通过两个标准库 _thread 和 threading 提供对线程的支持。
_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限。
threading 模块除了包含 _thread 模块中所有方法外，还提供了其他方法：
1、threading.currentThread(): 返回当前的线程变量。
2、threading.enumerate():     返回一个包含正在运行的线程的 list 。正在运行指线程启动后、结束前，不包括启动前和终止后的线程
3、threading.activeCount():   返回正在运行的线程数量，与 len(threading.enumerate()) 有相同的结果。

除了使用方法外，线程模块同样提供了 Thread 类来处理线程，Thread 类提供了一下方法：
1、run():        用以表示线程活动的方法。
2、start():      启动线程活动。
3、join([time]): 等待至线程中止。这阻塞调用线程直至线程的 join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
4、isAlive():    返回线程是否活动的。
5、getName():    返回线程名。
6、setName():    设置线程名。
'''

'''
使用 threading 模块创建线程

可以直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新的线程
即它调用了线程的 run() 方法：
'''
import threading
import time

exitFlag = 0

class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 开启新的线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("退出主线程")