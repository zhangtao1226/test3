'''
通过 contains() 方法，第一个参数传入属性名称，第二个参数传入属性值，只要把此属性包含
所传入的的属性值，既可以完成匹配
'''

from lxml import etree
html = etree.parse('text.html', etree.HTMLParser())
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)

'''
多属性匹配
'''
text = '''
    <li class="li li-first" name="item"><a href="link.html">first item</a></li>
    <li class="li li-second"><a href="link2.html">second item</a></li>
'''
html = etree.HTML(text)
result_2 = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result_2)