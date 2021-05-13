# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 15:33
# @Author  : zhangtao
# @File    : 遍历文件夹.py
# @Software: PyCharm

import os


def getAllDir(dir_path):
    """
    os.walk函数来遍历文件夹及子文件夹下所有文件并得到路径
    os.walk的完整定义形式如下：
        os.walk(top, topdown=True, onerror=None, followlinks=False)
    参数：
        top:需要遍历目录的地址。
        topdown 为真，则优先遍历top目录，否则优先遍历top的子目录(默认为开启)。
        onerror 需要一个 callable 对象，当walk需要异常时，会调用。
        followlinks 如果为真，则会遍历目录下的快捷方式(linux 下是 symbolic link)实际所指的目录(默认关闭)。

    os.walk使用
        os.walk 的返回值是一个生成器(generator),也就是说我们需要用循环不断的遍历它（不可以直接print），来获得所有的内容。

    每次遍历的对象都是返回的是一个三元元组(root,dirs,files)
        root 所指的是当前正在遍历的这个文件夹的本身的地址
        dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
        files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)

    :param dir_path:
    :return:
    """

    for dirPath, dirName, fileName in os.walk(dir_path):
        print(f'打开文件夹{dirPath}')  # 当前文件夹路劲

        if dirName:
            print(f'文件夹列表:{dirName}')  # 包含文件夹名称[列表形式]

        if fileName:
            print(f'文件列表:{fileName}')  # 包含文件名称[列表形式]
            for file in fileName:
                file_path = os.path.join(dirPath, file)
                if os.path.isfile(file_path):  # 判断是否是文件
                    print(f'文件绝对路径: {file_path}')

        print('-'*10)

def get_dir_by_scandir(dir_path):
    print(f'打开当前文件夹：{dir_path}')
    items = []
    dir_dict = dict()
    if not os.path.exists(dir_path):
        print(f'{dir_path}--文件夹不存在！！！')
        return
    for file in os.scandir(dir_path):
        items.append(file.name)
        dir_dict
        # print(file.name, file.path)
        dir_dict[file.name] = file.path
    return dir_dict



if __name__ == '__main__':
    # print(os.name)

    dir_path = '/Volumes/Projects/Python/test3'
    # getAllDir(dir_path)
    get_dir_by_scandir(dir_path)