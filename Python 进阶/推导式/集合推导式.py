"""
集合推导式和列表推导式类似，唯一的区别在于他们使用的大括号 {} 。
"""
def demo_1():
    squared = {x**2 for x in range(10)}
    print(squared)

demo_1()

def demo_2():
    squared = {x**2 for x in [1, 1, 2]}
    print(squared)
demo_2()