"""
位操作符
"""
a = 0b00111100  # 60
b = 0b00001101  # 13

print(a & b)  # 12

print(a | b)  # 61

print(a ^ b)  # 49

print(~b)  # -14
print(~a)  # -61
print(a << 2)  # 240
print(a >> 2)  # 15
