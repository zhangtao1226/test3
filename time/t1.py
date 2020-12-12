
import time
import pandas

s = time.time()

print(type(s))
print(type(str(s)))


t = time.localtime(s)
print(t)