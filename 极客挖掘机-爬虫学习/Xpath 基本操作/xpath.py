# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 18:04
# @Author  : zhangtao
# @File    : xpath.py
# @Software: PyCharm

import requests
from lxml import etree

def xpath_show_test():
    response = requests.get('https://www.geekdigging.com')
    # print(type(response), response)  # <class 'requests.models.Response'> <Response [200]>
    # print(type(response.content), response.content)  # <class 'bytes'> b'.......'
    html_str = response.content.decode('utf-8')
    # print(type(html_str), html_str)  # <class 'str'  '<!DOCTYPE html> ...'
    html = etree.HTML(html_str)
    result = etree.tostring(html, encoding='utf-8').decode('utf-8')
    # print(type(result), result)  # <class 'str'>  <html lang="zh-CN"> ...
# xpath_show_test()
    return html
"""
注：使用 request 获取页面的源代码 byte 数据流，解释使用 decode() 进行解码，解码后将字符串传入 etree.HTML() 构建
一个 lxml.etree._Element 对象，然后对这个对象做 tostring() 转换字符串并且进行打印
另：使用 tostring() 进行转化字符串的时候，一定需要添加参数 encoding,否则中文将会显示为 Unicode 编码
"""


# 所有节点
def get_all_element():
    html = xpath_show_test()
    result = html.xpath('//*')
    print(result)
get_all_element()
"""
运行结果如下：
[<Element html at 0x11a2da4c0>, <Element head at 0x11adf0740>, ...]
解释：
 * 代表匹配所有节点，也就是当前的html 中的所有节点都会被获取。
 返回形式是一个列表，每个元素是 Element 类型，其后根了节点的名称，如：html、head、meta等，所有节点都包含在列表中。
 
 也可指定节点名称，如：
 result = html.xpath('//meta')
"""

# 子节点 ： 获取子节点一般可以使用 / 或者 // 来获取子节点或者孙子节点
"""
1、获取 <main> 下面的 <article>
result = html.xpath('//main/article') / 是用于获取子节点
2、获取孙子节点
result = html.xpath('//main//div') // 获取 main 下面所有 div 节点
"""

# 父节点 ： 一般可以通过 .. 或 parent::
"""
1、<a target='_blank' href='/test/'><img class='img' src='aa'></a>
result = html.xpath('//img[@src='aa'/../@href]
结果：['/test/']
2、result = html.xpath('//img[@src='aa']/parent::*/@href)
"""

# 属性过滤 : 使用 @ 符号进行属性过滤
"""
result = html.xpath('//section/div[@class='container']')
"""

# 属性获取 : 一般用 @ + 属性名称，如 @href ，获取href值





