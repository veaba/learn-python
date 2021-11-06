# 条件判断还是进入函数内部return的速度快？
import time 


def b(i):
    if i>250:
        return True
    else:
        return False

def a1(i):
    if b(i):
        return
    pass
    # print('a1',i)

def a2(i):
    pass
    # print('a2',i)


def go():
    start=time.time()
    for i in range(1000000):
        a1(i)
    end=time.time()

    print('耗时1：',end-start)

# go()

def go2():
    start=time.time()
    for i in range(1000000):
        if not b(i):
            a2(i)
    end=time.time()

    print('耗时2：',end-start)

go2()
# 方式一：函数嵌套的组合即：多传球 
# 耗时： 0.01699995994567871
# 耗时1： 0.20300006866455078 100w 打印
# 耗时1： 0.16100001335144043 100w 无打印



# 方式二：截断式
# 耗时： 0.016000032424926758
# 耗时2： 0.16000008583068848 100w 打印
# 耗时2： 0.11500000953674316 100w 无打印