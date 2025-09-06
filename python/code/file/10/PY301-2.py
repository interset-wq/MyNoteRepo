# 
# 以下代码仅供参考。
# 

import jieba


with open('clean.txt', encoding='utf-8') as f:
    txt = f.read()

words = jieba.lcut(txt)


d = {}

for word in words:
    if len(word) < 3:
        continue
    d[word] = d.get(word, 0) + 1

lt = list(d.items())
lt.sort(key = lambda x:x[1],reverse = True)
top10 = [f'{w}:{n}' for w,n in lt[:10]]
print(','.join(top10))
