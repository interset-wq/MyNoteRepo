import jieba


def find(txt):
    words = jieba.lcut(txt)
    word_dict = {}
    for word in words:
        if len(word) < 2:
            continue
        word_dict[word] = word_dict.get(word,0) + 1
    sorted_words = sorted(list(word_dict.items()), key=lambda x: x[1], reverse=True)
    top10 = [f'{x}:{y}' for x,y in sorted_words[:10]]
    return ','.join(top10)

with open('data2019.txt') as f1:
    txt1 = f1.read()
    print('2019:' + find(txt1))
with open('data2018.txt') as f2:
    txt2 = f2.read()
    print('2018:' + find(txt2))
