import os
import sys
from datetime import datetime
import uuid
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.action_chains import ActionChains


class LikeShopTest():
    def __init__(self) -> None:

        self.browser = webdriver.Chrome()
    def shop_list(self):
        '''
        商品列表查询测试
        '''

        # 点击商品
        self.browser.find_element(By.XPATH, '//*[@id="LAY-system-side-menu"]/li[1]/a').click()
        sleep(4)

        # 定位frame子框架
        iframe1 = self.browser.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/iframe')
        # 进入子框架
        self.browser.switch_to.frame(iframe1)

        # 定位商品名称输入框并输入商品名称
        self.browser.find_element(By.XPATH, '//*[@id="keyword"]').send_keys('文具')

        # 定位查询按钮并点击查询
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[1]/div/div[5]/button[1]').click()

        sleep(1)

        # 获取列表
        tr_list = self.browser.find_elements(By.XPATH,
                                             '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr')

        if len(tr_list) == 0:
            print('没有数据')

        is_not_bug = True
        for item in tr_list:
            shop_name = item.find_element(By.XPATH, './td[2]/div').text
            if '文具' not in shop_name:
                is_not_bug = False
        if is_not_bug:
            print('没有问题')
        else:
            print('有bug')

    def login(self):
        '''
        测试登录
        '''
        self.browser.get('http://likeshop.abc/admin/account/login.html')
        self.browser.maximize_window()
        sleep(2)

        # 定位用户名输入框并输入用户名
        self.browser.find_element(By.NAME, 'account').send_keys('admin')

        # 定位密码输入框并输入密码
        self.browser.find_element(By.NAME, 'password').send_keys('admin')

        # 定位验证码输入框并输入密码
        self.browser.find_element(By.NAME, 'code').send_keys('1111')

        # 定位登录按钮并点击登录按钮
        self.browser.find_element(By.ID, 'login').click()
        sleep(3)

    def shop_add(self):
        '''
        商品新增测试
        '''
        # 点击商品
        self.browser.find_element(By.XPATH, '//*[@id="LAY-system-side-menu"]/li[1]/a').click()
        sleep(4)

        # 定位frame子框架
        iframe1 = self.browser.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/iframe')
        # 进入子框架
        self.browser.switch_to.frame(iframe1)

        # 定位商品发布按钮并点击
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[2]/div[1]/button[1]').click()

        # 定位商品发布子框架
        shop_add_iframe = self.browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/iframe')
        # 进入商品发布子框架
        self.browser.switch_to.frame(shop_add_iframe)
        uid=str(uuid.uuid4())
        # 定位商品名称输入框并输入数据
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[1]/div/input[2]').send_keys(
            '测试商品'+uid)

        # 定位第一个大类的选择框并点击
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[1]/div/div/input').click()
        sleep(2)
        # 定位第一个大类的下拉数据并点击第一个
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[1]/div/dl/dd[2]').click()
        sleep(2)
        # 定位第二个类的选择框并点击
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[2]/div/div/input').click()
        sleep(2)
        # 定位第二个类的下拉数据并点击第一个
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[2]/div/dl/dd[2]').click()
        sleep(2)
        # 定位第三个类的选择框并点击
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[3]/div/div/input').click()
        sleep(2)
        # 定位第三个类的下拉数据并点击第一个
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[3]/div/dl/dd[2]').click()
        sleep(2)

        # 定位商品主图 图片上传按钮并点击
        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[5]/div/div[2]/a').click()
        sleep(3)

        # 定位图片上传子框架
        upload_img_iframe_1 = self.browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/iframe')

        # 进入图片上传子框架
        self.browser.switch_to.frame(upload_img_iframe_1)

        self.upload_img("C:\\Users\\Administrator\\Desktop\\照片\\微信图片_20240912153734.jpg")

        # 先回到主框架
        self.browser.switch_to.default_content()
        # 进入商品子框架
        self.browser.switch_to.frame(iframe1)
        # 进入商品发布子框架
        self.browser.switch_to.frame(shop_add_iframe)

        # 定位商品轮播图 图片上传按钮并点击
        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[6]/div/div/a').click()
        sleep(2)
        # 定位图片上传子框架
        upload_img_iframe_2 = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[2]/iframe')

        # 进入图片上传子框架
        self.browser.switch_to.frame(upload_img_iframe_2)
        self.upload_img('C:\\Users\\Administrator\\Desktop\\照片\\微信图片_20240912153734.jpg')
        sleep(2)

        # 先回到主框架
        self.browser.switch_to.default_content()
        # 进入商品子框架
        self.browser.switch_to.frame(iframe1)
        # 进入商品发布子框架
        self.browser.switch_to.frame(shop_add_iframe)

        # 点击价格库存
        self.browser.find_element(By.XPATH, '/html/body/div[1]/ul/li[2]').click()
        sleep(2)

        # 填写价格、成本价、库存信息
        self.browser.find_element(By.XPATH, '//*[@id="one-spec-lists-table"]/tbody/tr/td[2]/input').send_keys('1')
        self.browser.find_element(By.XPATH, '//*[@id="one-spec-lists-table"]/tbody/tr/td[3]/input').send_keys('1')
        self.browser.find_element(By.XPATH, '//*[@id="one-spec-lists-table"]/tbody/tr/td[4]/input').send_keys('1')
        self.browser.find_element(By.XPATH, '//*[@id="one-spec-lists-table"]/tbody/tr/td[5]/input').send_keys('100')

        # 回到商品子框架点击保存按钮
        # 先回到主框架
        self.browser.switch_to.default_content()
        # 进入商品子框架
        self.browser.switch_to.frame(iframe1)

        self.browser.find_element(By.LINK_TEXT, '保存').click()

    def upload_img(self, file_path):
        # 上传图片
        self.browser.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)
        sleep(5)
        # 选择第一张图片
        self.browser.find_element(By.XPATH, '//*[@id="lists"]/li[1]/div/img').click()
        # 点击选中图片按钮
        self.browser.find_element(By.XPATH, '//*[@id="used"]').click()
        sleep(2)

    def shop_sj(self):
        self.browser.switch_to.default_content()
        # 点击商品
        self.browser.find_element(By.XPATH,"//a[@lay-tips='商品']").click()
        sleep(2)
        shop_add_iframe = self.browser.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/iframe')
        # 进入商品发布子框架
        self.browser.switch_to.frame(shop_add_iframe)
        sleep(2)
        # 点击商品标签
        self.browser.find_element(By.XPATH,"//li[contains(text(),'仓库中商品(1)')]").click()
        sleep(2)
        shop_list=self.browser.find_elements(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr")
        if len(shop_list)>0:
            self.browser.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/table/tbody/tr[1]")
            self.browser.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/table/tbody/tr/td/div/a[2]").click()
            self.browser.find_element(By.CLASS_NAME,
                                  "layui-layer-btn0").click()
    def logout(self):
        sleep(10)
        button=self.browser.find_element(By.XPATH, "(//cite[contains(text(),'admin（系统管理员）')])[1]")
        sleep(2)
        ActionChains(self.browser).move_to_element(button).perform()
        sleep(2)
        self.browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/ul[2]/li[3]/dl/dd[2]/a").click()
        sleep(8)

    def shop_edit(self):
        self.browser.switch_to.default_content()
        # 点击商品
        self.browser.find_element(By.XPATH, '//*[@id="LAY-system-side-menu"]/li[1]/a').click()
        sleep(4)

        # 定位frame子框架
        iframe1 = self.browser.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/iframe')
        # 进入子框架
        self.browser.switch_to.frame(iframe1)

        # 定位商品编辑按钮并点击
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/table/tbody/tr/td/div/a[1]').click()

        # 定位商品发布子框架
        shop_add_iframe = self.browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/iframe')
        # 进入商品发布子框架
        self.browser.switch_to.frame(shop_add_iframe)

        # 定位商品名称输入框并输入数据
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[1]/div/input[2]').clear()

        uid = str(uuid.uuid4())
        # 定位商品名称输入框并输入数据
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[1]/div/input[2]').send_keys(
            '测试商品' + uid)

        # 定位第一个大类的选择框并点击
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[1]/div/div/input').click()
        sleep(2)
        # 定位第一个大类的下拉数据并点击第一个
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[1]/div/dl/dd[2]').click()
        sleep(2)
        # 定位第二个类的选择框并点击
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[2]/div/div/input').click()
        sleep(2)
        # 定位第二个类的下拉数据并点击第一个
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[2]/div/dl/dd[2]').click()
        sleep(2)
        # 定位第三个类的选择框并点击
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[3]/div/div/input').click()
        sleep(2)
        # 定位第三个类的下拉数据并点击第一个
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div[3]/div/dl/dd[2]').click()
        sleep(2)

# a链接为display：none隐藏元素，需要执行脚本修改样式
        js = "document.querySelector('.goods-img-del-x.goods-image-del').style.display='block'"
        self.browser.execute_script(js)
#执行删除图片重新上传操作
        self.browser.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[5]/div/div[1]/a").click()
        sleep(2)
        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[5]/div/div[2]/a').click()
        sleep(8)
        # 定位图片上传子框架
        upload_img_iframe_1 = self.browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/iframe')

        # 进入图片上传子框架
        self.browser.switch_to.frame(upload_img_iframe_1)

        self.upload_img("C:\\Users\\Administrator\\Desktop\\照片\\微信图片_20240912153734.jpg")

        # 先回到主框架
        self.browser.switch_to.default_content()
        # 进入商品子框架
        self.browser.switch_to.frame(iframe1)
        # 进入商品发布子框架
        self.browser.switch_to.frame(shop_add_iframe)

        # 定位商品轮播图 图片上传按钮并点击
        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[6]/div/div/a').click()
        sleep(2)
        # 定位图片上传子框架
        upload_img_iframe_2 = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[2]/iframe')

        # 进入图片上传子框架
        self.browser.switch_to.frame(upload_img_iframe_2)
        self.upload_img('C:\\Users\\Administrator\\Desktop\\照片\\微信图片_20240912153734.jpg')
        sleep(2)

        # 先回到主框架
        self.browser.switch_to.default_content()
        # 进入商品子框架
        self.browser.switch_to.frame(iframe1)
        # 进入商品发布子框架
        self.browser.switch_to.frame(shop_add_iframe)

        # 点击价格库存
        self.browser.find_element(By.XPATH, '/html/body/div[1]/ul/li[2]').click()
        sleep(2)

        # 填写价格、成本价、库存信息
        self.browser.find_element(By.XPATH, '//*[@id="one-spec-lists-table"]/tbody/tr/td[2]/input').send_keys('1')
        self.browser.find_element(By.XPATH, '//*[@id="one-spec-lists-table"]/tbody/tr/td[3]/input').send_keys('1')
        self.browser.find_element(By.XPATH, '//*[@id="one-spec-lists-table"]/tbody/tr/td[4]/input').send_keys('1')
        self.browser.find_element(By.XPATH, '//*[@id="one-spec-lists-table"]/tbody/tr/td[5]/input').send_keys('100')

        # 回到商品子框架点击保存按钮
        # 先回到主框架
        self.browser.switch_to.default_content()
        # 进入商品子框架
        self.browser.switch_to.frame(iframe1)

        self.browser.find_element(By.LINK_TEXT, '保存').click()



if __name__ == '__main__':
    likeShopTest = LikeShopTest()
    likeShopTest.login()
    likeShopTest.shop_add()
    likeShopTest.shop_sj()
    likeShopTest.shop_edit()
    likeShopTest.logout()
    sleep(9)
    # likeShopTest.test_shop_list()

