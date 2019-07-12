"""
基本的数据序列和反序列化
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
- 意思是，将之前打印的数据都保存
"""
import pickle
import pprint

# data1 = {"name": [21231, 3, 56],
#          "job": "哈哈"}
# a_list = [2, 4, 6, 8]
# a_list = a_list.append(a_list)
#
# output = open("data1.pkl", "wb")
# pickle.dump(data1, output)
#
# pickle.dump(a_list, output, -1)
# output.close()

pkl_file = open("data1.pkl", "rb")
data2 = pickle.load(pkl_file)
pprint.pprint(data2)

data3 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()
