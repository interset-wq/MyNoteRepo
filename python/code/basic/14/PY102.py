#
# 编写代码替换横线
#

s = input("请输入5个小写字母：")
uppers = s.upper()[::-1]
print(','.join(uppers))
