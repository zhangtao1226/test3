'''
Python 标准库 string 中定义了数字、标点符号、英文字母、大写英文字母、小写英文字母等字符串常量
'''

import string

str = ''
# 所有英文字母

def get_all_letters():
    str = string.ascii_letters
    print('所有英文字母：%s' %str)

get_all_letters()

# 所有小写英文字母
def get_all_lower():
    str = string.ascii_lowercase
    print('所有小写英文字母：%s' %str)
get_all_lower()

# 所有大写英文字母
def get_all_upper():
    str = string.ascii_uppercase
    print('所有大写英文字母：%s' %str)
get_all_upper()

# 数字 0-9
def get_digits():
    str = string.digits
    print('数字0-9：%s' %str)
get_digits()

# 十六进制数字
def get_hexdigits():
    str = string.hexdigits
    print('十六进制数：%s'%str)
get_hexdigits()

# 八进制数
def get_octdigits():
    str = string.octdigits
    print('八进制数：%s'%str)
get_octdigits()

# 标点符号
def get_punctation():
    str = string.punctuation
    print('标点符号：%s'%str)
get_punctation()

# 可打印字符
def get_stringPrintable():
    str = string.printable
    print('可打印字符：%s'%str)
get_stringPrintable()

# 生成密码
import random
import string

def create_password(length=8):
    '''
    根据随机方法，生成任意长度密码
    random 模块的 choice()方法返回一个列表、元组或字符串的一个随机元素
    :return:
    '''
    chars = string.ascii_letters + string.digits
    password = ''.join([random.choice(chars) for _ in range(length)])
    print([random.choice(chars) for _ in range(length)])
    return password

passward = create_password(8)
print('生成密码：%s' %passward)

