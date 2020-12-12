from lxml import etree

html = etree.parse('./text.html', etree.HTMLParser())
print(html, '类型：', type(html))

# 返回所有节点
all_result = html.xpath('//*')  # 返回列表
print('返回所有节点: ', all_result, '返回类型: ', type(all_result))
for node in all_result:
    print(node, '类型: ', type(node))