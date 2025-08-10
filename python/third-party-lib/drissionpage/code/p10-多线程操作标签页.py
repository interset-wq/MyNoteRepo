
from DrissionPage import Chromium, ChromiumOptions
from pprint import pprint
import concurrent.futures

# 设置Chromium浏览器选项，使用系统用户路径
co = ChromiumOptions().use_system_user_path()

# 连接浏览器并获取浏览器对象
browser = Chromium(co)

# 获取标签页对象并打开目标网址
tab = browser.new_tab('https://m.sfacg.com/i/742961/')

# css定位到章节列表的无序列表
chapters_css = 'css:.mulu_list'
chapter_dict = {}

# 从网页中提取章节标题和链接
for chapter in tab(chapters_css).eles('tag:a'):
    chapter_dict[chapter.text] = chapter.link

# 打印提取到的章节字典
# pprint(chapter_dict)

def fetch_and_save_chapter(chapter_title, chapter_url):
    
    new_tab = browser.new_tab(chapter_url)  # 打开章节链接
    chapter_content = new_tab('css:div div').text  # 获取章节内容
    # print(chapter_content)

    print(f"正在下载小说 {chapter_title}")
    tab.wait(1)
    new_tab.close()
    
    # 将章节内容写入文件
    with open(f'./小说_{chapter_title}.txt', 'w', encoding='utf-8') as file:
        file.write(chapter_content)


#- 单线程
def single_thread():
    for title, url in chapter_dict.items():
        fetch_and_save_chapter(title, url)

#- 多线程
def mul_thread():
    # 创建一个线程池，最多允许 4 个线程同时运行
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # 提交多个任务到线程池
        for title, url in chapter_dict.items():
            executor.submit(fetch_and_save_chapter, title, url) 
  
    
if __name__ == "__main__":
    # single_thread()
    mul_thread()