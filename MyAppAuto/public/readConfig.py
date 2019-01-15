"""
@author: luyefei
@file:readConfig.py
@time:2019/1/15
"""
import configparser


class Readconfig(object):
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read("..\Config\config.ini")

    def getConfigValue(self, name):
        value = self.conf.get('config', name)
        return value

    def getcmdValue(self, name):
        value = self.conf.get('cmd', name)
        return value

    def getemailValue(self, name):
        value = self.conf.get('email', name)
        return value


if __name__ == '__main__':
    r = Readconfig()
    s = r.getConfigValue("platformName")
    print(s)
