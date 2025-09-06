# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

import re  # 此处可多行
fi = open('data.txt', 'r')
txt = fi.read()
fi.close()

f = open("univ.txt", "w")

  # 此处可多行
pattern = 'alt="(.*?)"'
colleges = re.findall(pattern,txt)

content = '\n'.join(colleges)
f.write(content)


f.close()
