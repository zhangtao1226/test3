"""
贝壳房产信息爬取
"""
import requests
import json
import time
import logging
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import pymongo

client = pymongo.MongoClient(host='47.102.46.193', port=27017)
db = client.beike
collection = db.ershoufang


headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}

def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html = response.text
            print(html)
            exit()
            soup = BeautifulSoup(html, 'lxml')
        return soup
    except RequestException:
        return None

def get_page_content(soup):
    sell_list_content = soup.find(name='ul', attrs={'class':'sellListContent', 'log-mod':'list'})
    print(sell_list_content)


url = 'https://nj.ke.com/ershoufang/'
soup = get_html(url)
house_list = get_page_content(soup)