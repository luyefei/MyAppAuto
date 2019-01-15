"""
@author: luyefei
@file:driver.py
@time:2019/1/15
"""
import time
from appium import webdriver
from MyAppAuto.public import log
from MyAppAuto.public import StartAppiumServer


class AndroidDriver(object):

    def __init__(self):
        self.desired_caps = {'platformName': "Android",  # 设备系统
                             'platformVersion': 8,  # 设备系统的版本
                             'deviceName': "8GP4C18705002188",  # 设备的uuid
                             'appPackage': "io.manong.developerdaily",  # app的包名
                             'appActivity': "io.toutiao.android.ui.activity.LaunchActivity",  # 测试appActivity
                             'noReset': True}  # 控制启动app时，是否初始化设置
        self.log = log.Log()

    def driver(self):
        try:
            driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
            time.sleep(5)
            self.log.info('启动driver成功')
            return driver
        except Exception as e:
            self.log.error(e)


if __name__ == '__main__':
    r = StartAppiumServer.AppiumServer()
    r.start_appiums()
    s = AndroidDriver()
    s.driver()
    r.stop_appium()
