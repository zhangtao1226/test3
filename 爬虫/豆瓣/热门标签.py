import requests
from bs4 import BeautifulSoup

class HotLabel:
    """
    豆瓣热门标签
    """
    def __init__(self, url, header):
        self.url = url
        self.header = header

    def get_html(self):
        respone = requests.get(self.url, headers=self.header).text
        html = BeautifulSoup(respone, 'lxml')
        return html


    def get_element(self, html):
        soup = html.find_all(name='table', attrs={'class':'tagCol'})
        tag_list = []
        for el in soup:
            a_tag_list = []
            for td in el.select('td'):
                tag_dict = {}
                tag_dict['href'] = td.a.attrs['href']
                tag_dict['name'] = td.a.string
                tag_dict['number'] = td.b.string.strip('()')
                a_tag_list.append(tag_dict)
            tag_list.append(a_tag_list)
        return tag_list

    def get_tag_type(self, html):
        soup = html.find_all(name='a', attrs={'class': 'tag-title-wrapper'})
        tag_type_list = []
        for s in soup:
            tag_type_list.append(s.attrs['name'])
        return tag_type_list

if __name__ == '__main__':
    url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-hot'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    hotLable = HotLabel(url, headers)
    html = hotLable.get_html()
    # print(html)
    # tag_list = hotLable.get_element(html)

    # print(tag_list)
    tag_type_name_list = hotLable.get_tag_type(html)
    print(tag_type_name_list)

