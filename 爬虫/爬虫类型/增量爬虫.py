# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 13:20
# @Author  : zhangtao
# @File    : 增量爬虫.py
# @Software: PyCharm

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from incrementPro.items import IncrementproItem

class MovieSpider(CrawlSpider):
    name = 'move'
    start_urls = ['http://www.4567tv.tv/frim/index7-11.html']
    rules = (
        Rule(LinkExtractor(allow=r'frim/index7-\d+\.html'), callable='parse_item', follow=True),
    )

    conn = Redis(host='127.0.0.1', port=6379)
    def parse_item(self, response):
        li_list = response.xpath('//li[@class="p1 m1"]')
        for li in li_list:
            detail_url = 'http://4567.tv.tv' + li.xpath('./a/@href').extract_first()

            ex = self.conn.sadd('urls', detail_url)
            if ex == 1:
                print('该URL没有被爬取过，可进行数据的爬取')
                yield scrapy.Request(url=detail_url, callable=self.parse_detail)
            else:
                print('数据还没有更新，暂无新数据可爬取')

    def parst_detail(self, response):
        item = IncrementproItem()
        item['name'] = response.xpath('//dt[@class="name"]/text()').extract_first()
        item['kind'] = response.xpath('//div[@class="ct-c"]/d1/dt[4]//text()').extract()
        item['kind'] = ''.join(item['kind'])
        yield item