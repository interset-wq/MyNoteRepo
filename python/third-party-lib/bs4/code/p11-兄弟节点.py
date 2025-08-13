"""遍历文档树 兄弟节点"""

from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

# 第二个a标签
a_2 = soup.find(id='link2')
# print(a_2) # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>

"""获取兄弟节点
.previous_slibing 上面的兄弟节点
.previous_slibings 上面的所有兄弟节点 迭代器
.next_slibing 下面的兄弟
.next_slibings 下面的所有兄弟 迭代器
"""
# 上面的兄弟节点 不一定是html标签
a_2_pre = a_2.previous_sibling
print(a_2_pre) #         ,
# 下面的兄弟
a_2_next = a_2.next_sibling
print(a_2_next) #         and