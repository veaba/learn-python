# 空集合需要 使用set()创建
job = {"中国", "web", "前端开发"}
print(job)

if "web" in job:
    print("has")
else:
    print("no has")

# 计算运算

a = set("中国China")
b = set("美国America")

print("a-b:", a - b)  # 差集
print("b-a:", b - a)  # 差集

print("a|b:", a | b)  # 并
print("b|a:", b | a)  # 并
print("a&b:", a & b)  # 交
print("b&a", b & a)  # 交
print("a^b:", a ^ b)  # 都不存在
print("b^a:", b ^ a)  # 都不存在
