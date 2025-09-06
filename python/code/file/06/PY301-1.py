# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

import jieba  #此处可多行

f = open('out1.txt','w')

with open('data.txt', 'r') as fo: #此处可用多行
    txt = fo.read()

word_list = []
words = jieba.lcut(txt)
for word in words:
    if word in word_list:
        continue
    if len(word) >= 3:
        word_list.append(word)

text = '\n'.join(word_list)
f.write(text)

f.close()
