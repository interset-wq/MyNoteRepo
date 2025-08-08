from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

"""对soup对象进行操作"""
# 以HTML标准格式美化
# print(soup.prettify())

# 获取浏览器标签页
print(soup.title) # <title>The Dormouse's story</title> (Tag对象)
print(soup.title.string) # The Dormouse's story (HTML标签包裹的文字)
print(soup.title.name) # title (HTML标签名)

# 获取Tag对象的父标签
print(soup.title.parent) # Tag对象head标签

# 通过元素选择器获取Tag对象
p = soup.p # Tag对象(第一个匹配到的p元素)
print(p)
print(p['class']) # ['title'] (获取p元素的类名列表)

# find_all()方法查找所有匹配
a_s = soup.find_all('a') # 查找所有a元素
print(a_s) # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
for a in a_s:
    print(a.get('href')) # 获取a元素的href属性
    # print(a['href']) # 和上面的写法作用效果相同

# find()方法查找第一个匹配
a = soup.find(id='link3') # Tag对象(匹配第一个id为link3的a元素)
print(a) # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a> 

# 获取HTML文件所有文字内容
print(soup.get_text()) # head和body标签中所有的静态文字内容