# coding=utf-8
# 方法1
def small10():
    a, b = 0, 1
    while b < 10:
        print(b, )
        a, b = b, a + b  # => 和上面的一样。a=b,b=a+b


# print(small10())


# 方法2，计算入参的斐波那契数列的值
def f(n):
    if n < 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


# print(f(10))


# 方法3,三个变量计算

def f1(n):
    a = 0
    b = 1
    if n < 2:
        print(b)
        return b
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
        print(a, b, c)


f1(10)
