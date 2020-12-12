"""
python 中的协程和生成器很相似但又不同。主要区别在于：
    * 生成器是数据的生产者
    * 协程则是数据的消费者
"""

def demo_yield():
    '''
    生成器
    :return:
    '''
    a, b = 0, 1
    while a < 20:
        yield a
        a, b = b, a+b

for i in demo_yield():
    print(i)

def grep(pattern):
    print('Searching for', pattern)
    while True:
        line = (yield )
        if pattern in line:
            print(line)
search = grep('coroutine')
next(search)

search.send('this is start')
search.send('this is second')
search.send('this is last')

search.close()

