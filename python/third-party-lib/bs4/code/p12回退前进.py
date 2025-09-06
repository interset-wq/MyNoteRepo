"""遍历文档树 回退和前进
按照html解析的顺序解析
"""


from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

link3 = soup.find(id='link3')
print(link3) # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

""".next_element解析下一个对象 浏览器解析html时，先解析id为link3的标签
然后再解析这个标签里面的内容，里面的内容都解析完毕之后，解析下一个标签
.previous_element与.next_element相反"""
print(link3.next_element) # Tillie
print(link3.next_element.next_element)
    #
    #        ; and they lived at the bottom of a well.
    #

""".previous_elements和.next_elements迭代器 一直向上或向下解析"""