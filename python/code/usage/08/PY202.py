#请完善如下代码
#在....处填写多行代码，不得修改其他代码
#PY202.py


while True:
    s = input("请输入不带数字的文本:")
    flag = True
    for char in s:
        if char in '0123456789':
            flag = False
            break
    if flag:
        break
print(len(s))
