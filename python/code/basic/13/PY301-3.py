#
# 请在此文件作答
#


f_data = open('data.txt', 'r')


scores = {}
nums = {}
for line in f_data:
    _, classroom_score = line.strip('\n').split(':')
    classroom, score = classroom_score.split(',')
    scores[classroom] = scores.get(classroom, 0) + int(score)
    nums[classroom] = nums.get(classroom,0) + 1

for classroom, score in scores.items():
    print(f'{classroom}:{score/nums[classroom]:.2f}')
f_data.close()
