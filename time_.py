"""
@desc 时间函数
"""
from datetime import date

now = date.today()  # YYYY-MM-DD 格式
print(now)

birthday = date(1993, 11, 1)

age = now - birthday  # 天数相减
print(age.days)
