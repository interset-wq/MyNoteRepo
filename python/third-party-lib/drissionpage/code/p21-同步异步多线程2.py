"""多线程
同时执行多个任务 并且任务资源共享
例如 三个人分别去买三种商品 但是它们用的是同一张银行卡账号支付
通过threading或concurrent.futures可以实现多线程
使用concurrent.futures更简便
"""

from time import sleep
from DrissionPage import Chromium
from threading import Thread

# 初始化浏览器实例（共享资源）
browser = Chromium()

def baidu_search(kw: str):
    """百度搜索函数，每个线程将执行此函数"""
    tab = browser.new_tab()
    tab.get('https://www.baidu.com/')
    tab.ele('@@id=kw').input(kw)
    try:
        tab.ele('@@id=su').click()
    except:
        tab.ele('@@id=chat-submit-button').click()

if __name__ == '__main__':
    keywords = ['python', 'html', 'css']
    threads = []

    """通过concurrent.futures实现多线程"""
    # with ThreadPoolExecutor(max_workers=3) as executor:
    #     for keyword in keywords:
    #         executor.submit(baidu_search, keyword)

    """通过threading实现多线程"""
    # 创建并启动线程
    for keyword in keywords:
        thread = Thread(target=baidu_search, args=(keyword,))
        threads.append(thread)
        thread.start()  # 启动线程
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()
