#
# 请在此文件作答
#

f_data = open('data.txt', 'r')
f_studs = open('studs.txt', 'w')

name_scores = []
for line in f_data:
    name, classroom_score = line.strip('\n').split(':')
    _, score = classroom_score.split(',')
    name_score = name + ':' + score
    name_scores.append(name_score)

txt = '\n'.join(name_scores)
f_studs.write(txt)



f_data.close()
f_studs.close()

