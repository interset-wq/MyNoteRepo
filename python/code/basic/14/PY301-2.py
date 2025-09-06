#
# 请在此文件作答
#
fi= open('webpage.txt')
datas = fi.readlines()
fo = open('images.txt','w')
for data in datas:
    if'.JPG' in data:
        data = data.split('src="")[1].split("')[0]
        fo.write(data+'\n')
fi.close()
fo.close()
