# python异步编程之asyncio（百万并发） https://www.cnblogs.com/shenh/p/9090586.html
# python中的asyncio https://www.jianshu.com/p/2eaf07770e79

import time
import asyncio


# demo1：循环里面进行同步代码
# def the_asyn():
#     def hello():
#         time.sleep(1)
#
#     def run_asyn():
#         for i in range(10):
#             hello()
#             print("哇哈哈：%s" % time.time())
#
#     run_asyn()
#
#
# demo2：循环里面异步代码
def the_async():
    async def hello(i):
        asyncio.sleep(i)
        # time.sleep(1)
        print("异步代码：%s" % time.time(),i)
        return str(i)+'：哈哈'
    def run_async():
        loop = asyncio.get_event_loop()
        for i in range(10):
           loop.run_until_complete(hello(i))
    run_async()

the_async()

# demo3：循环里面异步代码
# def the_async_await():
#     loop = asyncio.get_event_loop()
#     async def hello(i):
#         await asyncio.sleep(1)
#         print("异步代码：%s" % time.time())
#         return str(i)+'哈哈'

    

#     def run_async():
#         for i in range(10):
#            x= loop.run_until_complete(hello(i))
#            print(x)

#     run_async()

#
# the_async_await()

# def the_async_1():
#     @asyncio.coroutine
#     def hello():
#         print("Hello world!")
#         # 异步调用asyncio.sleep(1):
#         yield from asyncio.sleep(1)
#         print("Hello again!")


#     # 获取EventLoop:
#     loop = asyncio.get_event_loop()
#     # 执行coroutine
#     loop.run_until_complete(hello())
#     loop.close()

#     hello()

#     print("aaa")

# the_async_1()
# demo5:无法突破带来的异步
def the_async_c(i):
    time.sleep(1)
    print('the_async_c:',i)

def the_async_b(i):
   the_async_c(i)

async def the_async_a(i):
    await asyncio.sleep(1)
    the_async_b(i)

def the_async_main():
    start=time.time()
    print('执行：the_async_main')
    loop=asyncio.get_event_loop()
    for i in range(10):
        loop.run_until_complete(the_async_a(i))
    print('结束：the_async_main')
    end=time.time()
    print('总时间：',end-start)


# the_async_main()


