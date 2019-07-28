# -*- coding: UTF-8 -*-
"""
@desc 解析mongo日志

"""

# def parser_mongo_logo():
#     # errors = 'ignore'
#     f = open("file/aliyun-mongo.log", "r",errors='ignore')
#     for line in f:
#         print(line)
#     f.close()


# 2017-12-04T23:02:43.484+0800 I NETWORK  [thread1] connection accepted from 1.202.68.84:40992 #6238 (1 connection now open)
# 2017-12-04T23:03:13.961+0800 I NETWORK  [thread1] connection accepted from 113.63.94.68:39718 #6239 (2 connections now open)

import re

# def _search():
#     print(re.search("www", "www.xx.com").span())  # (0,3)
#     print(re.search("www", "www.xx.com").span())  # (0,3)
#     print(re.search("com", "www.xx.com").span())  # (0,3)
#

# def _match():
#     print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配 (0,3)
#     print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
#     print("测试")


# _match()

# parser_mongo_logo()
# 2017-12-04T23:02:43.484+0800 I NETWORK  [thread1] connection accepted from 1.202.68.84:40992 #6238 (1 connection now open)
attack = "2017-12-04T23:02:43.484+0800 I NETWORK  [thread1] connection accepted from 1.202.68.84:40992 #6238 (1 connection now open) "
phone = "2004-959-559 # 这是一个国外电话号码"


def _findall():
    pattern = re.compile(r'^.* from .*$')
    res = pattern.findall(attack)
    print(res)


_findall()
# def _sub():
#     print(re.sub(r'\(.*$', "", attack))# 替换
#     print(re.sub(r'#.*$', "", phone))
#
#
# _sub()
