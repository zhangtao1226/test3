'''
问题： 在迭代或其他形式的处理过程中对最后几项纪录做一个有限的历史纪录统计
解决方案：保存有限的历史纪录可算是 collections.deque 的完美应用场景
'''

from collections import deque

"""
下面代码对一系列文本行做简单的文本匹配操作，当发现有匹配是就输出当前的匹配行以及最后检查过的 N 行文本
"""
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
        print('1、', previous_lines)


if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, '安康', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)