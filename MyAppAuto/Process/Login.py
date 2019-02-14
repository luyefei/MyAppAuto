"""
@author: luyefei
@file:Login.py
@time:2019/1/23
"""
from MyAppAuto.public.StartAppiumServer import AppiumServer
from MyAppAuto.public.basicOperate import Swipe
from MyAppAuto.public.androidDriver import AndroidDriver
import time
from MyAppAuto.public.log import Log


class Login(object):

    def __init__(self):
        self.driver = AndroidDriver()
        self.server = AppiumServer()
        self.log = Log()

    def login(self):
        self.server.start_appiums()
        driver = self.driver.driver()
        i = 0
        while i < 3:
            Swipe(driver).swipe_left()
            i += 1
        # 进入首页
        driver.find_element_by_id("io.manong.developerdaily:id/btn_primary").click()
        # 点击登录/注册
        driver.find_element_by_id("io.manong.developerdaily:id/login_btn").click()
        driver.implicitly_wait(30)
        # 点击密码登录
        driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "密码登录")]').click()
        time.sleep(3)
        driver.find_element_by_id("io.manong.developerdaily:id/edt_phone").clear()
        driver.find_element_by_id("io.manong.developerdaily:id/edt_phone").send_keys('15821028996')
        driver.find_element_by_id("io.manong.developerdaily:id/edt_password").clear()
        driver.find_element_by_id("io.manong.developerdaily:id/edt_password").send_keys('123456')
        driver.find_element_by_id("io.manong.developerdaily:id/btn_login").click()
        title = driver.find_element_by_id("io.manong.developerdaily:id/toolbar_title").text
        try:
            assert title == '我的'
            self.log.info('登录成功，进入我的页面')
        except Exception as e:
            self.log.error(e)
        self.server.stop_appium()


if __name__ == '__main__':
    r = Login()
    r.login()
