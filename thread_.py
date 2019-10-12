# 异步多线程测试

from concurrent.futures import ThreadPoolExecutor
import time
import random


def la(name):
    print("%s is 正在拉" % name)
    time.sleep(random.randint(1,3))
    res = random.randint(1,10) * "#"
    return weigh({"name":name,"res":res})

def weigh(shit):
    name = shit["name"]
    size = len(shit["res"])
    print("%s 拉了《%s》kg" %(name,size))

# pool = ThreadPoolExecutor(30)
pool = ThreadPoolExecutor(13)
# pool = ThreadPoolExecutor(13)

# pool.submit(la,"mike")
# pool.submit(la,"peter")


for i in range(10):
    pool.submit(la,"jack"+str(i+1))