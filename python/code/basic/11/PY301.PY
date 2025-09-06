# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

import jieba

f = "红楼梦.txt"
sf = "停用词.txt"

with open(f, encoding='utf-8') as f1:
    txt1 = f1.read()

with open(sf,encoding='utf-8') as f2:
    txt2 = f2.read()

words = jieba.lcut(txt1)
for word in words:
    if word in ['凤姐','凤姐儿', '凤丫头']:
        word = '凤姐'
    elif word in ['宝玉','二爷', '宝二爷']:
        word = '宝玉'
    elif word in ['黛玉','颦儿', '林妹妹','黛玉道']:
        word = '黛玉'
    elif word in ['宝钗','宝丫头']:
        word = '宝钗'
    elif word in ['贾母','老祖宗']:
        word = '贾母'
    elif word in ['袭人','袭人道']:
        word = '袭人'
    elif word in ['贾政','贾政道']:
        word = '贾政'
    elif word in ['贾琏','琏二爷']:
        word = '贾琏'

d = {}
for word in words:
    if word in txt2:
        continue
    d[word] = d.get(word,0) + 1
items = list(d.items())
items.sort(key=lambda x:x[1], reverse=True)
# 此行语句可以对items列表进行递减排序
csv = open('result.csv', 'w',encoding='utf-8')
txt = ''
for name,num in items:
    if num >= 40:
        txt += f'{name},{num}\n'
csv.write(txt)
csv.close()
