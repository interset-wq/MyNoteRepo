"""将同一个人说的话拼接为一个字符串
并统计高频词出现次数"""

import jieba as j

f = open("talks.txt", "r", encoding='utf-8')
lines = f.readlines()
f.close()

ns = {}
for line in lines:  # 遍历 lines 的每一行ls，跳过空行
    line = line.strip()
    if not line:
        continue
    name, saying = line.strip("\n").split(":")  #去掉换行符，并将每行按照冒号分隔成两部分，分别代表人名和他们说的话
    ns[name] = ns.get(name,"") + saying #更新字典ts：以人名为键，追加该人对应的话到字典中
for name in ns:  # 遍历字典 ns 中的每一个人 r（键）
    wd = {}
    words = j.lcut(ns[name])  #使用jieba的lcut方法对每个人的全部发言进行分词，得到一个词列表words
    for word in words:
        wd[word]=wd.get(word,0)+1

    word_num_list = list(wd.items())
    word_num_list.sort(key=lambda x: x[1], reverse=True)
    print("{}说了{}个词, 其中top5是：".format(name, len(words)))
    for word, num in word_num_list[:5]:
        print((word, num), end='')
    print()

"""
alice说了35个词, 其中top5是：
('行政', 3)('的', 3)('心电图', 2)('更', 2)('心脏', 2)
bill说了45个词, 其中top5是：
('的', 5)('规模', 4)('停滞', 2)('或', 2)('秩序', 2)
jone说了19个词, 其中top5是：
('各种', 3)('肌肉', 3)('胖子', 1)('多', 1)('走', 1)
kate说了24个词, 其中top5是：
('保持', 2)('平衡', 2)('我们', 1)('生物', 1)('同样', 1)
herry说了26个词, 其中top5是：
('城市', 4)('的', 3)('为', 2)('体系', 1)('和', 1)
"""