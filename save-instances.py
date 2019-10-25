# 存储实例测试
import time
instanceList=[]

class A:
    def __init__(self):
        instanceList.append(self)
        time.sleep(1)
    def go(self,i):
        # time.sleep(1)
        print(i,'我被实例化拉！',time.time())


start=time.time()
for i in range(10):
    # if len(instanceList):
    #     instanceList[0].go(i)
    # else:
    #     a=A()
    #     a.go(i)
    a=A()
    a.go(i)
instanceList=[] #销毁
end=time.time()
print(instanceList)
print('消耗时间：',end-start) # 消耗时间： 1.0