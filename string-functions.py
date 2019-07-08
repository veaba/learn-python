"""
字符串的内置方法
"""
str1 = "hello,World "
chi = "中国"

# capitalize，转换首字母大写
print(str1.capitalize())
print(chi.capitalize())

# center返回一个指定宽度width居中的字样,width必须大于str1的长度
# fillchar 只能是一个字符a-z0-9，也可以是中文
print(str1.center(32, '*'))  # **********hello,World **********
print(chi.center(32, '_'))  # _______________中国_______________
print(chi.center(32, ' '))  # 中国
print(chi.center(32, '口'))  # 口口口口口口口口口口口口口口口中国口口口口口口口口口口口口口口口

# count 统计字符串里某字符的出现次数，可选开始到结束
chi1 = "中国人民万岁，世界人民万岁"
print(chi1.count("人民"))  # 2次
print(chi1.count("人民", 6))  # 1次

# bytes.decode

chi1_utf8 = chi1.encode("UTF-8")
str1_utf8 = str1.encode("UTF-8")

chi1_gbk = chi1.encode("GBK")
str1_gbk = str1.encode("GBK")
print(chi1_utf8)  # b'hello,World '
print(str1_utf8)  # b'hello,World '

print(chi1_gbk)  # b'hello,World '
print(str1_gbk)  # b'hello,World '

print(chi1_utf8.decode("UTF-8"))
print(chi1_gbk.decode("UTF-8", "strict"))
