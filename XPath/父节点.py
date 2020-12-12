'''
# .. 选取当前节点的父节点
'''
from lxml import etree
html = etree.parse('text.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@name') # 所有 a 节点中属性为 link4.html 节点的 父节点的属性 class
print(result)


# 通过 parent:: 获取父节点

result_2 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result_2)