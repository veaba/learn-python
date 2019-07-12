"""
@desc 异常处理

try
    finally:始终会执行

"""
import sys


def single_except_handler():
    while True:
        try:
            int(input("输入个数字"))
            break
        except ValueError:
            print("不对，请重输入")


# single_except_handler()

def multi_except_handler():
    try:
        f = open("file/foo1.log")
        s = f.readline()
        i = input(s.strip())  # 移除首尾空格
        print(i)
    except OSError as err:
        print("OS err:{0}".format(err))
    except ValueError:
        print("值转换失败")
    except:
        print("意外的异常", sys.exc_info()[0])
        raise

    else:  # 可选的，在没有发生异常时候执行
        print("正常!")


# multi_except_handler()

def custom_except_handler():
    class MyError(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

    try:
        raise MyError(2 * 9)
    except MyError as  er:
        print("我的异常捕获：", er)
    raise MyError("xxoo")


# custom_except_handler()


# finally

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("分母为0")
    else:
        print("result", result)
    finally:
        print("最后都到碗里来，finally")


divide(2, 0)
