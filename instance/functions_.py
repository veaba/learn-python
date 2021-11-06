"""
- 函数代码块，def关键字开头，后接函数标识符名称和()
- 函数名下划线，小写字母

"""


def hello():
    print(1 + 1)


hello()


def world(a):
    print(a)


world("hello world")


# 函数调用


def priter(str):
    print(str)
    # return
    return str + "<=>" + str


priter("搞~~")
priter("不搞~~")

str1 = priter("ε=(´ο｀*)))唉")
print(str1)


# python函数 传递不可变的对象实例
def no_change(a):
    a = 10
    print(a)  # 10


b = 2
no_change(b)  # 2
print(b)


# python函数 传可变对象实例
def the_change(a):
    a.append("XXXX")
    print(a)  # [2, 4, 6, 8, 10, 'XXXX']
    return


c = [2, 4, 6, 8, 10]
the_change(c)
print(c)  # [2, 4, 6, 8, 10, 'XXXX']


# 必须参数
def must_param(a):
    print(a)


# must_param()

# 关键字参数,与次数无，与变量名称有关系
def func1(name, age):
    print("name:", name)
    print("age:", age)


func1(age=99, name="狗狗")


# 默认参数,没值则使用默认值
def func2(name="666"):
    print(name)


func2()
func2("9999")


# 不定长参数，元组

def func3(name, *args):
    print("name:", name)
    print("args:", args)
    for item in args:
        print(item)


func3("张三", "嫂子", "阿姨")


# 不定长参数,字典，但入参需要时字典格式**参数

def func4(name, **args):
    print("name:", name)
    print("args:", args)
    for k in args:
        print(k, args[k])


func4("李四", a="嫂子1", b="阿姨2")


# *后参数，必须以关键字入参

def func5(aa, bb, *, cc):
    return aa + bb + cc


print(func5(66, 77, cc=88))

# 匿名函数,lambda，不建议使用匿名函数
# - 拥有自己的命名空间，且不能访问自己参数以外或者全局命名空间的参数
sum1 = lambda arg1, arg2, arg3: arg1 + arg2 + arg3
print(sum1(88, 8874, 2))


# 变量作用域
# - L local 局部作用域
# - E Enclosing 闭包函数外的函数中
# - G Global 全局作用域
# - B Built-in 内置作用域

# L>E>G>B

