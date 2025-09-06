# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

import jieba

f = open("八十天环游地球.txt", encoding="utf-8")

txt = f.read()
chs = txt.split('□ 作者：儒勒·凡尔纳\n')
output = ''
for ch in chs[:-1]:

    title = ch.split('\u3000')[0]
    
    times_dict = {}
    words = jieba.lcut(ch)
    for word in words:
        if len(word) < 2:
            continue
        times_dict[word] = times_dict.get(word,0) + 1
    times_list = list(times_dict.items())
    times_list.sort(key=lambda x:x[1], reverse=True)
    output += f'{title} {times_list[0][0]} {times_list[0][1]}\n'
    
print(output)

f.close()

