# 测试内部函数调用父级的函数

def a():
    aa=999
    b(aa)
    print('3',aa)
def b(p):
    print('1',p)
    p=66
    print('2',p)

a()

# 1 999
# 2 66
# 3 999

# 除非用return 的方式