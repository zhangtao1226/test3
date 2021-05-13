# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 10:59
# @Author  : zhangtao
# @File    : urllib_urlerror.py
# @Software: PyCharm

from urllib import request, error

# 访问明显不存在的地址， 报错： Not Found

def request_not_found():
    try:
        response = request.urlopen('https://www.geekdigging.com/aa')
    except error.URLError as e:
        print(e.reason)
# request_not_found()

# 访问超时，报错：timed out
def request_timeout():
    try:
        response = request.urlopen('https://www.baidu.com', timeout=0.001)
    except error.URLError as e:
        print(e.reason)
# request_timeout()
import socket
def request_timeout_2():
    try:
        response = request.urlopen('https://www.baidu.com', timeout=0.001)
    except error.URLError as e:
        # print(type(e))
        if isinstance(e.reason, socket.timeout):
            print('time out')
request_timeout_2()