'''
通过 @ 符 获取选取属性
'''
from lxml import etree
html = etree.parse('text.html', etree.HTMLParser())
result = html.xpath('//li/@class')
print(result)
print('set 集合去重：', set(result)) # set() 集合去重

result_2 = html.xpath('//li/a/@href')
print(result_2)