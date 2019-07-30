"""
# 解析ip.yml 和port.yml 文件
python mongo-log-parser.py mongo.log

# 如果带参数`-all` 则全部解析出来，不去重
python mongo-log-parser.py mongo.log  --all

"""

import re
import sys
import json
from datetime import datetime
from collections import Counter

# ip_list

# TODO
exclude_ip_list = [
    "127.0.0.1",
]
ip_list = []
user_list = []  # 解析用户+密码的组合 root@admin
ip_obj = {}
ip_new_obj = {}


# 解析行内容，user: username@password
def parser_user(line):
    pattern_user = re.compile(r'^.*unknown user \'(.+?)\'$')
    user = pattern_user.findall(line)
    if len(user) != 0:
        print(''.join(user))


#  封装解析函数为一个类

class DataVAIMongoLog:

    # log_path mongodb的log文件路径
    # dataV_obj 表示需要加载的对象值，一般为list结构

    def __init__(self, argv):
        self.ip_obj = ip_obj
        self.ip_new_obj = ip_new_obj
        self.start_time = datetime.now()
        self.path_name_list = '.yml'
        self.argv = argv
        try:
            argv[1]
        except IndexError as err:
            print("===", err, " ===")
            print("=== 请为python脚本传入路径参数 ===")
            exit(1)
        self.mongo_log_path = argv[1]
        try:
            with open(self.mongo_log_path, "r", errors="ignore") as f:
                for line in f:
                    self.parser_line(line)
                    # parser_user(line)
                # 去重文件,默认情况
                self.is_default()

        # 文件没发现错误
        except FileNotFoundError as err:
            print("解析的文件路径不存在：", err)

    # 解析行内容，ip+port
    def parser_line(self, line):
        pattern_ip_port = re.compile(r'^.*from (.+?) \(\d .*$')  # ['1.202.68.84:40992 #6238']
        ip_port = pattern_ip_port.findall(line)
        str_ip_port = ''.join(ip_port)
        ip = re.sub(r':.*$', "", str_ip_port)  # 1.202.68.84
        if ip in self.ip_obj:
            if len(ip):
                self.ip_obj[ip] = self.ip_obj[ip] + 1
        else:
            if len(ip):
                self.ip_obj[ip] = 1

    # 如果参数带有 --all，则不去重，默认去重
    def is_default(self):
        pass
        try:
            # 写出ip列表yml文件
            with open(self.mongo_log_path + '-ip--list.json', 'w') as ip_f:
                # 排序次数的值，并转为json文件输出
                self.exclude_ip()
                ip_f.write(json.dumps(dict(sorted(self.ip_obj.items(), key=lambda x: x[1], reverse=True))))
                print("=== " + self.mongo_log_path + '-port--list' + " export Successful  ===")
                end_time = datetime.now()
                print(str((end_time - self.start_time).seconds) + '秒')
        except ValueError:
            print("has_default_err", ValueError)

    # 排除无关ip
    def exclude_ip(self):
        # print(dict(Counter(self.ip_obj) - Counter(dict.fromkeys(exclude_ip_list, 1))))
        self.ip_obj = dict(Counter(self.ip_obj) - Counter(dict.fromkeys(exclude_ip_list, 1)))


# TODO 统计数据


dataV_ai_init_log = DataVAIMongoLog(sys.argv)
