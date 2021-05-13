# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 17:53
# @Author  : zhangtao
# @File    : robots.py
# @Software: PyCharm
"""
Robots 协议
robots 协议也称作爬虫协议、机器人协议，全名叫做网络爬虫排除标准（Robots Exclusion Protocol）
Robots 协议通常会保存在一个叫 robots.txt 的文本文件中，一般该文件位于网站的根目录。
"""

import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://www.taobao.com/robots.txt')
rp.read()
print(rp.can_fetch('Googlebot', 'https://www.taobao.com/article'))
print(rp.can_fetch('Googlebot', "https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=iphone&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest"))