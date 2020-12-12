"""
函数缓存（Function caching）
    函数缓存允许我们将一个函数对于给定参数的返回值缓存起来。
    当一个 I/O 密集的函数被频繁使用相同的参数调用的时候，函数缓存可以节约时间。
在 Python 3.2 版本以前我们只有写一个自定义的实现。在 Python 3.2 以后版本，有个 lru_cache 的装饰器，运行我们将
一个函数的返回值快速地缓存或取消缓存。
"""
# Python 3.2 及以后版本
from functools import lru_cache
@lru_cache(maxsize=2) # maxsize=32， 表示 lru_cache 最多缓存最近多少个返回值
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print([fib(n) for n in range(10)])
# fib.cache_clear() # 清空函数缓存
