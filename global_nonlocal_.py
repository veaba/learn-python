"""
@desc 关键字 global nonlocal关键字

"""

# global 提升局部作用域为全局作用域 略


# nonlocal 提升局部作用域为闭包函数外作用域 略


# 以下代码报错，局部作用域引用错误
a = 10


def test():
    a = a + 1 # 第二个a
    print(a)


test()
