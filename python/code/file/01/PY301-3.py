"""输出文字和出现的次数到文件中"""

f = open('命运.txt','r')
fi= open('命运-频次排序.txt','w')
txt = f.read()
d={}
for i in txt:
    if i != '\n':
        d[i] = d.get(i,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)#此行可以按照词频由高到低排序
s=''
for k in ls:
    s+="{}:{}".format(k[0],k[1])+','
fi.write(s[:-1])
f.close()
fi.close()