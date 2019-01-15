"""
@author: luyefei
@file:StartAppiumServer.py
@time:2019/1/14
"""
import platform
from subprocess import Popen
from MyAppAuto.public import log
import time


class AppiumServer(object):

    @staticmethod
    def os_platform():
        """
        系统平台
        :return:
        """
        sys_platform = platform.system()
        return sys_platform

    def start_appiums(self):
        if self.os_platform() == 'Windows':
            Popen(
                "appium -a localhost -p 4723 --session-override", shell=True)
            log.Log().info('系统平台Windows,appium服务启动，ip:localhost,port:4723')
            time.sleep(5)
        else:
            log.Log().error('无法获取系统版本，程序退出')
            quit()

    def stop_appium(self):
        if self.os_platform() == 'Windows':
            cmd = 'taskkill /F /IM node.exe'
            Popen(cmd)
            log.Log().info('系统平台Windows,appium服务关闭')
            time.sleep(5)
        else:
            log.Log().error('无法获取系统版本，程序退出')
            quit()


if __name__ == '__main__':
    s = AppiumServer()
    s.start_appiums()
