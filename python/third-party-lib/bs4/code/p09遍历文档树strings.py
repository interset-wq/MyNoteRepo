from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/third-party-lib/bs4/code/demo.html'
# 发送请求
res = requests.get(url)
# 创建soup对象
soup = BeautifulSoup(res.text, 'html.parser')

story_p = soup.find(class_="story")
print(story_p)
    # <p class="story">
    #         Once upon a time there were three little sisters; and their namrs; and their names were
    #         <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    #         ,
    #         <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    #         and
    #         <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    #         ; and they lived at the bottom of a well.
    #     </p>
print('------')

"""
.strings返回迭代器 通过遍历可以获取所有的字符串
.stripped_strings 在.strings的基础上删除所有空白字符
"""
for child_str in story_p.strings:
    print(child_str)
    """

            Once upon a time there were three little sisters; and their names were

    Elsie

            ,

    Lacie

            and

    Tillie

            ; and they lived at the bottom of a well.

    """
print('-------')
for child_str in story_p.stripped_strings:
    print(child_str)
    """
    Once upon a time there were three little sisters; and their names were 
    Elsie
    ,
    Lacie
    and
    Tillie
    ; and they lived at the bottom of a well.
    """