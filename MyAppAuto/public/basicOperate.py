"""
@author: luyefei
@file:basicOperate.py
@time:2019/1/15
"""


class Swipe(object):
    def __init__(self, driver):
        self.driver = driver

    def getsize(self):  # 获取屏幕的大小
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向上滑动(x值不变，y由大变小)
    def swipe_up(self, t=1000):
        l = self.getsize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.3)
        return self.driver.swipe(x1, y1, x1, y2, t)

    # 向下滑动（x值不变，y值由小变大）
    def swipe_down(self, t=1000):
        l = self.getsize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.8)
        return self.driver.swipe(x1, y1, x1, y2, t)

    # 向左滑动（y值不变，x值由大变小）
    def swipe_left(self, t=1000):
        l = self.getsize()
        y = int(l[1] * 0.5)
        x1 = int(l[0] * 0.8)
        x2 = int(l[0] * 0.1)
        return self.driver.swipe(x1, y, x2, y, t)

    # 向右滑动（y值不变，x值由小变大）
    def swipe_right(self, t=1000):
        l = self.getsize()
        y = int(l[1] * 0.5)
        x1 = int(l[0] * 0.2)
        x2 = int(l[0] * 0.8)
        return self.driver.swipe(x1, y, x2, y, t)


class Assert(object):

    def __init__(self, driver):
        self.driver = driver

    def Assert(self):
        pass
