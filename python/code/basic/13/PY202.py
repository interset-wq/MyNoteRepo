#
# 在……上补充一行或多行代码
#
import jieba
s = input("请输入一段中文文本，句子之间以逗号或句号分隔：")
slist = jieba.lcut(s)
words = []

for i in slist:
   if i in "，。":
      continue
   words.append(i)
output = '/'.join(words) + '/'
m = len(words)
print(output)

print("\n中文词语数是：{}\n".format(m))
for sentence in s.strip('。').split('，'):
   print(sentence)
   
   

