# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 16:33
# @Author  : zhangtao
# @File    : urllib-exercise.py
# @Software: PyCharm

import urllib.request
import urllib.parse
import socket

"""
urllib 是一个软件包，包含了几个用于处理 URL 的模块：
    1、request：基础的 HTTP 请求模块；
    2、error：异常处理模块；
    3、parse：用于解析 URL 的模块；
    4、robotparser：识别网站中 robots.txt 文件
"""

# urllib.request 模块

"""
urllib.request 模块提供了最基本的构造 HTTP 请求的方法，使用它可以模拟浏览器的一个请求发起过程，同时它还带有处理授权验证（autenentication)、
重定向（redirection)、浏览器Cookies以及其他内容。
语法：
urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)

参数：
cafile 、capath、cadefault 用于实现可信任的 CA 证书的 HTTP 请求，一般很少使用；
context 用来实现 SSL 加密传输；
"""

def urlopen_test():
    url = 'https://www.geekdigging.com'
    response = urllib.request.urlopen(url)
    # print(response.read().decode('utf-8'))
    """
    urlopen 返回一个 HTTPResponse 类型的对象，是对 HTTP 响应的包装。它提供了对请求头和请求体的访问。这个响应是一个可以迭代的对象。
    
    HTTPResponse 主要包含 read() 、readline()、getheader(name)、getheaders()、fileno() 等方法，以及msg、version、status、reason、debuglevel
    closed 等属性。
    """
    print(type(response))

    # 获取 HTTP 协议版本号
    print(response.version)

    # 获取响应码
    print('响应码：', response.status)
    print('响应码：', response.getcode())

    # 获取响应描述字符串
    print('响应字符串：' + response.reason)

    # 获取实际请求的页面url（防止重定向）
    print('页面url：', response.geturl())

    # 获取特定响应头信息
    print('响应头信息-指定信息：', response.getheader(name='Content-Type'))

    # 获取响应头信息，返回二元元组列表
    print('响应头列表：', response.getheaders())

    # 获取响应头信息，返回字符串
    print('响应头信息：', response.info())

    # 读取响应体
    # print(response.readline().decode('utf-8'))



# data
"""
data
用来指明发往服务器请求中的额外的参数信息， data 默认是 None，此时以 GET 方式发送请求；当用户给出 data 参数的时候，改为 POST 方式发送请求。
"""
def urlopen_data():
    url = 'https://httpbin.org/post'
    post_data = bytes(urllib.parse.urlencode({'name': 'geekdigging', 'hello': 'world'}), encoding='utf8')
    # print(post_data)
    response = urllib.request.urlopen(url, data=post_data)
    print(response.read().decode('utf-8'))

# urlopen_data()

def urllib_request_timeout():
    """
    timeout 用于设置超时时间，单位为秒。
    如果请求超出了设置的时间，还未响应，就会抛出异常
    :return:
    """
    try:
        response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
        print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('请求超时！！！')
        else:
            print(e)

urllib_request_timeout()