from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

story_p = soup.find(class_="story")

""".contents获取直接子节点列表
html中的缩进也会被当作是空白字符
字符串没有.contents属性,因为字符串没有子节点
.children与.contents相同,只不过children返回的是迭代器,用于遍历"""
child_list = story_p.contents
print(child_list) # ['\r\n        Once upon a time there were three little sisters; and their names were\r\n        ', <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, '\r\n        ,\r\n        ', <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, '\r\n        and\r\n        ', <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>, '\r\n        ; and they lived at the bottom of a well.\r\n    ']
print(child_list[0]) #         Once upon a time there were three little sisters; and their names were
print(story_p.children) # <list_iterator object at 0x000001D199470880>

""".descendants获取所有后代节点
返回迭代器"""
des_list = story_p.descendants
print(list(des_list))
print('----------')
for des in story_p.descendants:
    print(des)


#         Once upon a time there were three little sisters; and their names were

# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a> 
# Elsie

#         ,

# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> 
# Lacie

#         and

# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# Tillie

#         ; and they lived at the bottom of a well.
