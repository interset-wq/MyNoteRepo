"""
.find()是bs4的另一个核心方法，和find_all()用法相同
find()只匹配第一个
"""

"""简写 只能通过元素选择器定位
以下两种写法等价
soup.head.title
# <title>The Dormouse's story</title>

soup.find("head").find("title")
# <title>The Dormouse's story</title>
"""