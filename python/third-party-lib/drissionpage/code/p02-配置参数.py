"""常用的可选配置参数"""

from DrissionPage import Chromium, ChromiumOptions

"""创建配置参数对象"""
options = ChromiumOptions()
# 选择控制的浏览器，edge通过edge://version查看版本，复制可执行文件地址，chrome通过chrome://version查看版本
options.set_browser_path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
# 忽视证书错误
options.ignore_certificate_errors()
# 不加载图片
options.no_imgs()
# 是否使用无头模式
options.headless(False)
# 浏览器启动端口
options.set_local_port(9696)

"""创建浏览器对象"""
browser = Chromium(options)
# 此时打开百度首页并不会显示百度的logo，因为禁用了加载图片
tab = browser.new_tab('https://www.baidu.com/')
