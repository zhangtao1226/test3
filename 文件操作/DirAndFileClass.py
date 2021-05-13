# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 17:41
# @Author  : zhangtao
# @File    : DirAndFileClass.py
# @Software: PyCharm
import os

class DirAndFileClass(object):
    """
    文件夹及文件类
    """
    def __init__(self):
        pass

    def get_desktop_path(self):
        """
        获取桌面路径
        :return: string 桌面路径
        """
        return os.path.join(os.path.expanduser('~'), 'Desktop')



