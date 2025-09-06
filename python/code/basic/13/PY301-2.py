#
# 请在此文件作答
#

f_data = open('data.txt', 'r')

name_scores = []
for line in f_data:
    name, classroom_score = line.strip('\n').split(':')
    _, score = classroom_score.split(',')
    name_scores.append((name,int(score)))

name_scores.sort(key=lambda x:x[1],reverse=True)
print(name_scores[0][0] + ':' + str(name_scores[0][1]))


f_data.close()
