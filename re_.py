"""
@desc 正则匹配模块
"""
import re

# 查找正则
a_list = re.findall(r'\bf[a-z]*', 'which foot back hand fill fast')
print(a_list)

# 查询连续重复
b_list = re.sub(r'(\b[a-z]+) \1', r'\1', "cat in the tea the the hat")
print(b_list)

# 文本替换

c_str = "hello bitch world"

print(c_str.replace('bitch', ''))
