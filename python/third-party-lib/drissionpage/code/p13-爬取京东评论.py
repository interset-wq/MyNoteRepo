"""爬取京东评论"""

import time
from DrissionPage import Chromium
from loguru import logger

# 设置日志记录到文件
logger.add("JD_comment.log", format="{time} {message}")

# 初始化浏览器
browser = Chromium()

# 打开京东首页
main_tab = browser.new_tab('https://www.jd.com/')

# 获取搜索框并输入关键词
search_input = main_tab.ele('tag:input@@id=key')
search_input.input('小米手机')

# 点击搜索按钮
main_tab('tag:button@@aria-label=搜索').click()

# 获取搜索结果列表
search_results = main_tab.eles('t:li@@class=gl-item')

# 打印每个搜索结果的文本
# for result in search_results:
#     logger.info(result)

# 点击搜索结果中的第二个商品以打开商品详情页
product_detail_tab = search_results[1].ele('t:a').click.for_new_tab()
# 点击评论标签页
product_detail_tab.ele('@data-anchor=#comment').click()

# 获取并打印商品评论
def get_comments(tab):
    for comment in tab.eles('t:div@@class=comment-item'):
        # logger.info(comment)
        
        logger.info(comment('.comment-con').text)  # 记录评论内容
        if recomment:=comment.ele('.recomment',timeout=2):
            logger.error(recomment.text)
        
        time.sleep(2)

# 获取第一页评论并点击下一页
get_comments(product_detail_tab)
product_detail_tab.ele('t:a@@rel=2').click()

# 循环获取剩余页码的评论
for _ in range(4):
    get_comments(product_detail_tab)
    product_detail_tab.ele('下一页').click()