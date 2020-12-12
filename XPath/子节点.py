from lxml import etree

aa = 'text.html'
print(type(aa))
html = etree.parse(aa, etree.HTMLParser())
result = html.xpath('//ul//a')
if len(result):
    print(result)
    for r in result:
        print(r.text, r, '类型：', type(r))
else:
    print('nothing')