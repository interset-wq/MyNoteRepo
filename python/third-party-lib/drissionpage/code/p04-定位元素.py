"""定位元素"""

from DrissionPage import Chromium

# 创建浏览器对象
browser = Chromium()  

# 获取标签页对象并打开网址
tab = browser.new_tab('https://www.baidu.com')

# 定位并点击百度首页顶部导航的文库
wenku_button=tab.ele('文库') #最简单
wenku_button.click()

# 通过id定位到百度的搜索框，并模拟输入
input_box=tab.ele('@id=kw') #最常用
input_box.input('1234')

# 通过标签名，type，id，value属性定位百度一下搜索按钮，并模拟鼠标点击
search_button=tab.ele('tag:input@@type=submit@@id=su@@value=百度一下') #最精确
search_button.click()