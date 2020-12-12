"""
for-else : 循环
"""

def demo_1():
    fruits = ['apple', 'banana', 'mango']
    for fruit in fruits:
        print(fruit, fruit.capitalize()) # capitalize()将字符串的第一个字母变成大写,其他字母变小写。
# demo_1()


"""
else 从句：会在循环正常结束时执行。
"""

def demo_2():
    container = [1, 2, 3, 4]
    for item in container:
        if item % 2 == 0:
            print(item)
            break
        else:
            print(item)
    else:
        print('ending')

demo_2()
