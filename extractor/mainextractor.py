import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import os
import extractor.ottoeplitz
import extractor.plotting
import time
import sys
import os
from PyQt5.QtCore import QThread, pyqtSignal
sys.path.append(os.path.dirname(os.path.dirname(__file__)) + '\\QRNGdetection')
import QRNGdetection.sp800_22
print("调用了QRNGdetection中的模块")
print(sys.path)

""" 
Main program
======================

This file is the entry to the post-extractor program,
which is responsible for removing noise and extracting truly random numbers using the toeplitz matrix

"""


# ori_route = '../../实验/第二次预实验/第二次预实验txt'  # 原始数据文件路径
# filename = '输入4.135dBm量程0.2V'  # 实验数据类型
# fin_route = '../../实验/第二次预实验/实验结果'  # 提取后数据文件路径
# frname = f'{ori_route}/{filename}.txt'
# fwname = f'{fin_route}/{filename}'
# input = []  # 输入序列数据
# N = 14  # 采样位数
# scale = 2 ** 17 + 20000  # 输入数据规模


class Extractor:
    def __init__(self, para):
        self.filename = para["filename"]
        self.fewname = para["fewname"]
        self.fername = para["fername"]
        self.fdwname = para["fdwname"]
        self.fdrname = para["fdrname"]
        self.N = para["N"]
        self.scale = para["scale"]
        self.input = []
        self.length = 0
        self.runtime = 0
        self.testtime = 0
        self.speed = 0
        self.t = None

    def extract(self):

        with open(f'{self.fername}', mode='r') as fdata:
            for i in range(self.scale):
                self.input.append(int(fdata.readline()))
        inputdata = np.array(self.input)
        # for i in range(2**19):
        #     temp = random.gauss(5, .05)  #gauss() 是内置的方法random模块。它用于返回具有高斯分布的随机浮点数。
        #     inputdata.append(temp)
        self.t = extractor.ottoeplitz.Toeplitz(inputdata, self.N)  # 生成toeplitz矩阵
        # extractor.plotting.plot_data(inputdata, 14) #绘制直方图
        start = self.get_time()  # 程序运行时间计时
        dist1 = self.t.hash(0)  # 利用toeplitz后提取,参数为是否将二进制转换为十进制，0为不转换
        end = self.get_time()
        dist = ''
        for subdist in dist1:
            x = str(int(subdist))
            dist += x
        # extractor.plotting.plot_data(dist, 14)
        self.runtime = end - start
        print('Running time: %.4f Seconds\n' % self.runtime)
        self.length = len(dist)
        output = open(f'{self.fewname}/{self.filename}-后提取结果-数据：{self.scale}.txt', 'w')
        output.write(dist)
        outpara = open(f'{self.fewname}/{self.filename}-后提取结果-参数：{self.scale}.txt', 'w')
        outpara.write('原始数据最小熵为： %.2f \n' % self.t.min_ent)
        outpara.write('提取运行时间: %.4f Seconds\n' % self.runtime)
        self.extractspeed = self.length / (self.runtime * 1000)
        outpara.write('提取速度: %.2f kbps\n' % self.extractspeed)
        return [self.t.min_ent, self.runtime, self.extractspeed]

        # 检测

    def detection(self):
        test = ''
        with open(f"{self.fdrname}") as f:
            for line in f.readlines():
                line = line.strip()
                test += line
        nbits = [v for v in test]
        bits = [int(x) for x in nbits]
        results = list()
        start = self.get_time()
        QRNGdetection.sp800_22.all(results, bits)
        end = self.get_time()
        self.testtime = end - start
        print('**************************************************************************')
        print(len(test))
        fdresult = open(f'{self.fdwname}/{self.filename}-检测结果-数据：{self.scale}.txt', "w")
        for result in results:
            (summary_name, summary_p, summary_result) = result
            print(summary_name.ljust(40), summary_p.ljust(28), summary_result, file=fdresult)
        outpara = open(f'{self.fdwname}/{self.filename}-检测结果-参数：{self.scale}.txt', 'w+')
        outpara.write('检测时间: %.4f Seconds\n' % self.testtime)
        return results,self.testtime

    def get_time(self):
        if sys.version_info > (3, 8):  # 兼容Python版本
            return time.perf_counter()
        else:
            return time.clock()
