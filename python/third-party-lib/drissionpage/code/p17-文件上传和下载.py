"""文件上传和下载"""


from DrissionPage import Chromium

browser = Chromium()
tab = browser.new_tab('https://picui.cn/upload')

"""上传文件 将图片上传到图床"""
# 本地文件地址
upload_file_path = r"F:\Pictures\img2.jpg"
# 定位上传按钮,等待上传
tab.ele('选择图片').click.to_upload(upload_file_path)
tab.wait(3)
tab.ele('@text():上传这张图片').click()
tab.wait.ele_displayed('上传成功')
print('已上传')
tab.wait(3)
# 获取上传图片完成,图床提供的图片url
img_url = tab.ele('@data-tab=url').text
print(img_url)

"""下载文件 下载刚刚上传到图床的文件"""
tab.download(img_url, rename='img.jpg', goal_path=r'C:\Desktop')

"""下载文件 下载qq安装包"""
# 接管标签页
tab2 = browser.latest_tab
# 访问QQ官网
tab2.get('https://im.qq.com/pcqq/index.shtml')
# 定位下载按钮
btn = tab2('@text():全新版本下载')
print(btn)
# 等待下载按钮加载完成
btn.wait.has_rect()
# 点击下载
mission = btn.click.to_download(save_path=r'C:\Desktop', rename='qq.exe')
mission.wait()