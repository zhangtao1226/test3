import requests
import logging
import re
import pymongo
from pyquery import PyQuery as pq
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
BASE_UTL = "https://static1.scrape.cuiqingcai.com";
TOTAL_PAGE = 10;

def scrape_page(url):
    logging.info('scraping %s...',url)
    try:
        pass
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            logging.info('get invalid status code %s while scraping %s',response.status_code,url)
    except requests.RequestException:
        logging.info('error occurred while scraping %s',url, exc_info=True)

def scrape_index(page):
    '''
    拼接url，并调用scrape_page()方法，返回html
    :param page: 页码
    :return:
    '''
    index_url = f'{BASE_UTL}/page/{page}'
    return scrape_page(index_url)

def pages_index(html):
    '''
    解析html页面，获取二级页面的详情链接
    :param html:
    :return:
    '''
    doc = pq(html)
    links = doc('.el-row .name')
    for link in links.items():
        href = link.attr('href')
        detail_url = urljoin(BASE_UTL, href)
        # logging.info('get detail url $s', detail_url)
        yield detail_url

def scrape_detail(url):
    '''
    获取详情页面的html
    :param url:
    :return:
    '''
    return scrape_page(url)

def parse_detail(html):
    '''
    解析详情页面
    :param html:
    :return:
    '''
    doc = pq(html)

    cover = doc("img.cover").attr('src')
    name = doc('a > h2').text()
    categories = [item.text() for item in doc('.categories button span').items()]
    published_at = doc('.info:contains(上映)').text()
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
    if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
    drama = doc('.drama p').text()
    score = doc('p.score').text()
    score = float(score) if score else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }

MONGO_CONNECTION_STRING = 'mongodb://47.102.46.193:27017'
# MONGO_DB_NAME = 'movies'
# MONGO_COLLECTION_NAME = 'movies'
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies_2']
collection = db['movies']

def save_data(data):
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)

def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        detail_urls = pages_index(index_html)
        for detail_url in detail_urls:
            detail_html = scrape_detail(detail_url)
            data = parse_detail(detail_html)
            logging.info('get detail data %s', data)
            logging.info('saving data to mongodb')
            save_data(data)
            logging.info('data saved successfully')

import multiprocessing
if __name__ == "__main__":
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main(), pages)
    pool.close()
    pool.join()
