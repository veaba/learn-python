"""
@desc 处理文件和目录的方法
"""

import os
# import shutil
import glob
import sys

# os

# 获取当前工作目录

print(os.getcwd())

# 获取help
# print(help(os))

# #日常文件和目录管理任务

# copy 文件
# shutil.copyfile("./file/foo.log", "./file/foo_copy.log")

# move 文件
# shutil.move("x.log", "file/foo.log")

# 文件通配符 glob
print(glob.glob("*.py"))

# 命令行参数
print(sys.argv)

# 错误输出重定向和程序终止
"""
- sys.stderr
- sys.stdin
- sys.stdout
- sys.exit()
"""

# 字符串正则匹配
