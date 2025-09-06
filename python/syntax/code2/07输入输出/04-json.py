"""如果需要写入的是python字典或列表
建议直接通过json写入
这样读取文件时能更方便使用文件中的内容


标准库模块 json 可以接受带有层级结构的 Python 数据，
并将其转换为字符串表示形式；这个过程称为 serializing。 
根据字符串表示形式重建数据则称为 deserializing。 
在序列化和反序列化之间，用于代表对象的字符串可以存储在文件或数据库中，
或者通过网络连接发送到远端主机。"""


import json
x = [1, 'simple', 'list']


# 将python列表转换为json字符串
# dump()方法 将python对象转换为json字符串，并保存到指定文件
j_str = json.dumps(x)
print(j_str) # [1, "simple", "list"]

# 将json字符串转换为python列表或字典
print(json.loads(j_str)) # [1, 'simple', 'list']