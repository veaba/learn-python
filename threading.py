"""
@desc Python 多线程,TODO 这模块比较难，后续再学习
【优点】：
- 可以把占据长时间中的任务放到后台去处理
- 程序的运行速度可能加快
- 对于用户输入、读写、网络收发，可以释放内存占用等资源
【特点】：
- 线程可以被抢占（中断）
- 在其他线程运行时，线程可以暂时被搁置（睡眠）——线程的退让
【线程分类】：
- 内核线程：又操作系统内核创建和撤销
- 用户线程：不需要内核支持而在用户程序中实现的线程
【Python线程模块】：
- _thread
- threading(推荐)
"""

import _thread
import time


def go(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(go, ("thread-1", 2,))
    _thread.start_new_thread(go, ("thread-2", 4,))
except:
    print("Error 启动线程失败")
while 1:
    pass
