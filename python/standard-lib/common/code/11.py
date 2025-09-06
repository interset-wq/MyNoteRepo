# 方便地构造和格式化日期值
from datetime import date

"""获取当前日期"""
now = date.today()
print(now) # 2025-08-24

"""时间格式化"""
format_now = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(format_now) # 08-24-25. 24 Aug 2025 is a Sunday on the 24 day of August.

"""日期计算"""
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)