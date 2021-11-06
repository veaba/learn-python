import threading
import time

exit_flag=0

class ThreadDemo(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print("开始线程：",self.name)
        print_time(self.name,self.counter,5)
        print('退出线程：',self.name)

def timeout():
    time.sleep(5)
    print('劳资很耗时！！！！')

def print_time(threadName,delay,counter):
    print(threadName,delay,counter)
    timeout()


start=time.time()
# 创建线程
thread1=ThreadDemo(1,'Thread-1',1)
thread2=ThreadDemo(2,'Thread-2',2)
# thread3=ThreadDemo(3,'Thread-3',3)
# thread4=ThreadDemo(4,'Thread-4',4)
# thread5=ThreadDemo(5,'Thread-5',5)
# thread6=ThreadDemo(6,'Thread-1',6)
# thread7=ThreadDemo(7,'Thread-2',7)
# thread8=ThreadDemo(8,'Thread-3',8)
# thread9=ThreadDemo(9,'Thread-4',9)
# thread10=ThreadDemo(10,'Thread-5',10)

# 开启线程

thread1.start()
thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread8.start()
# thread9.start()
# thread10.start()

thread1.join()
thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# thread6.join()
# thread7.join()
# thread8.join()
# thread9.join()
# thread10.join()



# for 循环多线程，这里永远都是同步创建的，需要等待完成才下一步
# threadObj={

# }
# for i in range(10):
#     threadObj['thread_'+str(i+1)]=ThreadDemo(i+1,'Thread-'+str(i+1),str(i+1))
#     threadObj['thread_'+str(i+1)].start()
#     threadObj['thread_'+str(i+1)].join()

    

print('退出线程！！！')
end=time.time()
print('耗时：',end-start)