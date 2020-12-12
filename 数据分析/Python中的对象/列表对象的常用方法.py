

def listAppend():
    list1 = [1, 2, 3]
    list1.append(4)
    list1.append([3,3])
    print(list1)

# listAppend()

def listCount():
    list1 = [1,2,2,2]
    list1 = [1,2,2,2]
    print(list1.count(2))

# listCount()

'''
列表推导式
[生成列表元素的表达式 for 表达式中的变量 in 变量要遍历的序列]
[生成列表元素的表达式 for 表达式中的变量 in 变量要遍历的序列 if 过滤条件]

注：
    1、要把生成列表元素的表达式放到前面，执行时，先执行后面的 for 循环
    2、可以有多个 for 循环，也可以在 for 循环后面添加 if 过滤条件
    3、变量要遍历的序列，可以是任何方式的迭代器（元组、列表、生成器）
'''



