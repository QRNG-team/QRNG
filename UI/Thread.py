# -*- coding: utf-8 -*-
import time
from PyQt5.QtCore import QThread, pyqtSignal
from extractor.mainextractor import Extractor
import Tool.glo as glo
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
        exresult.append(f"提取结果已保存到{self.para['fewname']}")
        # 发射自定义信号
        # 通过emit函数将参数i传递给主线程，触发自定义信号
        self.finishSignal.emit(
             exresult)  # 注意这里与_signal = pyqtSignal(str)中的类型相同


# 定义一个线程类
class Detection_Thread(QThread):
    # 自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal(list)
    pb = pyqtSignal(int)
    # 带一个参数t
    def __init__(self, para, parent=None):
        super(Detection_Thread, self).__init__(parent)
        self.para = para


    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):

        ex = Extractor(self.para)
        detectresult,testtime = ex.detection()
        detectresult.append(testtime)
        detectresult.append(f"检测结果已保存到{self.para['fdwname']}")
        # 发射自定义信号
        # 通过emit函数将参数i传递给主线程，触发自定义信号
        self.finishSignal.emit(
            detectresult)  # 注意这里与_signal = pyqtSignal(str)中的类型相同

# Runthread子线程
class Runthread(QThread):
    progressBarValue = pyqtSignal(int)  # 更新进度条
    signal_done = pyqtSignal(int)  # 是否结束信号

    def __init__(self,flag):
        super(Runthread, self).__init__()
        self.flag = flag
    def run(self):
        if self.flag == 1: #负责提取进度条
            while True:
                num1 = glo.get_value('extractbar')
                self.progressBarValue.emit(num1)  # 发送进度条的值信号
                if num1 == 100:
                    break
                time.sleep(0.2)
            self.signal_done.emit(1)  # 发送结束信号
        if self.flag == 2: #负责检测进度条
            while True:
                num2 = glo.get_value('detectbar')
                n = (num2/15)*100
                self.progressBarValue.emit(n)  # 发送进度条的值信号
                if num2 == 15:
                    break
                time.sleep(0.5)
            self.signal_done.emit(1)  # 发送结束信号
    # def ExeMessageDialog(self):
    #     msg_box = QMessageBox(QMessageBox.Information, '通知', '提取已结束')
    #     self.pb.setValue(100)  # 如果爬取成功
    #     msg_box.exec_()
    #
    # def detectMessageDialog(self):
    #     msg_box = QMessageBox(QMessageBox.Information, '通知', '检测已结束')
    #     self.pb.setValue(100)  # 如果爬取成功
    #     msg_box.exec_()
