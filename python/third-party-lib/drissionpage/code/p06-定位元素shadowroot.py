"""定位shadow root元素"""


from DrissionPage import Chromium

# 连接浏览器并获取浏览器对象
browser = Chromium()  

# 获取标签页对象并打开网址

tab = browser.new_tab('https://spiderapi.cn/captcha/turnstile-managed/')

"""定位shadow root的父元素"""
# 由于shadow root的父元素div没有任何属性，因此需要先定位这个div的兄弟元素p
p=tab.ele('@id=cf-wait')
div=p.after(1)
print(div.html)

# 定位shadow root中的iframe元素
iframe_ele=div.sr("t:iframe")
print(iframe_ele)