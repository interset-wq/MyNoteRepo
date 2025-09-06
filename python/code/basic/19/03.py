"""判断输入的字符串是否全是小写字母"""

a, i = 0, 0
ss = input("请输入字符串：")
for a in range(len(ss)):
    if ss[a].islower():
        i += 1
    else:
        break
if i < len(ss):
    print("不全是英文字母", ss[i])
else:
    print("全部都是英文字母")