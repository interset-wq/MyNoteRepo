from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

p = soup.p

"""获取Tag对象的属性"""
# 方法一：字典通过键取值
print(p['class']) # ['title'] (由于HTML中的class是多值属性，所以返回列表。如果不是多值属性，则返回字符串)

# 方法二：.attrs获取属性字典
print(p.attrs) # {'class': ['title']}

# 属性可以增加，修改，删除，操作方法和字典相同