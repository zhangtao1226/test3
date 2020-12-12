import requests
import re
import json
from requests.exceptions import RequestException
import time

def get_one_page(url):
    '''
    获取 html
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
        return None
    except RequestException:
        return None

def parse_one_page(html):
    '''
    获取当前页列表
    :param html:
    :return:
    '''
    # 更新时间
    # pattern_update_time = '<p class="update-time">(.*?)<span.*?</p>'
    # update_time = re.findall(pattern_update_time, html)[0]
    pattern = re.compile(
        '''<dd>.*?board-index.*?>(\d+)</i><a href="(.*?)".*?<img.*?class="borad-img".*?src="(.*?)"></a>
        .*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?).*?</i>.*?fraction">(.*?)</i>.*?</dd>
        ''', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'id': item[1],
            'index': item[0],
            'image': item[2],
            'actor': item[3],
            'time': item[4],
            'score': item[5] + item[6]
        }

def write_to_file(content):
    with open('top100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    pattern = '<title>(.*?)</title>'
    verify_result = re.findall(pattern, html, re.S)[0]
    if verify_result == '验证中心':
        print('需要验证')
        return None
    else:
        for item in parse_one_page(html):
            write_to_file(item)

if __name__ == '__main__':
    for i in range(1):
        main(offset= i * 10)
        time.sleep(1)

