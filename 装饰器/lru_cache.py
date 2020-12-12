'''
Python 内置的装饰器（decorator) ，可以自动为任何函数缓存结果 => @functools.lru_cache(maxsize=None),其中 maxsize 表示 缓存最近的
多少次结果
'''
from functools import lru_cache
from typing import Dict, List, Tuple

@lru_cache(maxsize=None)
def fib(n: int) -> List[int]:
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

if __name__ == "__main__":
    print(fib(50))