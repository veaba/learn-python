# coding=utf-8
"""
@desc 面向对象

"""


# 定义一个省份的类
class Province:
    name = "浙江"

    def getCountry(self):
        return self.name + "属于中国"


province = Province()

print(province.name)
print(province.getCountry())


# 定义一个城市的类

class City:
    def __init__(self, x, y):
        self.x1 = x
        self.y1 = y


city = City("杭州", "市")

print(city.x1, city.y1)


class Self:
    # __xx ="我是私有属性，外面无法调用"
    def __init__(self):
        self.xxx='wo __init__里面的，你能调到我吗？'
        self.__xx='hahahahah'
    def show(self):
        print(self)
        print("我是私有属性====：",self.__xx)


    x =222
    @staticmethod
    def go():
        print('我是私有属性')

    @classmethod
    def haha(cls):
        print('类的方法：',cls.x)
        cls.go()# 调用今天的方法
    _aa=99


a_self = Self()
a_self.show()
print("打印类的属性：",a_self.x,a_self._aa,a_self.xxx,a_self.__xx)#可以调到，毕竟绑定在实例的属性下面
print("打印类的私有方法：",a_self.go())
a_self.haha()

# print("类的方法和属性：",dir(Self))# 打印这个类的方法和属性
# print("实例的方法和属性：",dir(a_self))# 打印这个类的方法和属性




# 定义一个School的类，

class School:
    name = "浙江大学"

    def get_school(self):
        return self.name + ':methods'


school1 = School()

print(school1.name)  # 浙江大学
print(school1.get_school())  # 浙江大学:methods

school2 = School()
school2.name = "北京大学"
print(school2.name)  # 北京大学
print(school2.get_school())  # 北京大学:methods
# 结论，实例去改变类，不会修改原来的方法或者属性
print(school1.get_school())  # 浙江大学:methods


# 定义一个Home类，继承
class Home:
    parent = ""
    children = ""
    __dog = "Class Dog"

    def __init__(self, p, c, d):
        self.parent = p
        self.children = c
        self.__dog = d

    def eat(self):
        print(self.parent, self.children)


class Li:
    age = 99

    def __init__(self, p, c, d, g):
        Home.__init__(self, p, c, d)
        self.age = g

    def eat(self):
        print(self.parent, self.children)


home = Li("爹娘", "孩子", "狗狗", 66)
home.eat()
print(home.parent)
print(home.children)
print(home.age)


# print(home.__dog)


# 方法重写
class Class1:
    def a_methods(self):
        print("class1 父类a_methods的方法")

    def b_methods(self):
        print("class1 父类b_methods的方法")


class Class2(Class1):
    def a_methods(self):
        print("class2 子类a_methods的方法")

    def c_methods(self):
        print("class2 子类c_methods的方法")


c = Class2()
c.a_methods()
c.b_methods()
c.c_methods()
super(Class2, c).a_methods()  # 什么意思：用子类对象调用父类已被覆盖的方法


# 多继承,TODO

# class Speaker():
#     name = "Coll"
#     topic = ""
#
#     def __init__(self, n, t):
#         self.name = n
#         self.topic = t
#
#     def speak(self):
#         print("xxxx")
#
#
# class Teacher(Speaker, Class1):
#     job = ""
#
#     def __init__(self, n, a, w, g, t):
#         Speaker.__init__(self, n, a, w, g)
#         Class1.__init__(self, n, a, w, g)
#
#
# test = Teacher("xxx", "xxx", "xx")
# test.speak()


# 运算符重载

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # TODO?
    def __str__(self):
        # print("__str__:", self)
        return "Vector (%d, %d)" % (self.a, self.b)

    # 此处的other
    def __add__(self, other):
        # print("self:", self)
        # print("other:", other)
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(6, 9)
v2 = Vector(8, 12)
print(v1, v2)
print(v1 + v2)
