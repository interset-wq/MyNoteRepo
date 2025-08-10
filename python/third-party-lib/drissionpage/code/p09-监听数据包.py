"""监听数据包"""

from DrissionPage import Chromium, ChromiumOptions
from pprint import pprint

# 连接浏览器并获取浏览器对象
browser = Chromium()
tab = browser.latest_tab
# 开始监听
tab.listen.start('spa1.scrape.center/api/movie')#开始监听，指定获取包含该文本的数据包，注意：要先开启监听再打开对应的页面
# 打开url
tab.get('https://spa1.scrape.center/') #访问网址，这行产生的数据包不监听
for packet in tab.listen.steps():
    pprint(packet.response.body)