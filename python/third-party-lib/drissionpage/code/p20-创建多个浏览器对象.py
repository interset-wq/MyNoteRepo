"""创建多个浏览器对象
通过指定端口可以创建多个浏览器对象"""


from DrissionPage import Chromium
from concurrent.futures import ThreadPoolExecutor, as_completed

"""手动创建多个浏览器对象"""

# browser1 = Chromium(9222)
# browser2 = Chromium(9333)
# browser3 = Chromium(9444)

# browser1.new_tab('chrome://version')
# 在chrome://version中可以看到浏览器使用的端口
# 命令行	"C:/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port=9222 --no-first-run --disable-popup-blocking --no-default-browser-check --hide-crash-restore-bubble --user-data-dir="C:\Users\86183\AppData\Local\Temp\DrissionPage\userData\9222" --disable-infobars --disable-features=PrivacySandboxSettings4 --disable-suggestions-ui --flag-switches-begin --flag-switches-end
# browser2.new_tab('chrome://version')
# browser2.new_tab('chrome://version')

"""通过线程池创建多个浏览器对象"""
START_PORT = 9222
BROWSER_COUNT = 10
MAX_THREADS = 5

def launch_browser(port: int):
    browser = Chromium(port)
    browser.latest_tab.get('chrome://version')
    return browser

def main():
    browsers = []
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(launch_browser, START_PORT + i) for i in range(BROWSER_COUNT)]
        for future in futures:
            try:
                browser = future.result()
                browsers.append(browser)
            except Exception as e:
                print(f'启动浏览器失败：{e}')
            
if __name__ == '__main__':
    main()