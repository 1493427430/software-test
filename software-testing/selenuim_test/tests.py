import os
import sys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.action_chains import ActionChains
class LikeShopTest():
    def __init__(self) -> None:

        driver_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(sys.executable)))),
                               'geckodriver.exe')
        service = FirefoxService(executable_path=driver_path)
        options = webdriver.FirefoxOptions()
        self.browser = webdriver.Firefox(service=service, options=options)

    def tset_1(self):
        self.browser.get('http://likeshop.abc/admin/account/login.html')
        sleep(2)
        
        # 输入用户名
        self.browser.find_element(By.NAME, 'account').send_keys('admin')
        
        # 输入密码
        self.browser.find_element(By.NAME, 'password').send_keys('admin')
        
        # 输入验证码
        self.browser.find_element(By.NAME, 'code').send_keys('111111')
        
        # 点击登录
        self.browser.find_element(By.ID, 'login').click()
        sleep(3)
        
        # 点击商品
        self.browser.find_element(By.XPATH, '//*[@id="LAY-system-side-menu"]/li[1]/a').click()
        sleep(2)
        # 定位子框架
        iframe1 = self.browser.find_element(By.XPATH, '//*[@id="LAY_app_body"]/div[2]/iframe')
        self.browser.switch_to.frame(iframe1)
        
        self.browser.find_element(By.XPATH, '//*[@id="keyword"]').send_keys('文具')
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[1]/div/div[5]/button[1]').click()
        
        # 接收列表
        tr_list = self.browser.find_elements(By.XPATH, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr')
        # 接收条数
        tr_count = len(tr_list)
        if tr_count == 0:
            print('没有数据')
        is_not_bug = True
        for i in tr_list:
            shop_name = i.find_element(By.XPATH, './td[2]/div').text
            if '文具' not in shop_name:
                is_not_bug = False
        if is_not_bug:
            print('商品列表查询没有问题')
        else:
            print('商品列表有问题')
        sleep(2)
        
if __name__ == '__main__':
    likeShopTest = LikeShopTest()
    likeShopTest.tset_1()