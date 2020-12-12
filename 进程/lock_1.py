from multiprocessing import Lock, Process

def f(l, i):
    l.acquire()
    try:
        print('hello world %s'%i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock, num)).start()
