# items = [1, 2, 3, 4]
# sq = map(lambda x: x**2, items) # 可迭代 map 对象
# print(sq)
#
# for i in iter(sq):
#     print(i)

# a = lambda x: x+2

# lst = ['one', 'two', 'three', 'four', 'five', 'six']
#
# l1 = sorted(lst, key=lambda x:len(x), reverse=True)
#
# print(l1)

# lst1 = [1, 2, 3, 4, 5, 6]
# lst2 = ['醉乡民谣', '驴得水', '放牛班的春天', '美丽人生', '辩护人', '被嫌弃的松子的一生']
# lst3 = ['美国', '中国', '法国', '意大利', '韩国', '日本']
#
# print(zip(lst1, lst2, lst3))
#
# for el in zip(lst1, lst2, lst3):
#     print(el)

# def func(i):
#     return i % 2 == 1
#
# lst = [1, 2, 3, 4, 5, 6]
#
#
# l1 = filter(func, lst)
# l2 = filter(lambda x:x % 2==0, lst)
# print(l1)
# print(list(l1))
# print(l2)
# print(list(l2))

# lst = [1, 2, 3, 4]
# it = map(lambda x: x, lst)
# print(it)
#
# for i in it:
#     print(i)
#
lst = [1, 2, 3, 4, 5, 6]
it = iter(lst)
print(it, it.__next__())
print(next(it))
print(next(it))
print(next(it))
