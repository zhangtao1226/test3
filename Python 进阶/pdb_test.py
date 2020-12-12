'''
debugger 模式下的命令列表：
1、c : 继续执行。
2、w : 显示当前正在执行的代码行的上下文信息。
3、a : 打印当前函数的参数列表。
4、s : 执行当前代码行，并停在第一个能停的地方（相当于单步进入）
5、n : 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）
'''
import pdb

def make_bread():
    for i in range(10):
        pdb.set_trace()
        print(i)


print(make_bread())