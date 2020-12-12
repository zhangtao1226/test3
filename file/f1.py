import shelve
import json

s = shelve.open('test.txt')
s['x'] = ['a', 'b', 'c']

print(s['x'])
print(id(s['x']))

# tem = s['x']
# tem.append('d')
#
# print(tem)
#
# s['x'] = tem
s['x'].append('d')
# print()

print(s['x'])
print(id(s['x']))
