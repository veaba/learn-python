# 正则溢出
# 官方开发者给出的demo
# 地址：https://bugs.python.org/issue38582%3E
import re

NUM = 100

# items = [ '(001)', '(002)', '(003)', ..., '(NUM)']
items = [r'(%03d)' % i for i in range(1, 1+NUM)]

print(items)
pattern = '|'.join(items)

print(pattern)# (001)|(002)|(003)|(004)

# repl = '\1\2\3...\NUM'
temp = ('\\' + str(i) for i in range(1, 1+NUM))

print(temp)
repl = ''.join(temp) # \\1
print(repl)

text = re.sub(pattern, repl, '(001)')
print(text)

# if NUM == 99
# output: (001)
# if NUM == 100
# output: (001@)
# if NUM == 101
# output: (001@A)