from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

"""Tag对象(html标签)中
嵌套的Tag对象(HTML标签)和字符串
都是这个Tag对象的字节点"""

"""获取子节点
通过.获取第一个匹配到的标签"""
# 获取head元素
head = soup.head
print(head)
    # <head>
    # <meta charset="utf-8"/>
    # <title>The Dormouse's story</title>
    # </head>

# 获取title标签
title = soup.title
print(title) # <title>The Dormouse's story</title>

# 获取body元素中嵌套的第一个b元素
b = soup.body.b 
print(b) # <b>The Dormouse's story</b>

# 获取所有的a元素
print(soup.find_all('a')) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]