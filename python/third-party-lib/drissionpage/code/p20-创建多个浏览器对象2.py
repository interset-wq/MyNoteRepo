"""创建多个浏览器对象
通过指定端口可以创建多个浏览器对象"""


from DrissionPage import Chromium, ChromiumOptions
from concurrent.futures import ThreadPoolExecutor, as_completed

"""通过线程池创建多个浏览器对象
使用自动端口"""

BROWSER_COUNT = 10
MAX_THREADS = 5

def launch_browser():
    co = ChromiumOptions().auto_port()
    browser = Chromium(co)
    browser.latest_tab.get('chrome://version')
    return browser

def main():
    browsers = []
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(launch_browser) for _ in range(BROWSER_COUNT)]
        for future in futures:
            try:
                browser = future.result()
                browsers.append(browser)
            except Exception as e:
                print(f'启动浏览器失败：{e}')
            
if __name__ == '__main__':
    main()