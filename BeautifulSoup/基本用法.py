"""
关联选择：获取某个节点的子节点、父节点、兄弟节点等。
"""

from bs4 import BeautifulSoup

html = """
    <html>
        <head>
            <title> The Dromouse's story</title>
        </head>
        <body>
            <p class="story">
                Once upon a time there were little sisters; and their names were
                <a href="http://example.com/elsis" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
                <a href="http://example.com/lacie" class="sister" id="link3">Tillie</a>
            </p>
            <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# print(soup.p.children)
# for child in enumerate(soup.p.children):
#     print(child)
#
# for child in enumerate(soup.p.descendants):
#     print(child)


def get_by_select():
    list_element = soup.select('p')
    return list_element
# for i, e in enumerate(get_by_select()):
#     print(e.children, type(e.children)) # 返回生成器
#     # for c in e.children:
#     #     print(c)
#     print(e.descendants)

def get_by_a_parent():
    a_parent = soup.a.parent
    return a_parent

print(get_by_a_parent().attrs)