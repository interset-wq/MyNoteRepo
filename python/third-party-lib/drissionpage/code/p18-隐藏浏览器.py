"""隐藏浏览器"""

from DrissionPage import Chromium, ChromiumOptions

# 自定义浏览器选项
co = ChromiumOptions()
co.set_browser_path(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
co.set_local_port(9696)

"""方法一 使用无头模式"""
# co.headless(True)

"""方法二 把浏览器窗口放在显示屏之外"""
co.set_argument('--window-position=32000,32000')

# 创建浏览器对象
browser = Chromium(co)

"""方法三"""
# browser.latest_tab.set.window.hide()

# 创建标签页对象
tab = browser.new_tab('https://www.baidu.com')