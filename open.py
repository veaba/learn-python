# TODO 如何读取任意的一行？
# TODO 如果写入中文汉字？
"""
@des 读写文件
@filename 文件名
@mode 只读、写入、追加
    - r 默认，只读方式打开文件，文件的指针将会放在文件的开头,默认的模式
    - rb
    - r+
    - rb+
    - w
    - wb
    - w+
    - wb+
    - a
    - ab
    - a+
    - ab+

"""
import time


# print(time.time())  # 1562914852.1520033


def repair_zero(num):
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)


localtime = time.localtime(time.time())
year = localtime.tm_year
month = repair_zero(localtime.tm_mon)
day = localtime.tm_mday
hour = localtime.tm_hour
minute = repair_zero(localtime.tm_min)
second = localtime.tm_sec
today = str(year) + '-' + month + '-' + str(day) + ' ' + str(hour) + ":" + minute + ':' + str(second)


# 写入一个文件，会重写一个文件

def write_file():
    f = open("file/foo.log", "w")
    f.write(today + ": Python is a good program language\n")  # todo 如果编码是其他类型的话。。
    f.close()


# write_file()


# 写一个文件，如果不是字符串，需要转换
def write_file_not_string():
    f = open("file/foo1.log", "w")
    num_text_value = (today + ": Python is a good program language\n", 146)
    f.write(str(num_text_value))  # todo 如果编码是其他类型的话。。
    f.close()


# write_file_not_string()


# 读一个文件

# 打开并写入一个文件

# 返回文件包含的所有行,前提是文件必须存在，否则保存，返回的是数组
def readlines():
    f = open("file/foo1.log", "r")
    print(f.readlines())
    f.close()


# readlines()

# 迭代的方式读行

def readiter():
    f = open("file/foo1.log", "r")
    # print(f) <_io.TextIOWrapper name='file/foo1.log' mode='r' encoding='cp936'>
    for line in f:
        print(line)
    f.close()


# readiter()


# readline读取单独的一行,返回空字符串，说明已读取到最后一行

def readline():
    f = open("file/foo1.log", "r")
    print(f.readline())


# readline()


# read 方法,指定数目返回，或者是全部返回字符串

def read():
    f = open("file/foo1.log", "r")
    print(f.read())  # read(size) size 为负数，则说明所有内容都会全部读取返回,
    f.close()


# read()


# tell 函数，当前操作的字节数（读、）,返回字节长度

def tell():
    f = open("file/foo1.log", "r")
    f.read()  # 移除此行，就是0
    print(f.tell())
    f.close()


# tell()


# seek()改变文件的位置，f.seek(offset,from_what)函数，默认0

# - seek(x,0) 首行到x字符
# - seek(x,1) 当前位置移动x个字符
# - seek(-x,3) 文件结尾往前移动x字符

# f.close() 模式下没有'b'的，相对于文件起始位置定位
# - 处理完一个文件，需要调用f.close()来关闭文件并系统的资源


# with 关键字 在结束后，正确的关闭文件

def with_file():
    with open("file/foo1.log", "r") as f:
        read_data = f.read()
        print(read_data)


# with_file()

# 追加文本插入

def append_file():
    with open('file/append_file.log', 'a') as f:
        f.write(today + ": Python is a good program language\n")


append_file()
