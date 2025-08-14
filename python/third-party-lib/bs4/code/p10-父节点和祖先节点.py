"""遍历文档树 父节点和祖先节点"""

from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

# 标签名为title的tag对象
title = soup.title 
# print(title) # <title>The Dormouse's story</title>

"""通过.parent获取父节点
通过.parents获取祖先节点 迭代器
html标签的父节点是BeautifulSoup对象
"""
# 获取title的父节点
head = title.parent
print(head)
    # <head>
    # <meta charset="utf-8"/>
    # <title>The Dormouse's story</title>
    # </head>

# 获取title的父辈节点
for parent in title.parents:
    print(parent.name, type(parent))
    # head <class 'bs4.element.Tag'>
    # html <class 'bs4.element.Tag'>
    # [document] <class 'bs4.BeautifulSoup'>