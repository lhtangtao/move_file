#!/usr/bin/env python
# encoding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
"""
@author: tangtao
@contact: tangtao@lhtangtao.com
@site: http://www.phpgao.com
@software: PyCharm
@file: get_dir_info.py
@time: 2017/5/23 20:59
"""
import os
import shutil


def get_dir_info(path="."):
    """
    目前只能对文件夹下只有一个文件的情况进行操作
    :param path: 
    :return: 
    """
    print os.getcwd()
    global root, files
    dir_list = []  # 存放文件夹名字的列表
    file_name = []  # 存放文件夹下的文件名的列表
    for root, dirs, files in os.walk(path):
        dir_list.append(root)
        file_name.append(files)
    size = len(dir_list)
    i = 1
    print file_name
    while i < size:
        src = dir_list[i] + os.sep + str(file_name[i][0])
        shutil.move(src, '.')  # 移动
        shutil.rmtree(dir_list[i])  # 删除
        i += 1


if __name__ == '__main__':
    get_dir_info()
