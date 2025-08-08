from DrissionPage import Chromium

# 创建浏览器对象
browser = Chromium()
# 打开一个新标签页
tab = browser.new_tab('https://www.baidu.com/')