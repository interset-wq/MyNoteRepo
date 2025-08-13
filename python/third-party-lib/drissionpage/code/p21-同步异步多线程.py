"""同步
按照顺序执行任务
完成第一个任务之后 才能开始第二个任务
如果某个任务没有完成 后面的任务也无法开始
例如 python某行代码报错了 那后面的代码也就无法执行了
python代码默认按照这种方式执行
"""

from DrissionPage import Chromium
from time import sleep

browser = Chromium()

def baidu_search(kw: str):
    tab = browser.new_tab()
    tab.get('https://www.baidu.com/')
    sleep(2)
    tab.ele('@@id=kw').input(kw)
    try:
        tab.ele('@@id=su').click()
    except:
        tab.ele('@@id=chat-submit-button').click()

if __name__ == '__main__':
    keywords = ['python', 'html', 'css']
    for keyword in keywords:
        baidu_search(keyword)