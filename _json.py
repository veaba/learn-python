"""
@desc json 模块

"""
import json

data = {
    "no": 44,
    "name": "alice",
    "url": "http://baidu.com"
}
json_str = json.dumps(data)
print("Python1:", data)
print("Python2:", repr(data))
print("JSON对象", json_str)

data1 = json.loads(json_str)
print(data["name"])

# 处理json文件，而不是json字符串

# 写入json文件

# while open('./file/data.json', "w") as f:
#     json.dump(data, f)
# # 读取json 文件
# while open("./file/data.json","r") as f:
#     data=json.load(f)
