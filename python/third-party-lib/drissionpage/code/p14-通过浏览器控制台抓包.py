"""通过浏览器控制台使用js代码抓包"""


from DrissionPage import Chromium,ChromiumOptions
from  loguru import logger

options=ChromiumOptions()

# 连接浏览器并获取浏览器对象
browser = Chromium(options)  

# 获取标签页对象并打开网址
tab = browser.new_tab('https://spa1.scrape.center/')


tab.console.start()

# 一条日志信息
# logger.info(tab.console.wait().text)

js_code='''
console.log(window.location.href);
'''

tab.run_js(js_code)

logger.info(tab.console.wait().text)


# 所有日志信息
for data  in  tab.console.messages:
    logger.info(data.text)


fetch_code=r'''fetch("https://spa1.scrape.center/api/movie/?limit=10&offset=0", {
  "referrer": "https://spa1.scrape.center/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET",
  "mode": "cors",
  "credentials": "omit"
});
'''

#立即调用的箭头函数形式
response_code='''
(async ()=>{
    var res = await fetch_code

    let data = await res.text();
    console.log(data);
})()
'''.replace('fetch_code',fetch_code)

tab.run_js(response_code)

tab.wait(3)
logger.info(tab.console.wait().text)
