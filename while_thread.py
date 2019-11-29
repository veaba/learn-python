
# while 线程循环不干扰
import time
import threading

def chiHuoGuo(people):
    while True:
        time.sleep(1)
        print('1s ==>',people)
def chiHi(people):
    while True:
        time.sleep(3)
        print('3s ==>',people)

class myThread(threading.Thread):
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadNmae = name
        self.people = people

    def run(self,x=None):
        print('self:',x)
        print("开始线程：" + self.threadNmae)
        if self.threadNmae=='Thread-1':
            chiHuoGuo(self.people)
        else:
            chiHi(self.people)
        print("结束线程：" + self.threadNmae)

if __name__ == "__main__":
    # 启动线程
    thread1 = myThread("小明", "Thread-1")
    thread2 = myThread("小王", "Thread-2")

    thread1.start()
    thread2.start()

    time.sleep(0.1)
    print("退出主线程：吃火锅，结账走人")

    print(11111)

