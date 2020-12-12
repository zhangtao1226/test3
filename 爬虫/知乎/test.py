import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/explore'
headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}

html = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(html, 'lxml')

for el in soup.find_all(attrs={'class':"ExploreSpecialCard ExploreHomePage-specialCard"}):
    img = el.a.img.attrs['src']
    title = el.find(attrs={'class':"ExploreSpecialCard-title"}).string

    print(img, title)
