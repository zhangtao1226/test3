from typing import List, Tuple, Dict

def add(a: int, string: str, f:float, b:bool) -> Tuple[List, Tuple, Dict, bool]:
    list1 = list(range(a))
    tup = (string, string, string)
    d = {'a': f}
    b1 = b
    return list1, tup, d, b1
# print(add(5, 'hhh', 2.3, False))

def func(a:int, string:str) -> List[int or str]:
    list1 = []
    list1.append(a)
    list1.append(string)
    return list1

print(func(33, 'tao'))