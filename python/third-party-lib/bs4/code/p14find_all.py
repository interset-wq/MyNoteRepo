"""
.find_all( name , attrs , recursive , string , **kwargs )

Args:
    name (str): 元素选择器 可以配合正则表达式使用
    attrs (dict[str,str]): 属性选择器
    recursive=False: 只匹配直接子节点
    string: 查找字符串 可以配合正则表达式

kwargs:
    id (str): id选择器
    href (str): 通过标签的href属性查找 可以配合正则表达式
    class_ (str): 类选择器 如果某个类有多个值，可以把它看作是一个整体，也可以不看做整体
    limit (int): 限制查找到结果的数量
"""

"""fin_all的简写 以下写法等价
soup.find_all("a")
soup("a")
"""


from bs4 import BeautifulSoup, Tag
import requests, re

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

"""元素选择器"""
# 查找标签为title的元素
print(soup.find_all("title")) # [<title>The Dormouse's story</title>]

"""id选择器"""
# 查找id是link2的标签
print(soup.find_all(id="link2")) # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
# 查找有id属性的标签
print(soup.find_all(id=True)) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

""""""
print(soup.find(string=re.compile("sisters")))
    #
    #        Once upon a time there were three little sisters; and their names were
    #

"""通过href查找"""
print(soup.find_all(href=re.compile("elsie"))) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]


"""更精确的查找 可以通过标签的多个属性实现更精确的查找"""
print(soup.find_all(href=re.compile("elsie"), id='link1')) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

"""属性选择器"""
# 属性选择器 id="link3"
print(soup.find_all(attrs={'id': 'link3'})) # [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# id选择器
print(soup.find_all(id='link3')) # [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

"""类选择器"""
# 查找 class="title"的元素
print(soup.find_all(class_='title'))
    # [<p class="title">
    # <b>The Dormouse's story</b>
    # </p>]