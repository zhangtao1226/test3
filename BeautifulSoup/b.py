from bs4 import BeautifulSoup
import requests

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    html = requests.get(url, headers=headers)
    print(html.text)

# def get_parse(html):


if __name__ == '__main__':
    url = 'https://book.douban.com/'
    html = get_html(url)

