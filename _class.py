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
    def show(self):
        print(self)
        print(self.__class__)


a_self = Self()
a_self.show()


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


home = Li("爹娘", "孩子", "狗狗",66)
home.eat()
print(home.parent)
print(home.children)
print(home.age)
# print(home.__dog)
