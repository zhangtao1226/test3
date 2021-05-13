# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 16:02
# @Author  : zhangtao
# @File    : httperror.py
# @Software: PyCharm

from urllib import request, error

# 访问明显不存在的地址，使用 HTTPError 捕捉异常
def http_error_test():
    try:
        response = request.urlopen('https://www.geekdigging.com/aa')
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
# http_error_test()
"""
运行结果如下：
Not Found
404
Server: nginx
Date: Wed, 12 May 2021 08:04:29 GMT
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: close
X-Powered-By: PHP/7.4.0
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Cache-Control: no-cache, must-revalidate, max-age=0
Link: <https://www.geekdigging.com/wp-json/>; rel="https://api.w.org/"
"""

"""
因为 URLError 是 HTTPError 的父类，所以可以先选择捕获子类的错误，再去捕获父类的错误，这样对异常的处理更具针对性。
注意：捕捉异常一般先捕捉子类异常，在捕捉父类异常
"""

# 先捕捉子类异常，再捕捉父类异常
def http_error_2():
    try:
        response = request.urlopen('https://www.geekdigging.com/aa')
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
    except error.URLError as e:
        print(e.reason)
    else:
        print('Request Success!')
http_error_2()