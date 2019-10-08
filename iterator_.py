"""
@desc python 迭代器
- 一个记住遍历的位置的对象
- 访问集合元素的一种方式
- 从集合中的第一个元素开始访问，直到所有的元素被访问结束，
- 迭代器一往无前
- 迭代器的两个基本方法：iter
- 迭代器的两个基本方法：next
- 迭代完就木得了。
"""
import sys

# a_list = [1, 3, 5, 7, 9]
# it = iter(a_list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# print(it)  # <list_iterator object at 0x00229BD0>

# for语句遍历迭代器
# it1 = iter(a_list)
# for item in it1:
#     print(item)
# print("\n")
# #  next 函数
# # print(it1)
# it2 = iter(a_list)
# while True:
#     try:
#         print(next(it2))
#     except StopIteration:
#         sys.exit()


# 类作为一个迭代器使用需要在类中实现两个方法  __iter__() ,__next__()，

# 创建返回数字的迭代器，初始值1，逐步加2

class TheNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 2
        return x


theNumber = TheNumber()
theIter = iter(theNumber)

print(next(theIter))
print(next(theIter))
print(next(theIter))

# StopIteration 用于表示迭代完成，防止无限循环情况 略

# 生成器 generator
# yield 实现斐波那契数列
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)

while True:
    try:
        print(next(f), end=" ") # 0 1 1 2 3 5 8 13 21 34 55
    except StopIteration:
        sys.exit
