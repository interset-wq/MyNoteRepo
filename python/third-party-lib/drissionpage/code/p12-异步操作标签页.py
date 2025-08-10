"""异步操作浏览器标签页"""


from DrissionPage import Chromium
# 官方文档 https://docs.python.org/zh-cn/3.13/library/asyncio.html
import asyncio
# 官方文档 https://drissionpage.cn/DataRecorderDocs/usage/introduction/
from DataRecorder import Recorder
# 官方文档 https://loguru.readthedocs.io/en/stable/
from loguru import logger

# 定义异步采集方法
async def collect(tab, recorder, title, page=1):

    # 遍历所有标题元素
    for i in tab.eles('.title project-namespace-path'):
        # 获取某页所有库名称，记录到记录器
        recorder.add_data((title, i.text, page))
        logger.info((title, i.text, page))
        
    # 获取下一页按钮
    btn = tab('@rel=next', timeout=2)
    # 如果有下一页，点击翻页并递归调用自身
    if btn:
        btn.click(by_js=True)
        await asyncio.sleep(1)  # 异步等待
        # 增加页数并递归调用
        await collect(tab, recorder, title, page + 1)

# 主函数
async def main():
    # 新建浏览器对象
    browser = Chromium()
    # 第一个标签页访问网址
    tab1=browser.new_tab('https://gitee.com/explore/ai')
    # 新建一个标签页并访问另一个网址
    tab2 = browser.new_tab('https://gitee.com/explore/machine-learning')

    # 新建记录器对象
    recorder = Recorder('data.csv')

    # 创建异步任务
    task1 = asyncio.create_task(collect(tab1, recorder, 'ai'))
    task2 = asyncio.create_task(collect(tab2, recorder, '机器学习'))

    # 等待任务完成
    await task1
    await task2

    print("所有任务完成")
    # 保存文件
    recorder.record()

# 运行主函数
if __name__ == '__main__':
    asyncio.run(main())