'''
compile() 该方法将正则字符串编译成正则表达式对象
'''

import re
content1 = '2020-08-05 12:00:00'
content2 = '2020-08-05 12:00:01'
content3 = '2020-08-05 12:00:02'

pattern = re.compile('\d{2}:\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)

print(result1, result2, result3)
