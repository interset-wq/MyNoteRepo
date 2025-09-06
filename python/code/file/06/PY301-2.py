# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

import jieba # 此处可多行
f1 = open('data.txt')
f2 = open('out2.txt', 'w')
txt = f1.read()
f1.close()

d = {}

words = jieba.lcut(txt)
for word in words: # 此处可多行
    if len(word)>=3:
        d[word] = d.get(word,0) + 1
    
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True) # 此行可以按照词频由高到低排序

for item in ls:  # 此处可多行
    line = '{}:{}\n'.format(item[0],item[1])
    f2.write(line)
f2.close()




