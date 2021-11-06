from multiprocessing.pool import ThreadPool

import time

def process(i,t=1):
    print(i)
    time.sleep(1)
    print(i,t.__hash__)
    print(i,dir(t))
    print(i,t.real)
    # return 
def x(*o):
    print(o)

start=time.time()
pool=ThreadPool(processes=20)
pool.map(process,((i,pool) for i in range(2)))

pool.close()
end=time.time()

print('耗时：',end-start)

# 耗时： 3.0139999389648438

# 30 2.0s
# 50 3.01s
# 100 6  16倍提升
# 200 12s
# 300 16s
# 500 18s
# 1000 52s
# 2600 132