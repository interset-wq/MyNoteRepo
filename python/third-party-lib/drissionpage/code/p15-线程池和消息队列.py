

from DrissionPage import Chromium, ChromiumOptions
import threading
import concurrent.futures
import time
import queue
from loguru import logger

# 创建一个队列用于存储标签页对象
标签页队列= queue.Queue()

# 启动浏览器并获取标签页对象
co = ChromiumOptions()
browser = Chromium(co)

tab_instance = browser.new_tab('https://www.bigee.cc/book/20233/')

# 获取所有章节链接


链接列表=[i.link   for i in  tab_instance('t:div@@class=listmain').eles('t:a')   if 'book' in i.link]
# 链接列表=链接列表[:15]
print(链接列表)


def 打开网页(url):
    if url is None:
        return
    t = browser.new_tab(url)
    标签页队列.put(t)    
    logger.info(f'{t.title} 该网页已经打开')
    time.sleep(2)

def 采集网页数据():
    while True:
        t = 标签页队列.get()
        if t is None: # 如果获取的消息为None，则退出循环
            break
        logger.error(t.ele('#chaptercontent').text[:15])        
        threading.Thread(target=t.close).start()
        
        logger.warning(f'{t.title} 已经完成抓取...')
    print('数据采集完成')    




采集线程数=6

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor1,   concurrent.futures.ThreadPoolExecutor(max_workers=采集线程数) as executor2:
    
    # 提交任务到网页打开线程池
    pool1 =  [executor1.submit(打开网页, chapter_url)   for  chapter_url in  链接列表]  

    time.sleep(1)

    # 提交任务到第网页数据采集线程池
    pool2 =  [executor2.submit(采集网页数据)   for  i in  range(采集线程数)]

    # 等待线程池1所有任务完成
    concurrent.futures.wait(pool1)

    # 批量添加结束标记，通知线程池2关闭
    [标签页队列.put(None)   for _ in range(采集线程数)]

  


    
