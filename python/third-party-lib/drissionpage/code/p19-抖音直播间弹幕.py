"""获取抖音直播间弹幕"""


from DrissionPage import Chromium,ChromiumOptions
from  loguru import logger

# 配置日志输出到文件
logger.add('弹幕1.txt',rotation='100 MB',encoding='utf-8')




# 连接浏览器并获取浏览器对象
browser = Chromium(5678)  
url='https://live.douyin.com/200852386071'

# 获取标签页对象并打开网址
tab = browser.new_tab(url)

# 开始监听控制台输出
tab.console.start()

logger.warning(f'开始监听记录{tab.url}的弹幕')


# 等待弹幕标签加载完成
tab.wait.eles_loaded('.webcast-chatroom___list')
tab.wait(2)


observer_code=r'''
// 选择要监控的目标节点
const targetNode = document.querySelector('.webcast-chatroom___list');

// 创建一个配置对象，指定要观察的变化类型
const config = { childList: true, subtree: true };

// 创建一个回调函数，当目标节点发生变化时执行
const callback = (mutationsList) => {
    for (const mutation of mutationsList) {
        if (mutation.type === 'childList') {
            mutation.addedNodes.forEach(node => {
                // 检查新增的节点是否是 div 元素
                if (node.nodeType === Node.ELEMENT_NODE && node.tagName === 'DIV') {
                    const currentTime = new Date().toLocaleTimeString(); // 获取当前时间
                    console.log(currentTime,node.innerText);   // 打印当前时间和新增 div 的 innerText
                }
            });
        }
    }
};

// 创建一个 MutationObserver 实例
const observer = new MutationObserver(callback);

// 开始观察目标节点
observer.observe(targetNode, config);
'''

tab.run_js(observer_code)


while True:
    # 打印控制台的输出
    logger.info(tab.console.wait().text)




input('请按回车键继续')