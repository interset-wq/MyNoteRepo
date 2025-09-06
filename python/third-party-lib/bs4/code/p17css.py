"""直接使用css选择器匹配"""


from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

"""
.css.select()和.find_all()类似 返回Tag对象的列表
.css.select()可以简写为.select()
.iselect()与.select()效果相同，返回迭代器

.css.select_one()和.find()类似
.css.select_one()可以简写为.select_one()
"""

# 元素选择器
print(soup.css.select('title')) #[<title>The Dormouse's story</title>]
# 伪类选择器
print(soup.css.select("p:nth-of-type(3)")) # [<p class="story">...</p>]
# 后代选择器
print(soup.css.select("html head title")) # [<title>The Dormouse's story</title>]
# 子代选择器
print(soup.css.select("p > a")) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>] 
print(soup.css.select("p > #link1")) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
# 兄弟选择器
print(soup.css.select("#link1 ~ .sister")) # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# 类选择器
print(soup.css.select(".sister")) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# id选择器
print(soup.css.select("#link1")) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
# 查找多个选择器 查找id="link1"和id="link2"的元素
print(soup.css.select("#link1,#link2")) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
# 查找有href属性的a
print(soup.css.select('a[href]')) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# 属性查找
print(soup.css.select('a[href="http://example.com/elsie"]')) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
