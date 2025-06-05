"""
@desc 时间函数
"""
from datetime import date, datetime

now = date.today()  # YYYY-MM-DD 格式
print(now)

print('datetime.now()=>', datetime.now())
print('datetime.now().timestamp()=>', datetime.now().timestamp())
print('datetime.now().timestamp()x1000=>', datetime.now().timestamp()*1000)

# 时间戳
t = datetime.timestamp(datetime.now())
print('不要小点=>', int(t))

birthday = date(1993, 11, 1)

age = now - birthday  # 天数相减
print(age.days)
