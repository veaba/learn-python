"""
类型转换

"""

a = 12.1
b = 66
c = 3.14j
print(int(a))  # 12

print(float(a))  # 12.1
print(float(b))  # 66.0
print(c)
print(complex(c))
print(complex(a))  # (12.1+0j)
print(complex(b))  # (66.1+0j)
