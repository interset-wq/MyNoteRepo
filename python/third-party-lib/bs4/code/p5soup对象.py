from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
"""soup对象可直接当作Tag对象处理"""
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.name) # [document]