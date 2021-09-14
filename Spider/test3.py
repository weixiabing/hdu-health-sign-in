from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
# 导入时间模块
import time
import os
# 填写获取到的token
TOKEN=os.environ['TOKEN']
js='window.sessionStorage.setItem("hduhelp_ncov_dailysign_token","3c07ebb9-7e9f-43d0-a801-c52f323df240")'
# 省 市 区 从上往下数第几个 如第1个,第2个 7 9 4表示浙江省杭州市江干区
province=7
city=9
area=4
# 获取驱动路径
DRIVER_PATH = '/usr/bin/chromedriver'
# 浏览器设置
options = Options()
options.add_argument('--no-sandbox')
# 无头参数
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 11; Redmi K30 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045811 Mobile Safari/537.36 MMWEBID/8641 MicroMessenger/8.0.11.1980(0x28000B51) Process/tools WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64')
# 启动浏览器
browser = Chrome(executable_path=DRIVER_PATH, options=options)
# 访问url
browser.get("https://healthcheckin.hduhelp.com/")
#窗口最大化
browser.maximize_window()
# 添加token
browser.execute_script(js)
# 刷新浏览器
browser.refresh()
# 间隔时间太短会导致打卡失败 因为界面元素还没有加载出来
time.sleep(2)
