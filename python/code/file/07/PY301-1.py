# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改



L=[]                          #L中的元素是学生原始成绩和总成绩

with open('score.txt') as f:  #此处可多行
    for line in f.readlines():
        scores = line.strip('\n').split()
        total = 0
        for i in scores[2:]:
            total += int(i)
        scores.append(str(total))
        L.append(scores)

L.sort(key=lambda x:x[-1],reverse=True)   #按学生总成绩从大到小排序

with open('candidate0.txt', 'w') as fi:  #此处可多行
    for item in L[:10]:
        fi.write(' '.join(item[:-1]) + '\n')


    
