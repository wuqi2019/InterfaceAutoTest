# _*_ coding:utf-8 _*_
__author__ = 'fanxun'
__data__ = "2021-05-10 15:47"

import os, time
import logging
from logging.handlers import TimedRotatingFileHandler
from config import BaseConfig

# 日志级别
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

LOG_PATH = BaseConfig.log_path

class LogHandler(logging.Logger):
    """
    日志处理
    """
    def __init__(self, name, level=DEBUG, stream=True, file=True):
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=level)
        self.__determine_folder()
        if stream:
            self.__setStreamHandler__()
        if file:
            self.__setFileHandler__()

    def __determine_folder(self):
        """判断日志路径是否存在"""
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)

    def __setFileHandler__(self, level=None):
        """
        输出到文件
        """
        file_name = os.path.join(LOG_PATH, f'{self.name}{time.strftime(r"%Y%m%d%H%M%S", time.localtime())}.log')
        # 设置日志回滚, 保存在log目录, 一天保存一个文件, 保留7天
        file_handler = TimedRotatingFileHandler(filename=file_name, when='D', interval=1, backupCount=7)
        file_handler.suffix = '%Y%m%d.log'
        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

        file_handler.setFormatter(formatter)
        self.file_handler = file_handler
        self.addHandler(file_handler)

    def __setStreamHandler__(self, level=None):
        """
        输出到控制台
        """
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        stream_handler.setFormatter(formatter)
        if not level:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(level)
        self.addHandler(stream_handler)

    def resetName(self, name):
        self.name = name
        self.removeHandler(self.file_handler)
        self.__setFileHandler__()


logger = LogHandler('log')


if __name__ == '__main__':
    log = LogHandler('test')
    log.info('this is a test msg')
    log.error('hoo')









































