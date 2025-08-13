"""处理网页弹窗prompt"""


from DrissionPage import Chromium


browser = Chromium()
tab = browser.new_tab('https://zh.javascript.info/alert-prompt-confirm')

"""处理弹窗 确定"""
tab.eles('tag:a@@title=运行')[0].click()
tab.wait(3)
msg = tab.handle_alert(accept=True)
print(msg)

tab.eles('tag:a@@title=运行')[1].click()
tab.wait(3)
msg = tab.handle_alert(accept=True)
print(msg)

"""处理弹窗 取消"""
tab.eles('tag:a@@title=运行')[1].click()
tab.wait(3)
tab.handle_alert(accept=False)
