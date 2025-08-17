"""统计文件中出现的最多次数的汉字"""


f = open('命运.txt','r')
txt = f.read()
d = {}
for i in txt:
    if i not in "\"：，。？！《》【】“”\n":
        d[i] = d.get(i, 0)+1
s = list(d.items())
s.sort(key=lambda x:x[1],reverse = True)
print("{}:{}".format(s[0][0],s[0][1]))
f.close()