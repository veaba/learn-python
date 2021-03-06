"""
@desc 字典,其实就是Javascript 中的对象，object
@desc 字典与字典如何比较？？
@desc 清空被引用的赋值也会一起被清空
@desc 使用copy。则会新生成的一个副本清空原先的字典，不会被清空引用
"""

import json
from collections import Counter


def default():
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


# list
def go_list():
    a_list = [1, 1, 1, 1, 2, 3, 4, 6, 6, 9, "127.0.0.1", "127.0.0.1"]

    obj = {}
    for item in a_list:
        obj[item] = str(a_list.count(item)) + '次'
    print(obj)  # {1: '4次', 2: '1次', 3: '1次', 4: '1次', 6: '2次', 9: '1次'}

    print(json.dumps(obj))


# go_list()

# 字段排序
def dirt_sort():
    obj = {
        "140.205.201.43": 199,
        "139.189.185.214": 197,
        "115.197.196.133": 166,
        "140.205.225.186": 150,
        "125.120.161.247": 135,
        "140.205.225.196": 125,
        "140.205.225.197": 125,
        "140.205.201.40": 125,
        "122.234.10.102": 119,
        "140.205.225.204": 100,
        "140.205.225.191": 100,
        "140.205.201.44": 100,
        "140.205.225.190": 75,
        "140.205.201.35": 75,
        "140.205.201.39": 75,
        "140.205.225.187": 75,
        "140.205.201.31": 75,
        "140.205.201.36": 75,
        "140.205.201.33": 75,
        "140.205.225.195": 75,
        "118.31.244.58": 73,
        "119.23.138.247": 72,
        "106.15.76.85": 72,
        "47.94.39.226": 72,
        "120.55.13.109": 69,
        "218.74.14.88": 68,
        "106.15.52.246": 67,
        "39.107.14.208": 65,
        "47.93.180.168": 65,
        "47.94.52.159": 62,
        "106.15.76.92": 62,
        "120.78.225.124": 61,
        "106.14.104.214": 61,
        "47.100.64.86": 60,
        "47.97.21.76": 60
    }
    # print(obj.values())
    # print(obj.keys())
    # list_obj_value = list(obj.values())
    # list_obj_key = list(obj.keys())

    # print(list_obj_value)
    # print(list_obj_key)
    # 默认对obj的键从小到大排序
    print("排序:", sorted(obj))
    # 默认对obj的键从小到大排序，取得元组的排序
    # print("排序:", sorted(obj.items()))

    # 结果
    # print("对值排序：", sorted(obj.items(), key=lambda x: x[1]))
    # print("对值逆序：", dict(sorted(obj.items(), key=lambda x: x[1], reverse=True)))

    print("对值排序：", sorted(obj.items()))


# dirt_sort()


# 元组转字典
def tup_to_dict():
    a_tup = [('127.0.0.1', 192), ('192.168.1.1', 1)]
    print(dict(a_tup))


# 列表转字典

def list_to_dict():
    a_list = ["127.0.0.1", "99,99,9,99"]

    print(dict.fromkeys(a_list))


# list_to_dict()


# tup_to_dict()


# 字典减
def dict_subtract():
    parent_dict = {"a": 999, "b": 888, "c": 777, "d": 666}
    child_dict = {"d": 666}

    print(dict(Counter(parent_dict) - Counter(child_dict)))

    print(Counter(parent_dict))
    print(Counter(child_dict))

    # print("x:", dict(Counter(child_dict) - Counter(parent_dict)))

    a_obj_x = dict(Counter(parent_dict) - Counter(child_dict))
    print(a_obj_x)

# dict_subtract()
