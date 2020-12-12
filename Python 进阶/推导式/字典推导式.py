"""
字典推导和列表推导的使用方法类似

注：
字典的循环方式：
1、for k in dic.keys()
2、for k, v in dic.items()
3、for k in dic

字典取值：
1、dic['key'] : 返回字典中对应的key值，若 key 不存在，则报错
2、dic.get(key, default = None) : 返回字典中 key 对应的值，若 key 不存在，则返回 default 的值（default 默认为 None）
"""


mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

for k in mcase.keys():
    print(mcase.get(k.lower(), 0), mcase.get(k.upper(), 0))


def demo_1():
    mcase_frequency = {
        k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()
    }
    return mcase_frequency

def demo_2():
    '''快速对换一个字典的键和值'''
    new_mcase = {v: k for k, v in mcase.items()}

    return new_mcase
print(demo_2())
