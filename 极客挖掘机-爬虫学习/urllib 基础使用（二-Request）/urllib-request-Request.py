# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 17:33
# @Author  : zhangtao
# @File    : urllib-request-Request.py
# @Software: PyCharm

"""
Request 用法：
urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
参数：
url：请求的地址链接，只有这个是必传参数，其余都是可选参数；
data：如果这个参数需要传递，则必须传 bytes（字节流）类型的；
headers：请求头信息，它是一个字典，可以在构造请求的时候通过headers之间构造，也可以调用 add_header() 添加
origin_req_host：发起请求一方的 host 名称或者也可以是 ip 地址；
unverifiable：值得是这个请求是否无法验证的，默认是 False。
method：请求方法，如：GET、POST、PUT、DELETE等。
"""
import urllib.request
import urllib.parse
import json

def urllib_request_Request():
    url = 'https://www.geekdigging.com'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))
# urllib_request_Request()

def urllib_request_Request_2():
    url = 'https://httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Content-Type': 'application/json;encoding=utf-8',
        'Host': 'geekdigging.com',
    }
    data = {
        'name': 'geekdigging',
        'hello': 'world',
    }
    print(type(json.dumps(data)))
    data = bytes(json.dumps(data), encoding='utf8')
    req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
    resp = urllib.request.urlopen(req)
    print(resp.read().decode('utf-8'))
# urllib_request_Request_2()

"""
输出结果如下：
{
  "args": {}, 
  "data": "{\"name\": \"geekdigging\", \"hello\": \"world\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Content-Length": "41", 
    "Content-Type": "application/json;encoding=utf-8", 
    "Host": "geekdigging.com", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-609b3877-04c373fe0e134ddf6520fada"
  }, 
  "json": {
    "hello": "world", 
    "name": "geekdigging"
  }, 
  "origin": "114.222.120.187", 
  "url": "https://geekdigging.com/post"
}
"""

# 进阶操作
"""
前面我们使用 REquest 完成了请求头的添加，如果我们想处理 Cookie 和使用代理访问，就需要使用到更加强大的 Handler。Handler 可以简单理解为各种功能
的处理器，使用它，几乎可以为我们做到所有有关 HTTP 请求的事情。

urllib.request 为我们提供了 BaseHandler 类，它是所有其他 Handler 的父类，它提供了直接使用的方法如下：
    1、add_parent()：添加 director 作为父类；
    2、close(): 关闭它的父类；
    3、parent(): 打开使用不同的协议或处理错误；
    4、default_open(): 捕获所有的 URL 及子类，在协议打开之前调用；

各种 Handler 子类集成这个 BaseHandler 类：
    1、HTTPDefaultErrorHandler: 用来处理 http 响应错误，错误会抛出 HTTPError 类的异常；
    2、HTTPRedirectHandler: 用于处理重定向；
    3、ProxyHandler: 用于设置代理，默认代理为空；
    4、HTTPPasswordMgr: 用于管理密码，它维护用户名和密码表；
    5、AbstractBasicAuthHandler: 用于获取用户名/密码，然后重试请求来处理身份验证请求；
    6、HTTPBasicAuthHandler: 用户重试带有身份认证信息的请求；
    7、HTTPCookieProcessor: 用于处理 cookies；
等，urllib 为我们提供的 BaseHandler 子类非常多，详细官网文档：https://docs.python.org/zh-cn/3.7/library/urllib.request.html#basehandler-objects


高级类：OpenerDirector
OpenerDirector 是用来处理 URL 的高级类，它分三个阶段来打开 URL：
    在每个阶段中调用这些方法的顺序是通过对处理程序实例进行排序来确定的，每个使用此类方法的程序都会调用 protocol_request() 方法来预处理请求，然
调用 protocol_open() 来处理请求；最后调用 protocol_response() 方法来响应。

我们可以称 OpenerDirector 为 Opener 。之前用过 urlopen() 这个方法，实际上他就是 urllib 尾门提供的一个 Opener。
Opener 的方法包括：
    1、add_handler(handler): 添加处理程序到链接中；
    2、open(url, data=None[,timeout]): 打开给定的 URL 与 urlopen() 方法相同；
    3、error(proto, *args): 处理给定协议的错误；
"""
import http.cookiejar
import urllib.request

def handler_class_test():
    # 实例化cookiejar对象
    cookie = http.cookiejar.CookieJar()
    # 使用 HTTPCookieProcessor 构建一个 handler
    handler = urllib.request.HTTPCookieProcessor(cookie)
    # 构建 Opener
    opener = urllib.request.build_opener(handler)
    # 发起请求
    response = opener.open('https://www.baidu.com/')
    print(cookie)
    for item in cookie:
        print(item.name + ' = ' + item.value)

# handler_class_test()
"""
运行结果如下：
<CookieJar[<Cookie BAIDUID=738F2CF973DDF2495AB0B10C3611732A:FG=1 for .baidu.com/>, <Cookie BIDUPSID=738F2CF973DDF249EBF88C838861A764 for .baidu.com/>, <Cookie PSTM=1620786920 for .baidu.com/>, <Cookie BD_NOT_HTTPS=1 for www.baidu.com/>]>
BAIDUID = 738F2CF973DDF2495AB0B10C3611732A:FG=1
BIDUPSID = 738F2CF973DDF249EBF88C838861A764
PSTM = 1620786920
BD_NOT_HTTPS = 1
"""

def cookies_save_mozilla():
    filename = 'cookies_mozilla.txt'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)
    print('cookies_mozilla 保存成功')
# cookies_save_mozilla()

def cookies_save_LWP():
    filename = 'cookies_lwp.txt'
    cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opender = urllib.request.build_opener(handler)
    response = opender.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)
# cookies_save_LWP()

def load_local_cookie_test():
    cookie = http.cookiejar.MozillaCookieJar()
    cookie.load('cookies_mozilla.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))
load_local_cookie_test()