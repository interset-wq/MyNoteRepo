from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

"""如果Tag对象只有一个子节点(HTML标签中不能嵌套标签)
.string返回被HTML标签包裹的字符串
如果有多个节点
返回None"""
# 有多个子节点返回None
p = soup.p
print(p)
    # <p class="title">
    # <b>The Dormouse's story</b>
    # </p>
print(p.string) # None

# 只有一个子节点返回被标签包裹的字符串
b = soup.b
print(b) # <b>The Dormouse's story</b>
print(b.string) # The Dormouse's story
