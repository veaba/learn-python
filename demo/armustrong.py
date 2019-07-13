# 1^3+5^3+3^3=153


def armustrong(num):
    sum1 = 0  # 初始变量
    n = len(str(num))  # 质数
    temp = num
    while temp > 0:
        digit = temp % 10
        sum1 += digit ** n
        temp //= 10
        print("---------------")
        print("n:", n)
        print("sum:", sum1)
        print("temp:", temp)
        print("digit:", digit)
        print("digit:", digit)
        print("++++++++++++++")
    if num == sum1:
        print('is')
    else:
        print('no')


armustrong(154)
