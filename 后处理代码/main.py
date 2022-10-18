import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ottoeplitz
import time
from QRNGdetection import *


# from QRNGdetection import sp800_22

""" 
Main program
======================

This file is the entry to the post-extractor program,
which is responsible for removing noise and extracting truly random numbers using the toeplitz matrix

"""
ori_route = 'E:/博一上/量子随机数/20221006-随机数熵源预实验'  # 原始数据文件路径
filename = '输入1mW量程0.1V-混合噪声'  # 实验数据类型
fin_route = 'E:/博一上/量子随机数/实验结果/预实验'  # 提取后数据文件路径
input = []
N = 14

with open(f'{ori_route}/{filename}.txt', mode='r') as fdata:
    for i in range(2 ** 16 + 20000):
        input.append(int(fdata.readline()))
inputdata = np.array(input)
# for i in range(2**19):
#     temp = random.gauss(5, .05)  #gauss() 是内置的方法random模块。它用于返回具有高斯分布的随机浮点数。
#     inputdata.append(temp)

t = ottoeplitz.Toeplitz(inputdata, 14)  # 生成toeplitz矩阵
# plot_data(inputdata, 14) #绘制直方图
start = time.clock()  # 程序运行时间计时
dist1 = t.hash(0)  # 利用toeplitz后提取,参数为是否将二进制转换为十进制，0为不转换
end = time.clock()
dist = ''

for subdist in dist1:
    x = str(int(subdist))
    dist += x
# # plot_data(dist, 14)

runtime = end - start
print('Running time: %.4f Seconds\n' % runtime)
length = len(dist)
outpara = open(f'{fin_route}/{filename}-后提取参数.txt', 'w+')
outpara.write('Running time: %.4f Seconds\n' % runtime)
speed = length / (runtime * 1000)
outpara.write('Speed: %.2f kbps\n' % speed)
outpara.write('最小熵为： %.2f \n' % t.min_ent)
output = open(f'{fin_route}/{filename}-后提取结果.txt', 'w')
output.write(dist)

# 检测
results = list()
QRNGdetection.sp800_22.all()
print('**************************************************************************')
f = open(f'{fin_route}/{filename}-检测结果', "w")
for result in results:
    (summary_name, summary_p, summary_result) = result
    print(summary_name.ljust(40), summary_p.ljust(28), summary_result, file=f)
