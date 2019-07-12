"""
@desc Python 数据结构
- 字符串 "hello world"
- 数字 9
- 元组 (2,4,6,8)

- 列表 [1,3,5,7]
- 集合 {1,3,6}
- 字典 {name:"xxx"}

"""

# list 当做堆栈使用
"""
- 最先进入的元素被最后一个释放，后进先出
- [2]
- [2, 4]
- [2, 4, 6]
- [2, 4]
- [2]
"""
stack_list = [2]
print(stack_list)
stack_list.append(4)
print(stack_list)
stack_list.append(6)
print(stack_list)
stack_list.pop()  # 释放出来
print(stack_list)
stack_list.pop()  # 释放出来
print(stack_list)

# list当队列使用
"""
@desc 效率不高
@desc 最后添加或者弹出元素速度快
@desc 列表里插入或者头部弹出不快(因为所有其他元素都得一个个移动，并且排列方式是靠左对齐的)
"""

from collections import deque

queue = deque(["中国", "日本", "韩国"])
print(queue)
queue.append("新加坡")
print(queue)
queue.append("印度")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

# 列表推导式

vec = [2, 4, 6]
a_list = [3 * x for x in vec]  # 循环的结果x 再*3
print(a_list)

fruit_list = [" 中国", " 美 国 ", "俄罗斯 "]
result_fruit = [item.strip() for item in fruit_list]
print(result_fruit)

# 列表推导式-if
print([3 * item for item in vec if item > 3])
# 列表推导式-双重循环
vec1 = [1, 3, 5, 7]
vec2 = [2, 4, 6, 8]
vec3 = [2, 4, 6]
print([x * y for x in vec1 for y in vec2])  # 4*4=16个项，交叉相乘
print([x * y for x in vec1 for y in vec3])  # 4*3=12个项，交叉相乘
print([x * y for x in vec3 for y in vec1])  # 4*3=12个项，交叉相乘
print([x + y for x in vec3 for y in vec1])  # 4*3=12个项，交叉相加
print([vec1[i] * vec2[i] for i in range(len(vec1))])  # vec1 和vec2的元素相加

# 嵌套列表解析
# 嵌套列表，矩阵转换，[3*4]=>[4*3]矩阵
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 方法一
print([[row[i] for row in matrix] for i in range(4)])
"""
    [
        [1, 5, 9], 
        [2, 6, 10], 
        [3, 7, 11], 
        [4, 8, 12]
    ]
"""

print([[row[i] for row in matrix] for i in range(3)])  # 此处的range长度不得超过最大值阵列
"""
    [
        [1, 5, 9], 
        [2, 6, 10], 
        [3, 7, 11]
    ]
"""

# 方法二
temp = []
for item in range(4):
    temp.append([row[item] for row in matrix])
print(temp)
# del语句
b_list = [2, 4, 6, 8]
del b_list[3]
print(b_list)
# del b_list[2:3]
# del a=[:]
# 元组和序列
tup = 899, 9, 63, 5
print(tup)  # (899, 9, 63, 5)
print(tup[1])
print(len(tup))
# 集合
a_set = {2, 4, 6, 8}
a_null_set = set()
print(a_set)
print(a_null_set)
# print(a_set[1])
print(len(a_set))
# 集合推导
a_set_for = {x for x in "helloworld"}  # 命令行可以实现
# a_set_for= {x for x in "helloworld" in x not in "abc"}  # 命令行可以实现
print("a_set_for:", a_set_for)  # a_set_for: {'o', 'l', 'h', 'r', 'd', 'e', 'w'}

# 字典
# 字典-元组列表中构建字典
print(dict([("a", 1), ("b", 2), ("c", 3)]))  # {'a': 1, 'b': 2, 'c': 3}
# 字典-字典推导元组的表达式字典
print({x: x ** 3 for x in (2, 4, 6)})
# dict 指定关键字参数
print(dict(name="bob", age=25, job="乞丐"))  # {'name': 'bob', 'age': 25, 'job': '乞丐'}
# 遍历技巧

# 遍历-字典
kv = {'name': 'bob', 'age': 25, 'job': '乞丐'}
for k, v in kv.items():
    print(k, v)
# 遍历-列表，索引位置和值全部得到，通过enumerate()函数

c_list = [2, 4, 6, 8]

for k, v in enumerate(c_list):
    print(k, v)
# 遍历-列表，同时遍历多个数组
d_list = [3, 5, 7, 9]

for k, v in zip(c_list, d_list):
    print("k:", k)
    print("v:", v)
