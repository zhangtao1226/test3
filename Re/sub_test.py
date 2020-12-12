'''
sub() 修正文本。
'''
import re

content = '54hdjfu86b2bdudm9762b'
new_content = re.sub('\d+', '', content) # 去除 content 中的数字
print(new_content)