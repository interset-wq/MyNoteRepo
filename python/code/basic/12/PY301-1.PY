# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f = open("八十天环游地球.txt", encoding="utf-8")

txt = f.read()
chs = txt.split('□ 作者：儒勒·凡尔纳\n')
titles = []
for ch in chs[:-1]:
    lines = ch.split('\n')

    titles.append(lines[0])

with open("八十天环游地球-章节.txt", 'w', encoding="utf-8") as fo:
    fo.write('\n'.join(titles))

f.close()

