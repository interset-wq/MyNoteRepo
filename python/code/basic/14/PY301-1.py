#
# 请在此文件作答
#
fi = open('webpage.txt')
datas = fi.readlines()
num=0
for data in datas:
    if'.JPG' in data:
        num += 1
print(num)
fi.close()
