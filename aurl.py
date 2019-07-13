"""
@desc 访问网络模块
"""
from urllib.request import urlopen

for line in urlopen("http://baidu.com"):
    lines = line.decode("utf-8")  # 二进制数据转文本
    if 'EST' in line or 'EDT' in lines:  # 寻找东方时间
        print(line)
    # print(lines)
