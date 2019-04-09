# en = ord('A')
# cn = ord('中')
#
# print(en)
# print(cn)
#
# # 中
# print(chr(20013))
# # 中文，十六进制
# print('\u4e2d\u6587')
# print(b'abc')


# unicode 表示str encode
name = 'ABC'.encode('ascii')  ## b'ABC'
zh = '中文'.encode('utf-8')  ##b'\xe4\xb8\xad\xe6\x96\x87'
print(name)
print(zh)


# unicode decode

print(b'ABC'.decode('ascii'))# ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))# 中文