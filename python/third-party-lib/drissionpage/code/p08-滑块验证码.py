"""模拟通过滑块验证码"""

from DrissionPage import Chromium, ChromiumOptions

options = ChromiumOptions().use_system_user_path()
browser = Chromium()

tab = browser.new_tab('https://dun.163.com/trial/sense')
tab.wait(1)

# 通过元素的文本内容定位元素
tab.ele('可疑用户-滑动拼图').click()
tab.ele('点击完成验证').click()

# 使用css选择器定位滑块元素
slider = tab.ele('css:.yidun_slider')
# 移动滑块，运行失败
x = 20
y = 2
tab.actions.move_to(slider).hold(slider).move(offset_x=x, offset_y=y, duration=2.5).release()
