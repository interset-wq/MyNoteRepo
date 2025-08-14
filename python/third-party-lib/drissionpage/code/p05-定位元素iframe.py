"""定位iframe元素"""

from DrissionPage import Chromium

# 连接浏览器并获取浏览器对象
browser = Chromium()  
# 获取标签页对象并打开网址
tab = browser.new_tab('https://drissionpage.cn/demos/iframe_diff_domain.html')

"""定位iframe元素"""
# 方法1
iframe = tab.get_frame('t:iframe') #最规范
ele = iframe.ele('网易首页')
print(ele)
# 方法2
iframe = tab.ele('t:iframe') #最简洁
ele = iframe('网易首页')
print(ele)
# 方法3
iframe = tab.eles('t:iframe')[0]  # 成功率最高
ele = iframe('网易首页')
print(ele)