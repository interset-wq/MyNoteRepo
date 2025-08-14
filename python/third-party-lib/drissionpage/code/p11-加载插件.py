"""加载插件 定位插件中的元素"""


from DrissionPage import Chromium,ChromiumOptions

# 插件下载  https://www.crxsoso.com/
# 这里使用的是本地插件（下载到此电脑中的插件）
# 传入的参数为插件目录的绝对路径
options=ChromiumOptions().add_extension(r'E:\DP_helper_7.9\DP_helper')    

# 连接浏览器并获取浏览器对象
browser = Chromium(options)  

# 获取标签页对象并打开网址
tab = browser.new_tab('https://www.baidu.com/')

tab.wait(3)
# 浏览器插件本质上是一个网页
# 通过开发者工具可以获取插件的url,谷歌plugin_url以chrome-extension://开头
plugin_url='chrome-extension://njefpdhdonjcjmhllbppkkndmikdeomg/popup.html'

tab.get(plugin_url)

"""模拟鼠标点击插件上的元素"""
tab.ele('📌DrissionPage 官网').click()
tab.ele('📌骚神网').click()
tab.ele('css:.slider').click()
