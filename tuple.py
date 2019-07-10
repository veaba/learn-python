"""
@desc 如何获取到索引值

"""
# 元组无法修改
tup = ("I", "Love", "You")
print(tup)

# 需要加逗号，声明，如果只有一个参数的时候
tups = (20,)
print(tups)

# 不是元组
tup1 = (210)
print(tup1)

tup2 = ("I", "Love", "You")
tup3 = ("世", "界")
# 修改元组,通过相加实现
print(tup2 + tup3)

# 删除元组，不允许删除单个，但可以删除全部

# 计算元组个数
print(len(tup3))

# 复制
print(tup2 * 1)
# 判断存在
print("Y" in tup2)
# 连接
print(tup2 + tup3)
# 迭代
for x in tup2:
    print(x, )

# 截取


# 最大值
print(max(tup2))
# 最小值
print(min(tup3))
# 列表转元组
print(tuple(["英", "雄", "联", "盟"]))
