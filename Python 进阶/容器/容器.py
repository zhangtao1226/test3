"""
容器（Collections）
python 附带一个模块，它包含许多容器数据类型，名字叫作 collections 。
包含：
    1、defaultdict
    2、counter
    3、deque
    4、namedtuple
    5、enum.Enum(包含在Python 3.4以上）
"""
# 1、defaultdict
# from collections import defaultdict
#
# colours = (
#     ('Yasoob', 'Yellow'),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )
#
# favourite_colours = defaultdict(list)
# for name, colour in colours:
#     favourite_colours[name].append(colour)
# print(favourite_colours)

'''
当在一个字典中对一个键进行嵌套赋值时，如果这个键不存在，会触发 keyError 异常。defaultdict 可以避免这个问题
'''
# 抛出 keyError 异常 ， 如下：
# some_dict = {}
# some_dict['colours']['favourite'] = "yellow"  # 异常输出：KeyError: 'colours'
#

# 解决方案
import collections
import json
tree = lambda : collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"  # 正常运行
print(json.dumps(some_dict))  # {"colours": {"favourite": "yellow"}}

