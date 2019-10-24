    # list 是python 最常见的数据类型,就是数组
def default():
    test = [1, 3, 5, 7, 9]
    odd = [2, 4, 6, 8, 10]
    array = ["维", "护", "世", "界", "和", "平"]
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

    print(test * 2)  # [541564, 5, 654, 656, 5, 541564, 5, 654, 656, 5]

    test.append("你好")
    print(test)

    test.pop()  # 移除末尾
    print(test)

    # 删除列表、即删除数组，del 似乎没有返回值，无法进行赋值
    del test[2]
    print(test)

    # 列表长度
    print(len(test))

    # 列表组合 +
    print(test + array)

    # 重复*
    print(test * 2)

    # 判断是否存在列表中
    print("世" in array)  # True
    print("世界" in array)  # False

    # 迭代list
    for x in test + array:
        print(x, end=" ")

    # 截取和拼接
    print(array[-3])
    print(array[1:2])

    # 嵌套树,二维数组
    print([test, array])

    # 列表最大值
    print(max(test))
    # 列表最小值
    print(min(odd))

    # 元组转为列表
    tup = ("中", "国")
    print(list(tup))

    # 末尾添加
    # 统计出现的次数
    # 末尾添加一次性，类似一个JS 中的concat
    # test.extend(odd)
    # print(test)

    # 快速创建数组
    print(list(range(5)))

    # 类似js中splice，只是单个
    array.insert(2, ["银", "河"])
    array.insert(5, "的")

    # pop 移除一个元素，默认是最后一个
    array.pop(2)
    print(array)

    # 移除匹配的元素
    array.remove("的")
    print(array)

    # 逆向
    array.reverse()
    print(array)

    # 排序list.sort( key=None, reverse=False)
    array.sort()
    print(array)

    # clear 清空列表
    array.clear()
    print(array)

    # copy 复制列表 -> 类似 test[:]
    print(test.copy())

    # 去重
    ids = [111, 3, 32, 3, 5, 66, 6, 5]
    new_ids = list(set(ids))
    print(new_ids)

    # 排序
    new_ids.sort()
    print(new_ids)


# a=[99,656,262]
# b=['add','dsada']
# print(a+b)
# o=a+b

# def x(h):
#     print(h)

# x(o)

def create_list_mode1():
    a =10
    for i in range(a):
        print(i)# 0-1

# 创建100个长度的[2,,...,2]
def create_list_mode2():
    xx =[ 2 for i in range(99)]
    print(xx)


# 创建 [0, 1, 2, 3, 4, 5, 6, 7, 8] 数组
def create_list_mode3():
    xx =[i for i in range(9)]
    print(xx)
# create_list_mode3()

# [2, 3, 4, 5, 6, 7, 8, 9, 10]
def create_list_mode4():
    xx =[i+2 for i in range(9)]
    print(xx)
# create_list_mode4()

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
def create_list_mode5():
    xx =[i*2 for i in range(10)]
    print(xx)
# create_list_mode5()

# [0, 1, 2, 3, 4, 5, 6, 7, 8]
def create_list_mode6():
    xx =list(range(9))
    print(xx)
create_list_mode6()