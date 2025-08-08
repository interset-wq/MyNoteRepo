"""标签页对象"""

from DrissionPage import Chromium

# 创建浏览器对象
browser = Chromium()  
# 获取标签页对象并打开网址
tab1 = browser.new_tab('https://www.baidu.com')
tab2 = browser.new_tab('https://www.bing.com')
tab3 = browser.latest_tab # 激活的标签页，被鼠标光标控制的标签页
print(tab1.title) # 百度一下，你就知道
print(tab2.title) # 搜索 - Microsoft 必应
print(tab3.title) # 搜索 - Microsoft 必应
browser.latest_tab.close() # 关闭最新的标签页

# 标签页没有Selenium所谓的焦点的概念，多个标签页可以并行操作，所以可以多线程同时打开多个标签页

from concurrent.futures import ThreadPoolExecutor

def open_url(browser: Chromium, url): 
   browser.new_tab(url)

chinese_websites = [
    "https://www.taobao.com",   # 淘宝
    "https://www.tmall.com",   # 天猫
    "https://www.jd.com",     # 京东
]   
# 使用线程池
with ThreadPoolExecutor(max_workers=3) as executor:
  for url in chinese_websites:
    executor.submit(open_url, browser, url)
