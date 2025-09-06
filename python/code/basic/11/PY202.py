# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f = open('data.txt', 'r',encoding="utf-8")

country_num_dict = {}
unis_country_list = []

for line in f:
    line = line.rstrip('\n')
    if not line:
        continue
    words = line.split(',')[1:]
    country = words[1]
    country_num_dict[country] = country_num_dict.get(country, 0) + 1
    unis_country_list.append(words)

unis = []
for country,num in country_num_dict.items():
    item = [country, num]
    for college, country1 in unis_country_list:
        if country1 == country:
            item.append(college)
    unis.append(item)

    
    

    
f.close()
for d in unis:
    print('{:>4}: {:>4} : {}'.format(d[0], d[1], ' '.join(d[2:])))
