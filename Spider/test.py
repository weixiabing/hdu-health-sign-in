from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import sys
DRIVER_PATH = '/chrome/chromedriver'

options = Options()
options.add_argument('--no-sandbox')
    #options.add_argument('--headless')  # 无头参数
    #options.add_argument('--disable-gpu')
    #换成微信浏览器ua
options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 11; Redmi K30 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045811 Mobile Safari/537.36 MMWEBID/8641 MicroMessenger/8.0.11.1980(0x28000B51) Process/tools WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64')
def main(username,password):
    # 设置浏览器
  
    
   
    # 启动浏览器
    driver = Chrome(executable_path=DRIVER_PATH, options=options)
    # 访问目标URL
    driver.get('https://api.hduhelp.com/login/direct/yiban?clientID=healthcheckin&redirect=https%3A%2F%2Fhealthcheckin.hduhelp.com%2F%23%2Fauth')
    print(driver.page_source)
    
    # 省 市 区 从上往下数第几个 如第1个,第2个 7 9 4表示浙江省杭州市江干区
    province=7
    city=9
    area=4
    
    time.sleep(2)
    #登录确认
    driver.find_element_by_id('oauth_uname_w').send_keys(username)
    driver.find_element_by_id('oauth_upwd_w').send_keys(password)
    time.sleep(2)
    driver.find_element_by_css_selector('.oauth_check_login').click()
    
    #driver.find_element_by_id('btnOk').click()
    time.sleep(2)
    #重新定位
    driver.find_element_by_css_selector('.van-tag.van-tag--warning').click()
    time.sleep(2)
    #再次点击
    driver.find_element_by_css_selector('.van-cell.van-cell--clickable.van-cell--required.van-field').click()
    time.sleep(2)
    #获取区域列表
    pickers=driver.find_elements_by_css_selector('.van-picker-column')
    
    for i in range(province):
    # 依次点击 直到选择了对应城市
        pickers[0].find_elements_by_class_name('van-picker-column__item')[i].click()
    for i in range(city):
    # 同上
        pickers[1].find_elements_by_class_name('van-picker-column__item')[i].click()
    for i in range(area):
    # 同上
        pickers[2].find_elements_by_class_name('van-picker-column__item')[i].click()
    
    #区域确认
    driver.find_element_by_css_selector('.van-picker__confirm').click()
    #获取问题8列表
    pickers1=driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[3]/div[4]/div[8]')
    #点击
    pickers1[0].find_elements_by_css_selector('.van-radio')[3].click()
    

    #立即打卡
    driver.find_element_by_css_selector('.van-button.van-button--info.van-button--normal').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.van-button.van-button--default.van-button--large.van-dialog__confirm.van-hairline--left').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.van-button.van-button--default.van-button--large.van-dialog__cancel').click()
    driver.save_screenshot("0001.png")  # 截图
    driver.close()
    driver.quit() 
if __name__ == "__main__":
    print(sys.argv)
    username = sys.argv[1]
    password = sys.argv[2]
    try:
        main(username, password)
    except Exception:
        exit(1)