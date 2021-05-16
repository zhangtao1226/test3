# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 15:50
# @Author  : zhangtao
# @File    : get_test.py
# @Software: PyCharm

import requests

def get_test_1():

    r = requests.get('https://httpbin.org/get')
    print(r.text)
# get_test_1()
"""
结果运行如下：
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.25.1", 
    "X-Amzn-Trace-Id": "Root=1-609e2c26-776b6ff43727827b19dfb3c5"
  }, 
  "origin": "221.231.194.110", 
  "url": "https://httpbin.org/get"
}
"""

def get_params_test():
    url = 'https://httpbin.org/get'
    params = {
        'name': 'geekdigging',
        'age': 18
    }

    response = requests.get(url=url, params=params)
    print(response.text)
    print(type(response.text))
    print(response.json())
    print(type(response.json()))
# get_params_test()
"""
运行结果如下：
{
  "args": {
    "age": "18", 
    "name": "geekdigging"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.25.1", 
    "X-Amzn-Trace-Id": "Root=1-609e2d8a-5722402817ed4baf47c36108"
  }, 
  "origin": "221.231.194.110", 
  "url": "https://httpbin.org/get?name=geekdigging&age=18"
}

<class 'str'>
{'args': {'age': '18', 'name': 'geekdigging'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.1', 'X-Amzn-Trace-Id': 'Root=1-609e2d8a-5722402817ed4baf47c36108'}, 'origin': '221.231.194.110', 'url': 'https://httpbin.org/get?name=geekdigging&age=18'}
<class 'dict'>
"""

# 抓取图片（视频）
def get_image_test():
    url = 'https://www.baidu.com/img/superlogo_c4d7df0a003d3db9b65e9ef0fe6da1ec.png'
    r = requests.get(url)
    with open('image.png', 'wb') as f:
        f.write(r.content)
# get_image_test()

# post 请求
def post_test():
    url = 'https://httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'referer': 'https://www.geekdigging.com/'
    }

    params = {
        'name': 'geekdigging',
        'age': 90
    }

    r = requests.post(url, params, headers)
    print(r.text)
# post_test()
"""
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "age": "90", 
    "name": "geekdigging"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.25.1", 
    "X-Amzn-Trace-Id": "Root=1-609e30c5-7b44aa9c557b69516a0bb40f"
  }, 
  "json": null, 
  "origin": "221.231.194.110", 
  "url": "https://httpbin.org/post"
}

"""

# -----------------------------

"""
Response 响应
"""
def response_type():
    r = requests.get('https://www.baidu.com')
    print(type(r.status_code), r.status_code)  # 状态码
    print(type(r.headers), r.headers)  # 响应头
    print(type(r.cookies), r.cookies)  # Cookie
    print(type(r.url), r.url)  # URL
    print(type(r.history), r.history)  # 请求历史
# response_type()
"""
运行结果如下：
<class 'int'> 200
<class 'requests.structures.CaseInsensitiveDict'> {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Fri, 14 May 2021 08:16:43 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:23:55 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
<class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
<class 'str'> https://www.baidu.com/
<class 'list'> []
"""

# ---------------------------
"""
超时设置
timeout 仅对连接过程有效，与响应体的下载无关。timeout 并不是整个下载响应的时间限制，而是如果服务器在 timeout 秒内没有应答，将会引发一个异常
（更精确地说，是在 timeout 秒内没有从基础套接字上接收到任何字节的数据时） if no tomeout is specified explicitly, requests do not time out）
"""

def request_timeout_test():
    url = 'https://www.geekdigging.com/'
    r = requests.get(url, timeout=1)
    print(r.status_code)
# request_timeout_test()

# --------------------------
"""
代理设置
"""
def request_proxies():
    proxies = {
        'http': 'http://10.10.1.10:3128',
        'https': 'https://10.10.1.10:1080'
    }
    url = 'https://www.geekdigging.com/'
    requests.get(url, proxies=proxies)

def request_proxies_socket():
    proxies_socket = {
        'http': 'socks5://user:pass@host:port',
        'https': 'socks5://user:pass@host:port',
    }

    requests.get('https://www.geekdigging.com', proxies_socket)

# ---------------------------------
"""
Cookies
"""
def request_cookies_test():
    r = requests.get('https://www.csdn.net')
    print(type(r.cookies), r.cookies)
    for key, value in r.cookies.items():
        print(key + ' = ' + value)
# request_cookies_test()
"""
运行结果：
<class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[<Cookie dc_session_id=10_1620983836758.855637 for .csdn.net/>, <Cookie uuid_tt_dd=10_37229533260-1620983836758-562349 for .csdn.net/>, <Cookie csrfToken=RNtvnYn5v3TdaVwGM_Ac5aOz for www.csdn.net/>]>
dc_session_id = 10_1620983836758.855637
uuid_tt_dd = 10_37229533260-1620983836758-562349
csrfToken = RNtvnYn5v3TdaVwGM_Ac5aOz
"""

# 通过 Cookies 维持会话状态

def cookies_status_test():
    headers = {
        'cookie': '_zap=d0580efe-2655-43f3-91dc-6fe85c822700; _xsrf=51781dba-dbe2-4396-b50f-b63724607c2e; d_c0="ABCf12noEhOPTmVZRFBeEOkLx2PwHG7ls5w=|1620466399"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1620466401,1620984060; captcha_session_v2="2|1:0|10:1620984059|18:captcha_session_v2|88:bXNJM0pOYkhvWmRmeW5OdGJkdFkxd0lzeUZHMVBVUlRoOFhLb3M2NnI2c3FYTmlrU0RzeldUQ3hhTXZHY0d3ZA==|b8ec15e09e76a6fa127fc59ba5110d54ac59875d545665afe844df9e18558c10"; SESSIONID=BvkAe6q3hISTXAwdB87414dOmnGpM6aZGxmgDoSByjK; JOID=WlERBk4wWDjzvM_GEz1U6RPWKtgMcyNSstT4uiFVEGam5IOwesAUp56ww8oSQQWYvUunxIsRRYdQ_85GAcgkees=; osd=UV4SBEg7VzvxusTJED9S4hzVKN4HfCBQtN_3uSNTG2ml5oW7dcMWoZW_wMgUSgqbv02sy4gTQ4xf_MxACscne-0=; __snaker__id=KBmjTMyS2qDpsSlT; gdxidpyhxdE=z3yOOTWIqn1k1K5cdm0DWVcP8RYIPcOwh65NzlQu6CK3eegb%2BAqBLry68VWLtccvDnZ68WdgNRbX4ga%5CpUW6yrL9GtivCxsc%5C7d7oLza8n6ueXUcXY6o6cGBOXA%2BB8uXEIyU%5CPUY%5Ct5kI0bmCr%5Cvyd6Jr%2FaZaWR1EWhC3kfAc3YU40Ic%3A1620984961048; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=bre45GLpYD4xMCP8nXXTZmCjYkGA97V%2BQuxVamfIKPcSQukLU5rzaNSN%2B9X8KMFlS6%2FuXh6btAU1IaBy6PPjf2b8NVKwWlvEcxS7%2BifgNgyFH3xdoi%2B5o6%2B%2Fff6B8Bp2R2Y%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea8f047aa9485d6b161ba8a8bb2d44a969f9aaaaa3babed97b4ca6eafab8dd0f12af0fea7c3b92aa2aeabd5b84d90b097a5b7748f9da0d9ed549c8c968ec2629bb589a2bc3d96f59f96fb5ea3b3aaaaca5ca18d9f96ea4897ebbe9be4469192e5dadb3489938a8dd23eedab9889b56ab89f9bd2cc6b82a7fab1d362a6eeaed9cd5e89a9998df54fa1a89dd8aa63a6b98288fc4e8cedb885ee63e9eba1d7aa25a6bafaa3bb4ab4ee9ed3dc37e2a3; YD00517437729195%3AWM_TID=pf9QSY0WN9hEVFFUUBIukzmZHOaz6Dq%2F; captcha_ticket_v2="2|1:0|10:1620984080|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfLXU3a1YxdGQyRmx2eEVxeG5xWUxCNmxEZ0dhTDF2d1VYNnhZaU4wSW81LUJWY24xbFJoUG1YX1BSMUlJYlFjUy1mX2Q5RzBmUG0yMmJIRkJ4TFZZRTZxREZnZXVtLXlFX05MRkFzQVFJSE9ZNlBXeHFQMkdEMGQxLlI2OXdFNGpuSGtJbTA0cnBDQmpqUXhjb3dHMTFoRHlURnpGN29XTWFZNWJxWl9Land1cEtkZC11ZHhzMGxONm52VU1yUmlwTmxIdjVXNF91bGp6eUxJdFBFT0FaZUxVb3pYRmtxcHFJOUxCYm1rdnR4aEIxMkQ5T0pmdmlDaXBLN1pubUJNZmM4cUFrV21XNGoudkxzTi1sMlNWaG94VkhlbzAxa0Q2SFFxaXFUVXlUNDg1R2NBVDg3VHg1enh3LlVuV1VYYWwyNHBENGNva21NSkNFQzFXbE5TWjkwRXNILlFHNk1CNlVQa3ZFVl9xLkgxaGN6N3dER1RYS2JDU21LWkxNQW9jUUtRQWpRbFF3djhaSFNkYzdZVzdtaUxXZDR4MFRYZEwtc1VWQXFpbmhROWNISG9VQmpTZFlwWHQyVGtWNS1TZHVQR2lsSi5GVTJmekRZTXZrQTdaYUl0TU5RcmZqeE8ueC14ai5JZDh1bGl1TWVoTGUya2x5aTVCcWZxMyJ9|eab2d49f918d6550522b5db29872e0ce86c8d6fd22225a98a567526862baa33a"; z_c0="2|1:0|10:1620984080|4:z_c0|92:Mi4xWTVXWkF3QUFBQUFBRUpfWGFlZ1NFeVlBQUFCZ0FsVk5FSS1MWVFDRnRIaU1ITXFIZWFLUmtNYXhzUENkLThXYzJ3|65a30903df505197cfe2d234679e44ad189cd4db0ccc02614cee350ab586331f"; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1620984087; KLBRSID=b33d76655747159914ef8c32323d16fd|1620984095|1620984058',
        'host': 'www.zhihu.com',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    r = requests.get('https://www.zhihu.com', headers=headers)
    print(r.status_code)
    print(r.text)
# cookies_status_test()

# 构造 cookies ，并构建 RequestsCookiesJar 对象
def create_cookies_jar():
    cookies = '_zap=7c875737-af7a-4d55-b265-4e3726f8bd30; _xsrf=MU9NN2kHxdMZBVlENJkgnAarY6lFlPmu; d_c0="ALCiqBcc8Q-PTryJU9ro0XH9RqT4NIEHsMU=|1566658638"; UM_distinctid=16d16b54075bed-05edc85e15710b-5373e62-1fa400-16d16b54076e3d; tst=r; q_c1=1a9d0d0f293f4880806c995d7453718f|1573961075000|1566816770000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1574492254,1574954599,1575721552,1575721901; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330; CNZZDATA1272960301=1829573289-1568039631-%7C1575793922; capsion_ticket="2|1:0|10:1575798464|14:capsion_ticket|44:M2FlYTAzMDdkYjIzNDQzZWJhMDcyZGQyZTZiYzA1NmU=|46043c1e4e6d9c381eb18f5dd8e5ca0ddbf6da90cddf10a6845d5d8c589e7754"; z_c0="2|1:0|10:1575798467|4:z_c0|92:Mi4xLXNyV0FnQUFBQUFBc0tLb0Z4enhEeVlBQUFCZ0FsVk53eFRhWGdBSlc3WFo1Vk5RUThBMHMtanZIQ2tYcGFXV2pn|02268679f394bd32662a43630236c2fd97e439151b0132995db7322736857ab6"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1575798469'

    jar = requests.cookies.RequestsCookieJar()

    for cookie in cookies.split(';'):
        key, value = cookie.split('=', 1)
        jar.set(key, value)

    headers_request = {
        'host': 'www.zhihu.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    r = requests.get('https://www.zhihu.com', cookies=jar, headers=headers_request)
    print(r.status_code)
    if r.status_code == 200:
        print(r.text)
# create_cookies_jar()


# 会话维持 -- Session

def hold_cookies_test():
    requests.get('https://httpbin.org/cookies/set/number/123456789')
    r = requests.get('https://httpbin.org/cookies')
    print(r.text)
hold_cookies_test()
"""
运行结果如下：
{
  "cookies": {}
}
"""

def hold_cookies_by_session():
    s = requests.Session()
    s.get('https://httpbin.org/cookies/set/number/123456789')
    r = s.get('https://httpbin.org/cookies')
    print(r.text)
hold_cookies_by_session()
"""
{
  "cookies": {
    "number": "123456789"
  }
}
利用 Session 可以做到模拟同一个会话而不用手动设置 Cookies
"""
