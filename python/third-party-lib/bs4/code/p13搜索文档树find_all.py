"""搜索文档树
.find_all()是bs4的核心方法
可以通过多种方式查找元素
返回Tag对象的列表
"""


from bs4 import BeautifulSoup, Tag
import requests, re

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

"""元素选择器查找元素"""
b = soup.find_all('b')
print(b) # [<b>The Dormouse's story</b>]

"""使用正则表达式的元素选择器"""
# 查找所有以b开头的标签
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
    # body
    # b

# 查找所有包含l的标签
for tag in soup.find_all(re.compile("l")):
    print(tag.name)
    # html
    # title

"""使用列表的元素选择器 查找多个标签"""
# 查找a标签和b标签
print(soup.find_all(["a", "b"])) # [<b>The Dormouse's story</b>, <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


"""查找所有标签 True"""
for tag in soup.find_all(True):
    print(tag.name)
    # html
    # head
    # title
    # body
    # p
    # b
    # p
    # a
    # a
    # a
    # p
    # script

"""自定义查找"""
# 定义一个函数设置查找规则
# 这个函数有且只有一个参数，这个参数就是Tag对象
# 必须返回布尔值，True表示符合规则
def has_class_but_no_id(tag: Tag) -> bool:
    """查找有类名但是没有id的标签"""
    return tag.has_attr('class') and not tag.has_attr('id')

print(soup.find_all(has_class_but_no_id))
    # [<p class="title">
    # <b>The Dormouse's story</b>
    # </p>, <p class="story">
    #         Once upon a time there were three little sisters; and their names were
    #         <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    #         ,
    #         <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    #         and
    #         <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    #         ; and they lived at the bottom of a well.
    #     </p>, <p class="story">...</p>]