f = open('somefile.txt')
print('1:' + f.read(7))
f.close()

f1 = open('somefile.txt')
print('2：' + f1.read())
f1.close()

f2 = open('somefile.txt')
print('3：' + f2.readline())
f2.close()

import pprint
f3 = open('somefile.txt')
pprint.pprint(f3.readlines())

print(type(f3.readlines()))

