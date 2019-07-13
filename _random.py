"""
随机数，py的文件名不能是random，否则无法引入module，从而报错
"""
import random

# 随机
print(random.random())  # 0.7605868477680534

# 整数的随机数

print(random.randint(0.9))

# 有范围的条件随机数
print(random.uniform(99, 100))  # 99.9339876248865

# 挑选
print(random.choice([554, 54, 6]))  # choice 必须是数组

# 生成数组
print(range(10))  # range(0, 10)

# 挑选0-9随机整数
print(random.choice(range(10)))

# 种子

random.seed()
print("默认：", random.random())

random.seed(100)
print("整数种子：", random.random())  # 没改变

random.seed("hello", 10)
print("字符串种子：", random.random())
