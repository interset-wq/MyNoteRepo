"""打印文件中出现最多的10个汉字"""


f=open('命运.txt','r')
txt = f.read()
d={}
for i in txt:
    if i != "\n":
        d[i] = d.get(i,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)#此行可以按照词频由高到低排序
for k in range(10):
    print(ls[k][0],end='')
f.close()