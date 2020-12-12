import requests
from requests.exceptions import RequestException
from lxml import etree

def get_one_page(url):
    '''
    获取html
    :param url:
    :return:
    '''
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except RequestException:
        return None

def pars_one_page(html):
    '''
    匹配当前页内容
    :param html:
    :return:
    '''
    html_data = etree.HTML(html)
    result = html_data.xpath('')

    if len(result):
        for r in result:

            print(r.text)
    else:
        print("nothing")

if __name__ == '__main__':
    url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
    html = get_one_page(url)
    pars_one_page(html)