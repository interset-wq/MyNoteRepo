# 
# 以下代码仅供参考。
# 


with open('data.txt', encoding='utf-8') as f:
    txt= f.read()
output = ''

for char in txt:
    if char in '，。？；：‘’“”【】（）\n  ':
        continue
    output += char
with open('clean.txt', 'w', encoding='utf-8') as fo:
    fo.write(output)
