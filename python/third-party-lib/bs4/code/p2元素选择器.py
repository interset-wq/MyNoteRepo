from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

"""元素选择器"""
# 可以把所有的HTML标签名看作是soup对象和tag对象的属性

# 使用元素选择器匹配第一个p元素
p = soup.p # Tag对象(p标签)
print(p)
    # <p class="title">
    # <b>The Dormouse's story</b>
    # </p>
print(p.name) # p (标签名)

# 可以对标签名重新赋值
p.name = 'div'
print(p)
    # <div class="title">
    # <b>The Dormouse's story</b>
    # </div>