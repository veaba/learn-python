"""
@desc 集合
@desc 集合有什么用途和实际场景??TODO
@desc 集合是无序的，所以每次返回都不一样的顺序
@desc 元素具有唯一值
"""
# 空集合需要 使用set()创建
job = {"中国", "web", "前端开发"}
print(job)

if "web" in job:
    print("has")
else:
    print("no has")

# 计算运算

a = set("中国")
b = set("美国")

print("a|b:", a | b)  # 并
print("b|a:", b | a)  # 并
print("a&b:", a & b)  # 交
print("b&a", b & a)  # 交
print("a^b:", a ^ b)  # 都不存在
print("b^a:", b ^ a)  # 都不存在

print("a:", a)
print("b:", b)
# 为集合添加元素
a.add("china")
print(a)
# 移除集合中的所有元素
# 拷贝一个集合
# 集合差集
print("a-b:", a - b)  # 差集
print("b-a:", b - a)  # 差集
print(a.difference(b))
print(b.difference(a))

# 移除集合中都存在的元素，没有返回值
a.difference_update(b)
print(a)

# 删除集合中指定的元素
a.discard("china")
print(a)

a.add("Chinese")
a.add("国")
a.add("中")
print(a)

# 返回交集
print(a.intersection(b))
print(b.intersection(a))

print(a)

# 交集并增加
a.intersection_update(b)
print(a)  # 国
a.add("Chinese")
a.add("国")
a.add("中")
a.clear()
# 判断两个集合中的相同的元素
print(a.isdisjoint(b))  # 没有则发挥False，否则True

a.add("Chinese")
a.add("国")
a.add("中")

# a是否都包含b
print(a.issubset(b))  # False

# 随机移除元素
print(a.pop())

# 移除指定的元素
print(b.remove("国"))
print(b)

# 返回集合中两个不重复的元素集合
a.symmetric_difference(b)

# 移除当前集合中另外指定集合相同元素，并将另外一个指定集合中不同的元素插入当前的集合中。意思是，把别人的二姨太的副本给取过来
a.symmetric_difference_update(b)

print(a, b)
# 返回两个集合的并集
print(a.union(b))  # {'国', '美', 'Chinese'}
# 给集合添加元素，b合并到a，并忽略重复x
print(a.update(b))
