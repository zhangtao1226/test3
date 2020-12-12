'''
python 提供了 multiprocessing 模块来开启子进程，并在子进程中执行我们定制的任务（比如函数），该模块与多线程
模块 threading 的编程接口类似。multiprocessing 模块的功能众多看：支持子进程、通信和共享数据，执行不同形式的同步，提供了 Process、
Queue、Lock 等组件。

Process 类介绍
1、创建进程的类：
Process([group [, target[, name[, args[, kwargs]]]]]),由该类实例化得到的对象，可用来开启一个子进程
强调：
    1、需要使用关键字的方式来指定参数。
    2、args 指定的为传给 target 函数的位置参数，是一个元组形式，必须有逗号。

2、参数介绍：
group   参数未使用，值始终未 None
target  表示调用对象，即子进程要执行的任务
args    表示调用对象的位置参数元组，args=（1,2,'tao',）
kwargs  表示调用对象的字典，kwargs={'name':'tao', 'age':'18'}
name    为子进程的名称
'''
