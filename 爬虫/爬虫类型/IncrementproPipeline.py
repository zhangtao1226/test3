# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 13:39
# @Author  : zhangtao
# @File    : IncrementproPipeline.py
# @Software: PyCharm

from redis import Redis
class IncrementproPipeline(object):
    conn = None
    def open_spider(self, spider):
        self.conn = Redis(host='127.0.0.1', port=6379)

    def process_item(self, item, spider):
        dic = {
            'name':item['name'],
            'kind':item['kind']
        }
        print(dic)
        self.conn.push('movieDate', dic)
        return item