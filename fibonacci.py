"""
斐波那契数列
"""
"""
@desc 计算右边表达式，同时赋值给左边  
a,b=b,a+b # a=b,b=a+b
==>
n=b
m=a+b
a=n
b=m

"""

a, b = 0, 1
while b < 10:
    print(b, end="=>")
    a, b = b, a + b  # => 和上面的一样。a=b,b=a+b
