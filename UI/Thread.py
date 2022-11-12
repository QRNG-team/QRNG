# -*- coding: utf-8 -*-
import time
from PyQt5.QtCore import QThread, pyqtSignal
from extractor.mainextractor import Extractor


# 定义一个线程类
class Extract_Thread(QThread):
    # 自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal(list)

    # 带一个参数t
    def __init__(self, para, parent=None):
        super(Extract_Thread, self).__init__(parent)
        self.para = para

    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        ex = Extractor(self.para)
        exresult = ex.extract()
        exresult.append(f"提取结果已保存到{self.para['fewname']}/{self.para['filename']}")
        # 发射自定义信号
        # 通过emit函数将参数i传递给主线程，触发自定义信号
        self.finishSignal.emit(
             exresult)  # 注意这里与_signal = pyqtSignal(str)中的类型相同


# 定义一个线程类
class Detection_Thread(QThread):
    # 自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal(list)

    # 带一个参数t
    def __init__(self, para, parent=None):
        super(Detection_Thread, self).__init__(parent)
        self.para = para

    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        ex = Extractor(self.para)

        detectresult,testtime = ex.detection()
        detectresult.append(testtime,f"检测结果已保存到{self.para['fdwname']}/{self.para['filename']}")
        # 发射自定义信号
        # 通过emit函数将参数i传递给主线程，触发自定义信号
        self.finishSignal.emit(
            detectresult)  # 注意这里与_signal = pyqtSignal(str)中的类型相同


# Runthread子线程
class Runthread(QThread):
    progressBarValue = pyqtSignal(int)  # 更新进度条
    signal_done = pyqtSignal(int)  # 是否结束信号

    def __init__(self):
        super(Runthread, self).__init__()

    def run(self):
        length = 14
        for start in range(0, length, 10):
            self.progressBarValue.emit(int(start / length * 100))  # 发送进度条的值信号
        self.signal_done.emit(1)  # 发送结束信号

    def ExeMessageDialog(self):
        msg_box = QMessageBox(QMessageBox.Information, '通知', '提取已结束')
        self.pb.setValue(100)  # 如果爬取成功
        msg_box.exec_()

    def detectMessageDialog(self):
        msg_box = QMessageBox(QMessageBox.Information, '通知', '检测已结束')
        self.pb.setValue(100)  # 如果爬取成功
        msg_box.exec_()
