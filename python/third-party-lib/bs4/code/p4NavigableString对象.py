from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.title
print(title) # <title>The Dormouse's story</title>

"""通过.string返回的是NavigableString对象"""
print(title.string) # The Dormouse's story
print(type(title.string)) # <class 'bs4.element.NavigableString'>
