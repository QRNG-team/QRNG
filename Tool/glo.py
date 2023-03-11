# -*- coding: utf-8 -*-
import sys
class Logger(object):
    def __init__(self, filename="Detection.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")
        # 可以选择"w"
        self.log = open(filename, "a", encoding="utf-8")  # 防止编码错误

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

    def reset(self):
        self.log.close()
        sys.stdout = self.terminal

def _init():#初始化
    global _global_dict
    _global_dict = {}
def set_value(key,value):
    """ 定义一个全局变量 """
    _global_dict[key] = value
def get_value(key,defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return _global_dict[key]
    except KeyError:
        return defValue
