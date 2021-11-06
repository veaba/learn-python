# 数据压缩
# 不确保压缩后比原始数据一定小，主要压缩在相同的字符上面
# zlib
import zlib
a_str = b'ddddddddddddddddddddddddddddd aaaaaaaaaaaaaaa'
# a_str = '从日后的三天，在海港旁的一处阴影下。'
# a_str = b'从日后的三天，在海港旁的一处阴影下。'
print(len(a_str))

a_zlib = zlib.compress(a_str)
print(len(a_zlib))#37
print(a_zlib) # b'x\x9cKI,N1341531L)NT045K1)N45I15KT\x00\x00~o\x08!'

b_zlib=zlib.decompress(a_zlib)
print(b_zlib)

# gzip
# bz2
# zipfile
# trafile