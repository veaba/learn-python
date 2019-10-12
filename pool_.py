from multiprocessing.pool import ThreadPool

import time

def process(i):
    print(i)
    time.sleep(1)
    # return 


start=time.time()
pool=ThreadPool(processes=20)
pool.map(process,(i for i in range(2600)))
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