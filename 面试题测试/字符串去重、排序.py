import json

s = 'ajldjlajfdljfdd'
print('这是字符串：', s, type(s))

set_s = set(s)

print('这是集合：', set_s, type(set_s))

list_s = list(set_s)
print('这是列表：', list_s, type(list_s))
list_s.sort(reverse=False)
print('排序后的列表 ：', list_s, type(list_s))

str_s = ''.join(list_s)

print('这是字符串：', str_s, type(str_s))