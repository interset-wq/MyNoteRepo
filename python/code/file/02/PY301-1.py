# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f = open('sensor.txt', encoding='utf-8')
fo = open('earpa001.txt', mode='w', encoding='utf-8')
for line in f.readlines():
    words = line.split(',')
    if ' earpa001' not in words:
        continue
    fo.write('{},{},{},{}\n'.format(words[0], words[1], words[2], words[3]))
f.close()
fo.close()

