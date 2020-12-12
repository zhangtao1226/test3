'''
Pool 对象，提供了一种快捷的方法，赋予函数并行化处理一系列输入值的能力，可以将输入数据分配给不同进程处理
（数据并行）。
'''
from multiprocessing import Pool

def demo_pool(x):
    return x * x

if __name__ == '__main__':
    with Pool(5) as  p:
        print(p.map(demo_pool, [1, 2, 3]))