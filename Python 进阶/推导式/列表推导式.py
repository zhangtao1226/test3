"""
列表推导式（又称列表解析式）提供了一种简单的方法来创建列表。
它的结构是在一个中括号里包含一个表达式，然后是一个 for 语句，然后是 0 个或多个 for 或者 if 语句。
那个表达式可以是任意的，意思是你可以在列表中放入任意类型的对象。返回结果将是一个新的列表，在这个以 if 和 for 语句为上
下文的表达式运行完成之后产生。

规范
input_list = []
variable = [out_exp for out_exp in input_list if out_exp == 2]
"""

# 例如：
multiples = [i for i in range(30) if i % 3 is 0]
# print(multiples)  # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]


def created_list_1():
    '''
    普通方法：生成列表
    :return:
    '''
    squared = []
    for x in range(10):
        squared.append(x**2)

    return squared

def create_list_2():
    '''
    列表推导式：生成列表
    :return:
    '''
    squared = [x**2 for x in range(10)]
    return squared

print('普通方法：', created_list_1(), '列表推导式：', create_list_2())