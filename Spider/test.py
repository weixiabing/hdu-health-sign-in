from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
# 导入时间模块
import time
import os
# 填写获取到的token
TOKEN=os.environ['TOKEN']
js='window.localStorage.setItem("hduhelp_ncov_dailysign_token",'fc53cc9f-d43b-4fa9-9386-ef165fe020e9')'
# 省 市 区 从上往下数第几个 如第1个,第2个 7 9 4表示浙江省杭州市江干区
province=7
city=9
area=4
# 获取驱动路径
DRIVER_PATH = './chromedriver'
# 浏览器设置
options = Options()
options.add_argument('--no-sandbox')
# 无头参数
options.add_argument('--headless')
options.add_argument('--disable-gpu')
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
# 点击 确认打卡 按钮
browser.find_element_by_css_selector('.van-button.van-button--info.van-button--normal').click()
time.sleep(1)
# 点击弹出的 确认 按钮 因为之后才能填写位置信息
browser.find_element_by_class_name('van-dialog__confirm').click()
time.sleep(1)
# 点击 确认 手动填写位置按钮
browser.find_element_by_class_name('van-field__control--right').click()
time.sleep(1)
# 获取滑动选择框
pickers=browser.find_elements_by_class_name('van-picker-column__wrapper')
for i in range(province):
    # 依次点击 直到选择了对应城市
    pickers[0].find_elements_by_class_name('van-picker-column__item')[i].click()
for i in range(city):
    # 同上
    pickers[1].find_elements_by_class_name('van-picker-column__item')[i].click()
for i in range(area):
    # 同上
    pickers[2].find_elements_by_class_name('van-picker-column__item')[i].click()
# 点击 确认 地区选择按钮
browser.find_element_by_class_name('van-picker__confirm').click()
time.sleep(1)
# 点击 确认打卡 按钮
browser.find_element_by_css_selector('.van-button.van-button--info.van-button--normal').click()
time.sleep(1)
# 点击 确认负责 按钮
browser.find_element_by_css_selector('.van-button.van-button--default.van-button--large.van-dialog__confirm.van'
                                     '-hairline--left') .click()
time.sleep(1)
#退出窗口
browser.quit()
print('打卡成功')
