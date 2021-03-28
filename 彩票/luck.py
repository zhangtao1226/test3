# -*- coding = urf-8 -*-
# @Time : 2021/1/12 下午9:42
# @Author : ZhangTao
# @File : luck.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup
import time
import json

class GetDate:
    """
    获取彩票日期
    """
    def __init__(self, path_url, header):
        self.url = path_url
        self.header = header

    def get_html(self):
        """
        
        :return:
        """
        try:
            response = requests.get(self.url, headers=self.header)
            if response.status_code == 200:
                return response.text
        except requests.ConnectionError:
            return None

    def get_element(self, html):
        """
        获取子页面的URL
        :param html:
        :return:
        """
        soup = BeautifulSoup(html, 'lxml')
        children_html_url = soup.select('.iSelectList a')
        html_info = []
        luck_date_list = []
        for child_path in children_html_url:
            luck_date = child_path.get_text()
            luck_date_list.append(luck_date)
            html_info.append(child_path.attrs['href'])
        return html_info, luck_date_list

    def get_child_html(self, child_url):
        """
        获取子页面的HTML
        :param child_url:
        :return:
        """
        try:
            response = requests.get(child_url, self.header)
            if response.status_code == 200:
                return response.text
        except requests.ConnectionError:
            return None

    def get_child_element(self, child_html):
        """
        获取中奖号码
        :param child_html:
        :return:
        """
        soup = BeautifulSoup(child_html, 'lxml')
        element = soup.select('.ball_box01 ul li')
        luck_num_list = []
        for el in element:
            luck_num_list.append(el.get_text())

        print(json.dumps(luck_num_list))
        return luck_num_list

    def save_to_txt(self, number):
        with open('./luck_number.txt', 'a+') as file:
           file.write(str(number) + '\n')

if __name__ == "__main__":
    url = 'http://kaijiang.500.com/dlt.shtml'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    date_list = GetDate(url, headers)
    html = date_list.get_html()
    info_url_list, luck_date_list = date_list.get_element(html)
    for date, path in zip(luck_date_list, info_url_list):
        children_html = date_list.get_child_html(path)
        luck_number = date_list.get_child_element(children_html)
        date_list.save_to_txt(luck_number)
        time.sleep(2)

    # print(all_luck_num_list)
    # print(html)




