"""
@desc 字典,其实就是Javascript 中的对象，object
@desc 字典与字典如何比较？？
@desc 清空被引用的赋值也会一起被清空
@desc 使用copy。则会新生成的一个副本清空原先的字典，不会被清空引用
"""
obj = {
    "name": "jo.gel",
    "job": "web前端"
}
print(obj)

obj1 = {
    999: 55
}
obj2 = {
    "country": "china",
    "nation": "Han",
    "province": "Zhejiang"
}
print(obj1)

# 访问字典
print(obj1[999])

# 修改字段
obj1[999] = "世界第一"
print(obj1)

# 删除字段
del obj1[999]
print(obj1)

# 删除字典
del obj1

# 字段长度
print(len(obj2))
# 输出字典
print(str(obj2))
print(obj2)
# type
print(type(obj2))  # <class 'dict'>

# 清空字典元素
print(obj2)
obj3 = obj2.copy()
obj2.clear()
print(obj2)
print(obj3)

# 元组生成字典，且赋一个相同的值
tup1 = (1, 3, 5)
obj4 = dict.fromkeys(tup1)
obj5 = dict.fromkeys(tup1, "hello")
print(obj4)
print(obj5)

# 获取一个值，且有自己的默认值，如果没有则返回默认值
print(obj5.get(3, "world1"))  # hello
print(obj5.get(4, "world2"))  # world2

# 判断字典是否存在某值
print("2" in obj5)
print("3" in obj5)
print(3 in obj5)

# 快速创建元组
atup = range(5)
print(tuple(atup))

# 遍历元组数组
print(obj5.items())  # dict_items([(1, 'hello'), (3, 'hello'), (5, 'hello')])

tup2 = obj5.items()

for k, v in tup2:
    print(k)
    print(v)

# 返回一个迭代器，用list转为列表
print(obj5.keys())  # dict_keys([1, 3, 5])
print(list(obj5.keys()))  # [1, 3, 5]
print(tuple(obj5.keys()))  # (1, 3, 5)

# 和get类似，setdefualt，如果不存在，则将默认值添加到字典中
print(obj5.setdefault(2, "HHAK"))

# 返回一个迭代器
print(obj5.values())
print(list(obj5.values()))
print(tuple(obj5.values()))
print(obj5)

# 删除字典所给key对应的值，返回被删的值，key必须，否则返回默认值
print(obj5.pop(3))
print(obj5)

# 随机返回并删除字典中的一堆键和值，一般删除末尾对
obj6 = obj5.popitem()
print(obj6)

obj7 = dict.fromkeys(obj6, "hello")

print("obj7:", obj7)
print(obj5)

# 把x 更新到o,相当于合并字典
obj7.update(obj5)
print(obj7)
