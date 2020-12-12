'''
set 集合与列表（list）类似，区别在于 set 不能包含重复的值
'''

def set_fun():

    some_list = ['a', 'b', 'c', 'a']

    print(set(some_list))

# 交集(intersection）
def set_intersection():
    l = ['1', '2', 3, 4,'a']
    l_2 = ['1', 1, 2]
    print(set(l_2).intersection(set(l)))

# set_intersection()

# 差集(difference), 相当于用一个集合减去另一个集合
def set_difference():
    l_1 = set(['1', 2, 3, 'a'])
    l_2 = set(['2', 3])
    print(l_2.difference(l_1))
set_difference()

