"""获取元素的信息"""

from DrissionPage import Chromium

browser = Chromium()
tab = browser.new_tab('https://www.baidu.com/')

# 通过id定位元素获取Element对象
ai = tab.ele('@id=csaitab')

"""获取元素的信息"""
# 获取被HTML标签包裹的文字
print(ai.text) #
# 获取a元素的href属性
print(ai.link) # https://chat.baidu.com/search?isShowHello=1&pd=csaitab&setype=csaitab&extParamsJson=%7B%22enter_type%22%3A%22home_tab%22%7D (这个锚点元素的href属性)
# 获取这个元素的HTML
print(ai.html) # 这个锚点元素的HTML
# 获取这个元素的类名
print(ai.attr('class')) # mnav c-font-normal c-color-t

# 获取视口坐标（相对浏览器窗口左上角的坐标）
print(ai.rect.viewport_midpoint) # (454.38751220703125, 30)
# 获取屏幕坐标（相对电脑屏幕左上角的坐标）
print(ai.rect.screen_location) # (551.7343902587891, 131.25)

# 通过id定位百度logo元素
logo = tab.ele('@id=s_lg_img')
# 下载百度logo，保存到当前目录
logo.save(name='baidu_logo.png')