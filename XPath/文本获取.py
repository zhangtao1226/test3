'''
XPath 中的 text() 方法获取节点中的文本
'''
from lxml import etree
html = etree.parse('text.html', etree.HTMLParser())

# 利用 / 获取直接子节点 a
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

# 利用 // 获取所有子孙节点
result_2 = html.xpath('//li[@class="item-0"]//text()')
print(result_2)

