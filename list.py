# list 是python 最常见的数据类型

test = [541564,5,654,656,5]

print(test[0])
print(test[1])
print(test[2])
print(test[3])
print(test[4])
# print(test[5])

print(test[-1])
print(test[-2])
print(test[-3])
print(test[-4])
print(test[-5])

# 重复 输出两次

print(test*2)# [541564, 5, 654, 656, 5, 541564, 5, 654, 656, 5]

test.append("你好")
print(test)

test.pop()#移除末尾
print(test)