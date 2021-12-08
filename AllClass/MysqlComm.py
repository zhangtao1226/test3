# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 16:42
# @Author  : zhangtao
# @File    : MysqlComm.py
# @Software: PyCharm
import pymysql
from timeit import default_timer

class MysqlComm(object):
    def __init__(self, commit=True, log_time=True, log_label='总用时'):
        """
        :param commit: 是否在最后提交事务（设置为False的时候方便单元测试）
        :param log_time: 是否打印程序运行总时间
        :param log_label: 自定义log的文字
        """
        self._log_time = log_time
        self._commit = commit
        self._log_label = log_label

    def __enter__(self):
        # 如果需要记录时间
        if self._log_time is True:
            self._start = default_timer()

        # conn = get_con