# -*- coding: utf-8 -*-
import time
from PyQt5.QtCore import QThread, pyqtSignal
from extractor.mainextractor import Extractor

# 定义一个线程类
class Extract_Thread(QThread):
    # 自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal(str)

    # 带一个参数t
    def __init__(self, para, parent=None):
        super(Extract_Thread, self).__init__(parent)
        self.para = para

    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        ex = Extractor(self.para)
        ex.extract()
        # 发射自定义信号
        # 通过emit函数将参数i传递给主线程，触发自定义信号
        self.finishSignal.emit("yes")  # 注意这里与_signal = pyqtSignal(str)中的类型相同




# 定义一个线程类
class Detection_Thread(QThread):
    # 自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal(str)

    # 带一个参数t
    def __init__(self, para, parent=None):
        super(Detection_Thread, self).__init__(parent)
        self.para = para

    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        ex = Extractor(self.para)

        ex.detection()
        # 发射自定义信号
        # 通过emit函数将参数i传递给主线程，触发自定义信号
        self.finishSignal.emit("yes")  # 注意这里与_signal = pyqtSignal(str)中的类型相同

