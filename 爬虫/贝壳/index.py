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
            soup = BeautifulSoup(html, 'lxml')
        return soup
    except RequestException:
        return None

def get_parse(soup):
    sellListContent = soup.find_all(name='li', attrs={'class': 'clear'})
    all_house_list = []
    for li in sellListContent:
        hose_info_list = {}
        hose_info_list['detail_url'] = li.a.attrs['href']
        hose_info_list['house_img'] = li.a.img.attrs['src']
        hose_info_list['house_title'] = li.find(name='a', attrs={'class': 'VIEWDATA CLICKDATA maidian-detail'}).attrs['title']
        hose_info_list['house_address'] = li.find(name='div', attrs={'class': 'positionInfo'}).a.string
        hose_info_list['house_address_detail_url'] = li.find(name='div', attrs={'class': 'positionInfo'}).a.attrs['href']
        hose_info_list['house_info'] = li.find(name='div', attrs={'class': 'houseInfo'}).contents[2].strip('\n')
        hose_info_list['house_follow_info'] = li.find(name='div', attrs={'class': 'followInfo'}).contents[2].strip('\n')
        hose_info_list['house_total_price'] = li.find(name='div', attrs={'class': 'totalPrice'}).span.string
        hose_info_list['huose_unit_price'] = li.find(name='div', attrs={'class': 'unitPrice'}).span.string
        house_tags = li.find(name='div', attrs={'class': 'tag'})
        hose_info_list['house_tags'] = []
        for tag in house_tags:
            hose_info_list['house_tags'].append(tag.string)
        all_house_list.append(hose_info_list)

    return all_house_list


def save_data(lists):
    result_list = []
    for list in lists:
        result = collection.insert_one(list)
        result_list.append(result)
    return result_list


url = 'https://nj.ke.com/ershoufang/'
# soup = get_html(url)
# house_list = get_parse(soup)

for i in range(1, 101):
    if i > 1:
        url = url + 'pg' + str(i)
    soup = get_html(url)
    house_list = get_parse(soup)
    save_data(house_list)

    time.sleep(1)








