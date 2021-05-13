# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 16:12
# @Author  : zhangtao
# @File    : parse_1.py
# @Software: PyCharm
"""
urllib.parse 模块定义的函数分为两大类：URL 解析和 URL 引用。
1、URL 解析
    urlparse() ： 该方法主要用于识别 URL 和将其分段。
    urlparse 对于一个 URL 的定义：
    scheme://netloc/path;parameters?query#fragment, 由其可以看出，urlparse() 将一个 URL 拆解成 6 个部分，分别是：
        1、scheme: 位于 :// 前面，代表了当前的协议；
        2、netloc: 位于第一个 / 之前，代表了域名；
        3、path: 位于第一个 / 和 ； 之间，代表了访问路径；
        4、parameters: 位于 ; 和 ？之间，代表了路径元素的参数；
        5、query: 位于 ？ 和 # 之间，代表了查询组件；
        6、fragment: 位于 # 之后，代表了判断识别；
"""
from urllib.parse import urlparse
# urlparse 解析链接
def parse_test_1():
    result = urlparse('https://docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse')
    print(result)  # ParseResult(scheme='https', netloc='docs.python.org', path='/zh-cn/3.7/library/urllib.parse.html', params='', query='', fragment='module-urllib.parse')

    print(type(result))  # <class 'urllib.parse.ParseResult'>
# parse_test_1()
"""
运行结果如上注释，可以通过 result.netloc 方式获取或者通过索引的方式 result[1] 方式获取对应值
属性          索引          描述              值（如果不存在）
scheme        0          URL 方案说明符      scheme parameter
netloc        1          域名                 空字符串
path          2          分层路径              空字符串
params        3          最后路径元素的参数      空字符串
query         4          查询组件              空字符串
fragment      5          判断识别              空字符串
"""

"""
urllib.parse.urlparse(url[string], scheme='', allow_fragments=True)
    1、url: 这是必填项，即带解析的 URL；
    2、scheme: 它是默认的协议（比如：http 或 https）。假如这个链接没有带协议信息，会将这个作为默认协议；
    3、allow_fragments: 即是否忽略 fragment。如果他被设置为 False，fragment 部分就会被忽略，它会被解析为 path、
    parameters 或者 query 的一部分，而 fragment 部分为空。
"""

# allow_fragment = False
def parase_fragment_false():
    result = urlparse('docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse', scheme="https",
                      allow_fragments=False)
    print(result)  # ParseResult(scheme='https', netloc='', path='docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse', params='', query='', fragment='')
# parase_fragment_false()
"""
运行结果如下：
ParseResult(scheme='https', netloc='', path='docs.python.org/zh-cn/3.7/library/urllib.parse.html#module-urllib.parse', params='', query='', fragment='')
可以看出，scheme 信息是正常识别出来，而片段识别的信息则被解析成为了 path 的一部分
"""

from urllib.parse import urlunparse

# urlunparse 构建链接, 这个方法接受的参数是一个可迭代对象，但是它的长度必须是 6，否则会抛出参数数量不足或过多问题
def urlunparse_test_1():
    params = ('https', 'www.geekdigging.com', 'index.html', 'people', 'a=1', 'geekdigging')
    print(urlunparse(params))
# urlunparse_test_1()
"""
运行结果如下：
https://www.geekdigging.com/index.html;people?a=1#geekdigging

注：在构建 URL 时， 如果其中某些参数在构建的时候不存在，不可不写，需留出空字符串即可，如下：
params = ('https', 'www.geekdigging.com', 'index.html', '', '', 'geekdigging')
"""
# -----------------------------------------------------

"""
urlsplit() 这个方法和 urlparse() 非常像，唯一区别就是 urlsplit() 不再单独解析 params 这个组件，只会返回 5 个组件的结果，它将 params 合
并到 path 中。
"""
from urllib.parse import urlsplit

def urlsplit_test_1():
    result_urlsplit = urlsplit('https://www.geekdigging.com/index.html;people?a=1#geekdigging')
    print(type(result_urlsplit))
    print(result_urlsplit)
# urlsplit_test_1()
"""
运行结果如下：
<class 'urllib.parse.SplitResult'>
SplitResult(scheme='https', netloc='www.geekdigging.com', path='/index.html;people', query='a=1', fragment='geekdigging')
返回的结果时 urllib.parse.SplitResult ，它其实是一个元组类型，既可以用属性获取值，也可以用索引来获取。
示例如下：
print(result_urlsplit.netloc)
print(result_urlsplit[1]
"""

# -----------------------------------------------------------

"""
urlunsplit() 和 urlunparse(）相似，唯一的区别就是他的参数长度必须为 5.
"""
from urllib.parse import urlunsplit

def urlunsplit_test_1():
    params_urlunsplit = ('https', 'www.geekdigging.com', 'index.html;people', 'a=1', 'geekdigging')
    print(urlunsplit(params_urlunsplit))
# urlunsplit_test_1()
"""
运行结果如下：
https://www.geekdigging.com/index.html;people?a=1#geekdigging
"""

# --------------------------------------------------------------------------------
"""
urljoin() 介绍：
通过基础的 URL 和 另一个 URL 来完成组合最终的 URL，它会分析基础的 URL 的 scheme、netloc、path 三个内容，并对新连接缺失的部分进行补充，完成
最终的 URL。示例如下：
print(urljoin("https://www.geekdigging.com/", "index.html"))
print(urljoin("https://www.geekdigging.com/", "https://www.geekdigging.com/index.html"))
print(urljoin("https://www.geekdigging.com/", "?a=aa"))
print(urljoin("https://www.geekdigging.com/#geekdigging", "https://docs.python.org/zh-cn/3.7/library/urllib.parse.html"))

运行结果如下：
https://www.geekdigging.com/index.html
https://www.geekdigging.com/index.html
https://www.geekdigging.com/?a=aa
https://docs.python.org/zh-cn/3.7/library/urllib.parse.html

解释：只有在第二个参数链接缺失 scheme、netloc、path 这三个内容的时候，才会从第一参数中获取对应的内容进行组合
"""

# ------------------------------------------------
"""
parse_qs(): 可以将一串 GET 请求中的参数转换成字典。示例如下：
"""
from urllib.parse import parse_qs

def parse_qs_test():
    print(parse_qs('ie=UTF-8&wd=python'))
# parse_qs_test()
"""
运行结果如下：
{'ie': ['UTF-8'], 'wd': ['python']}
"""

# ------------------------------

"""
parse_qsl(): 用于将参数转化为元组组成的列表。
"""
from urllib.parse import parse_qsl

def parse_qsl_test():
    print(parse_qsl("ie=UTF-8&wd=python"))
# parse_qsl_test()
"""
运行结果：
[('ie', 'UTF-8'), ('wd', 'python')]
"""

# --------------------------
"""
URL  引用
    1、urlencode(): 这个方法用来构造 GET 请求参数，可以将一个字典转换成 GET 请求参数。
"""
from urllib.parse import urlencode

def create_url_by_url_encode():
    url = 'https://www.geekdigging.com'
    param_dict = {
        'name': "数据挖掘",
        'age': 18
    }
    print(url + urlencode(param_dict))
create_url_by_url_encode()
"""
运行结果如下：
https://www.geekdigging.comname=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&age=18
将url进行编码，url中的中文参数进行 URL 编码
"""

# ----------------------
"""
quote() urllib.parse 中提供的对 url 中文进行转码
"""
from urllib.parse import quote

def quote_test():
    print(quote("数据挖掘"))
quote_test()  # %E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98

"""
unquote() url 中文解码
print(unquote("%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98"))
"""





