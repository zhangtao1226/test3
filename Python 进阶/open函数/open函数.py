"""
open 函数可以打开一个文件。
例：
    f = open('text.txt', 'r+')
    data = f.read()
    f.close()
    注：该方法调用 close 关闭了这个文件句柄，但是前提是只有在 read 成功的情况下。
    如果有任意异常正好在 f = open(...) 之后产生， f.close() 将不会被调用（这取决
    与 Python 解释器的做法，文件句柄可能还是会被归还，但那时另外的话题）。

为了确保不管异常是否触发，文件都能关闭，将其包裹成一个 with 语句：
    with open('text,txt', 'r+') as f:
        data = f.read()

    open 的第一个参数是文件名。第二个参数为 mode（打开文件模式）
    * r: 读取文件
    * r+ : 读取并写入文件
    * w : 覆盖写入文件
    * a : 在文件末尾追加内容
"""
def read_demo():
    with open('text.txt', 'r') as f:
        text = f.read()
    print(text)

def read_and_write():
    str = '\n' + '这是追加内容\n'
    with open('text.txt', 'r+') as f:
        # text = f.read()
        f.write('\n' + '第二次追加：' + str) # 添加到文件开头位置
read_and_write()