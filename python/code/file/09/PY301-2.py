import jieba


with open('data2019.txt') as f1:
    txt1 = f1.read()
with open('data2018.txt') as f2:
    txt2 = f2.read()
word_set1 = set(item for item in jieba.lcut(txt1) if len(item) >= 2)
word_set2 = set(item for item in jieba.lcut(txt2) if len(item) >= 2)
both_set = word_set1 & word_set2
alone1 = word_set1 - both_set
alone2 = word_set2 - both_set
print('共有词语:' + ','.join(both_set))
print('2019特有:' + ','.join(word_set1))
print('2018特有:' + ','.join(word_set2))
