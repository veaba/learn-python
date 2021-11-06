# -*- coding: UTF-8 -*-
"""
@desc 解析mongo日志

"""

import re

ip_list = []  # ip list
port_list = []  # port list


def _findall(line):
    pattern_ip_port = re.compile(r'^.*from (.+?) \(\d .*$')  # ['1.202.68.84:40992 #6238']
    ip_port = pattern_ip_port.findall(line)
    str_ip_port = ''.join(ip_port)
    str_ip = re.sub(r':.*$', "", str_ip_port)  # 1.202.68.84
    str_port = re.sub(r'^.*:(.+?) #', '', str_ip_port)  # 40992
    ip_list.append(str_ip)
    port_list.append(str_port)


def parser_mongo_logo():
    with open("file/aliyun-mongo.log", "r", errors='ignore') as f:
        for line in f:
            _findall(line)
    set_ip_list = list(set(ip_list))
    set_port_list = list(set(port_list))

    print("ip列表：", set_ip_list)
    print("端口列表：", set_port_list)

    # 不去重
    with open('file/aliyun_ip_list_all.yml', 'w') as f:
        for ip in ip_list:
            if len(ip) != 0:
                f.write(ip + '\n')
    with open('file/aliyun_port_list_all.yml', 'w') as f:
        for port in port_list:
            if len(port) != 0:
                f.write(port + '\n')
    # 写到一个文件里面去,去重
    with open('file/aliyun_ip_list.yml', 'w') as f:
        for ip in set_ip_list:
            f.write(ip + '\n')
    with open('file/aliyun_port_list.yml', 'w') as f:
        for port in set_port_list:
            f.write(port + '\n')


parser_mongo_logo()
