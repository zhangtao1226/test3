'''
ncalls : 执行次数
tottime : 总执行时间（排除子函数执行时间）。
percall : 平均每次执行时间（ tottime / ncalls）。
cumtime : 累计执行时间（包含子函数执行时间）。
percall : 平均每次执行时间（ cumtime / ncalls ，递归调用只记一次）。
filename : lineno(function) : 具体执行内容说明，比如：{method 'append' of 'list' objects}
'''

import cProfile
import pstats
from io import StringIO

pr = cProfile.Profile()

def loop(count):
    result = []
    for i in range(count):
        result.append(i)

pr.enable()
loop(100000)
pr.disable()
s = StringIO()
sortby = 'tottime'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())