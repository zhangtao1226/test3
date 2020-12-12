'''
sorted() 函数对所有可迭代的对象进行排序操作。
语法：
sorted(iterable, cmp=Nome, key=None, reverse=False)
参数说明：
1、iterable ：可迭代对象；
2、cmp ：比较的函数，这个具有两个参数，参数的值都是从可迭代对象去出，此函数必须遵守的规则为，大于则返回1 ，小于则返回-1， 等于则返回0.
3、key ：主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代法对象中，指定可迭代对象中的一个元素进行排序。
4、reverse ：排序规则，reverse = True 降序，reverse = False 升序（默认）。
返回值：
返回重新排序的列表

sort 和 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。list 的sort 方法返回的是对已经存在的列表进行操作，无返回值
而内建函数 sorted 方法返回的是一个新的 list ，而不是在原来的基础上进行的操作。
'''
dic = {
    'name': 'tao',
    'age': 18,
    'city': '南京',
    'tel': '18115169459'
}
print(dic.items())


lis = sorted(dic.items(), key=lambda item: item[0], reverse=False)

print(lis)
new_dict = {}
for i in lis:
    new_dict[i[0]] = i[1]

print(new_dict)