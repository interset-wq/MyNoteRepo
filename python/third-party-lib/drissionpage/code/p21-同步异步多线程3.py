"""异步(协程)
在某个任务等待时 去执行其他任务
例如 打开电饭煲煮饭之后 需要等饭煮熟才可以吃
在等待的事件中 我可以去打扫卫生
打扫卫生结束之后 继续回到电饭煲煮饭的任务
通过asyncio和异步函数实现异步
同步是一个人依次执行多个任务
异步是一个人在任务等待时切换执行其他任务
多线程是多个人分别执行不同的任务
异步比多线程更节省资源 而且比同步效率更高
"""

import asyncio
from typing import Coroutine, List
from DrissionPage import Chromium

browser = Chromium()

async def baidu_search(kw: str):
    """百度搜索函数，每个线程将执行此函数"""
    tab = browser.new_tab()
    tab.get('https://www.baidu.com/')
    # 异步等待 等待网页加载的同时执行其他任务
    await asyncio.sleep(2)
    tab.ele('@@id=kw').input(kw)
    try:
        tab.ele('@@id=su').click()
    except:
        tab.ele('@@id=chat-submit-button').click()
    # 异步等待
    await asyncio.sleep(2)

async def main():
    """事件循环"""

    keywords: List[str] = ['python', 'html', 'css']
    # 创建任务列表
    tasks: List[Coroutine] = []
    for keyword in keywords:
        tasks.append(baidu_search(keyword))
    # 并发执行所有任务
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    # 启动事件循环
    asyncio.run(main())
