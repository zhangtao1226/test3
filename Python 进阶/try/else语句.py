"""
try / else: else 从句只会在没有异常的情况下执行，而且它会在 finally 语句前执行。
"""

try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # 这里的代码只会在 try 语句里没有触发异常时运行，但是这里的异常不会被捕获
    print('This wourld only run if no exception occurs. And an error would NOT be caught')
finally:
    print("this wourld be printed in every case")
