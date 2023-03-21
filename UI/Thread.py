# -*- coding: utf-8 -*-
import time
from PyQt5.QtCore import QThread, pyqtSignal
from extractor.mainextractor import Extractor
import Tool.glo as glo
import extractor.entropy


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
    fb = pyqtSignal(str, float)

    # 带一个参数t
    def __init__(self, para, standard, parent=None):
        super(Detection_Thread, self).__init__(parent)
        self.para = para
        self.standard = standard

    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        if self.standard:
            ex = Extractor(self.para)
            detectresult, testtime = ex.detection()
            detectresult.append(testtime)
            detectresult.append(f"NIST检测结果已保存到{self.para['fdwname']}")
            # 发射自定义信号
            # 通过emit函数将参数i传递给主线程，触发自定义信号
            self.finishSignal.emit(
                detectresult)  # 注意这里与_signal = pyqtSignal(str)中的类型相同
        else:
            ex1 = Extractor(self.para)
            fd, testtime = ex1.guomi_detection()
            print(fd)
            self.fb.emit(fd, testtime)  # 注意这里与_signal = pyqtSignal(str)中的类型相同


class Access_Thread(QThread):
    # 自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal(list)
    pb = pyqtSignal(int)

    # 带一个参数t
    def __init__(self, entropylist, entropypara, faname, parent=None):
        super(Access_Thread, self).__init__(parent)
        self.list = entropylist
        self.faname = faname
        self.entropypara = entropypara

    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        f = open(self.faname, 'r')
        flist = []
        accessresult = []
        self.entropypara = list(map(int, self.entropypara))
        for i in range(100):
            flist.append(int(f.readline()))
        if self.list[0] == 1:
            num = extractor.entropy.min_entropy(flist)
            accessresult.append(f"评估文件的最小熵（min entropy)为：{num}")
        if self.list[1] == 1:
            num = extractor.entropy.shannon_entropy(flist)
            accessresult.append(f"评估文件的香农熵（shannon entropy)为：{num}")
        if self.list[2] == 1:
            num = extractor.entropy.sample_entropy(flist, self.entropypara[0], self.entropypara[1])
            accessresult.append(f"评估文件的样本熵（sample entropy)为：{num}")
            accessresult.append(f"样本熵的参数：embedding dimension={self.entropypara[0]}")
            accessresult.append(f"样本熵的参数：tolerance={self.entropypara[1]}")
        if self.list[3] == 1:
            num = extractor.entropy.renyi_entropy(flist, self.entropypara[2])
            print(num)
            accessresult.append(f"评估文件的瑞丽熵（renyi entropy)为：{num}")
            accessresult.append(f"瑞丽熵的参数：order={self.entropypara[2]},require q>=0 and q not = 1")
        # 发射自定义信号
        # 通过emit函数将参数i传递给主线程，触发自定义信号
        self.finishSignal.emit(
            accessresult)  # 注意这里与_signal = pyqtSignal(str)中的类型相同

class Image_Thread(QThread):
    # 自定义信号声明
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等

    finishSignal = pyqtSignal(list)

    # 带一个参数t
    def __init__(self, para, parent=None):
        super(Image_Thread, self).__init__(parent)
        self.para = para

    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        ex = Extractor(self.para)
        print(self.para)
        input1 = ex.file_to_array(self.para['fername'], self.para['scale'])
        input2 = ex.file_to_array(self.para['fewname'], self.para['scale'])
        ex.plot_data(0, 2, input1)
        glo.set_value("imagebar",1)
        ex.plot_data(1, 2, input2)
        glo.set_value("imagebar",2)


# Runthread子线程
class Runthread(QThread):
    progressBarValue = pyqtSignal(int)  # 更新进度条
    signal_done = pyqtSignal(int)  # 是否结束信号

    def __init__(self, flag):
        super(Runthread, self).__init__()
        self.flag = flag

    def run(self):
        if self.flag == 1:  # 负责提取进度条
            while True:
                num1 = glo.get_value('extractbar')
                self.progressBarValue.emit(num1)  # 发送进度条的值信号
                if num1 == 100:
                    break
                time.sleep(0.2)
            self.signal_done.emit(1)  # 发送结束信号

        if self.flag == 2:  # 负责NIST检测进度条
            while True:
                num2 = glo.get_value('detectbar')
                n = (num2 / 15) * 100
                self.progressBarValue.emit(n)  # 发送进度条的值信号
                if num2 == 15:
                    break
                time.sleep(0.5)
            self.signal_done.emit(1)  # 发送结束信号

        if self.flag == 3:  # 负责评估进度条
            while True:
                num2 = glo.get_value('accessbar')
                n = (num2 / 15) * 100
                self.progressBarValue.emit(n)  # 发送进度条的值信号
                if num2 == 15:
                    break
                time.sleep(0.5)
            self.signal_done.emit(1)  # 发送结束信号

        if self.flag == 4:  # 负责国密检测进度条
            while True:
                num3 = glo.get_value('detectbar2')
                n = (num3 / 3) * 100
                self.progressBarValue.emit(n)  # 发送进度条的值信号
                if num3 == 15:
                    break
                time.sleep(0.2)
            self.signal_done.emit(1)  # 发送结束信号

        if self.flag == 5:  # 负责生成图片进度条
            while True:
                num4 = glo.get_value('imagebar')
                n = (num4 / 2) * 100
                self.progressBarValue.emit(n)  # 发送进度条的值信号
                if num4 == 2:
                    break
                time.sleep(1)
            self.signal_done.emit(1)  # 发送结束信号

