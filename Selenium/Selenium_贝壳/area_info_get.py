'''
获取贝壳区域地址信息，包括 城市名称、链接等；
'''

import time
import pymongo
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


chrome_options = Options()
# 无头模式启动
chrome_options.add_argument('--headless')
# # 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--disable-gpu')
# brower = webdriver.Chrome()
brower = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(brower, 10)

client = pymongo.MongoClient(host='47.102.46.193', port=27017)
db = client.beike
mycol = db.citys

url = 'https://nj.fang.ke.com/loupan'

def page_index(url):
    try:
        brower.get(url)
    except TimeoutException:
        print('Time Out')

    try:
        button = brower.find_element_by_class_name('s-city')
        button.click()
        city_lists = brower.find_elements_by_css_selector('.city-change .fc-main div ul li')
        all_citys = []
        for city_list in city_lists:
            city_info = {}
            city_info['code'] = city_list.find_element_by_tag_name('span').text
            city_info['city_list'] = []
            son_city_lists = city_list.find_elements_by_css_selector('div a')
            for son_city_list in son_city_lists:
                son_list = {}
                son_list['name'] = son_city_list.text
                son_list['href'] = son_city_list.get_attribute('href')
                city_info['city_list'].append(son_list)
            all_citys.append(city_info)
        return all_citys
    except NoSuchElementException:
        print('Not found')

def save_data_to_MongoDb(citys):
        for data in citys:
            try:
                if mycol.insert_one(data):
                    print(data.get('code'),'seccess')
            except Exception:
                print(data.get("code"), 'fiald')

if __name__ == '__main__':
    all_citys = page_index(url)
    save_data_to_MongoDb(all_citys)

