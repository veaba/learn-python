# 遍历数字5
for i in range(5):
    print(i)

# 指定区间遍历

for i in range(90, 100):
    print(i, end="<")

# 反序列指定区间遍历，结论：正数：无法遍历
for i in range(100, 90):
    print(i)

# 反序列指定区间遍历，大到小，指定正数步长,无法处理
for i in range(100, 90, 2):
    print("指定正数步长:", i)
# 反序列指定区间遍历，大到小，指定负数步长
for i in range(100, 90, -2):
    print("指定负数步长:", i)

# 正数小到大，指定正数步长
for i in range(90, 100, 2):
    print("正数小到大，指定正数步长:", i)

# 正数小到大，指定负数步长，无法处理
for i in range(90, 100, -2):
    print("正数小到大，指定负数步长:", i)


# 指定步长遍历
for i in range(50, 100, 5):
    print(i)

# 负数，从小到大，无法处理
for i in range(-10):
    print("负数，从小到大", i)

# 负数，从小到大，,范围,无法处理
for i in range(-10, -100):
    print("负数，从小到大，,范围", i)

# 负数，从小到大，范围,指定步长，可以
# for i in range(-10, -100, -2):
#     print("负数，从小到大，范围,指定步长：", i)
