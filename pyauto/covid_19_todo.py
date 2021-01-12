"""
Created by J.
2020-8-28
代码简单，请自行修改四处中文的代码
有问题请自行修改代码或者反馈
由于我的不是最新版，请自行安装python和selenium
pip install selenium
由于浏览器不同，请自行下载driver并设置路径
Chrome: http://chromedriver.storage.googleapis.com/index.html
Edge: https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/
"""

import time

try:
    from selenium import webdriver
except ImportError:
    print('请自行安装selenium后重试')
    exit()

chrome_location = r"浏览器的路径"  

driver_path = r'driver的路径'  

options = webdriver.ChromeOptions()

options.binary_location = chrome_location


def auto_sign(accounts: list, pwds: list):
    """自动健康打卡"""
    
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.get('https://weixine.ustc.edu.cn/2020/login')

    for i in range(0, len(accounts)):
        login_btn = driver.find_element_by_xpath('//*[@id="user-login"]/div/div[3]/div[2]/a')
        
        login_btn.click()
        
        username = driver.find_element_by_xpath('//*[@id="username"]')
        pwd = driver.find_element_by_xpath('//*[@id="password"]')
        login_ok = driver.find_element_by_xpath('//*[@id="login"]')
        username.send_keys(accounts[i])
        pwd.send_keys(pwds[i])
        login_ok.click()
        driver.implicitly_wait(3)
        try:
            j = 0
            while j < 4:  
                time.sleep(2)
                submit = driver.find_element_by_xpath('//*[@id="report-submit-btn"]')
                submit.click()
                j += 1
        except Exception as e:
            print(e)
        
        exit_btn = driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/ul[2]/li/a')
        exit_btn.click()

    driver.quit()


def run():
    auto_sign(['账号列表'], ['密码列表'])


if __name__ == '__main__':
    run()
