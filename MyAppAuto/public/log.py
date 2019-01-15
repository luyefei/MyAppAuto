"""
@author: luyefei
@file:logDIr.py
@time:2019/1/14
"""
import os
import logging
import time


class Log(object):

    def __init__(self):
        filename = 'toutiao' + ''.join(time.strftime('%Y%m%d')) + ''.join('.log')  # 设置log名
        self.folder = "..\Logs"
        self.logname = os.path.join(self.folder, filename)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 设置日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s')

    def output(self, level, message):
        """
        :param level: 日志等级
        :param message: 日志需要打印的信息
        :return:
        """

        # send logging output to a disk file
        fh = logging.FileHandler(self.logname, 'a', encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # send logging output to streams
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warn':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 防止重复打印
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)

        fh.close()

    def info(self, message):
        self.output('info', message)

    def debug(self, message):
        self.output('debug', message)

    def warn(self, message):
        self.output('warn', message)

    def error(self, message):
        self.output('error', message)

    def folder_log(self):
        folder = self.folder
        try:
            os.makedirs(folder, exist_ok=False)
        except FileExistsError:
            self.info("日志文件夹已存在，无需创建")


if __name__ == '__main__':
    r = Log()
    r.folder_log()
