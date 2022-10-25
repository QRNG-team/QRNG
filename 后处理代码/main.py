import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import os
import ottoeplitz
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__))+'\\QRNGdetection')
import QRNGdetection.sp800_22

print("调用了QRNGdetection中的模块")
print(sys.path)


def get_time():
    if sys.version_info > (3, 8):
        return time.perf_counter()
    else:
        return time.clock()


""" 
Main program
======================

This file is the entry to the post-extractor program,
which is responsible for removing noise and extracting truly random numbers using the toeplitz matrix

"""
ori_route = '../../实验/第二次预实验/第二次预实验1019'  # 原始数据文件路径
filename = '输入4.135dBm量程0.2V'  # 实验数据类型
fin_route = '../../实验/第二次预实验/实验结果'  # 提取后数据文件路径
input = []  # 输入序列数据
N = 14  # 采样位数
scale = 2 ** 19 + 20000  # 输入数据规模

with open(f'{ori_route}/{filename}.txt', mode='r') as fdata:
    for i in range(scale):
        input.append(int(fdata.readline()))
inputdata = np.array(input)
# for i in range(2**19):
#     temp = random.gauss(5, .05)  #gauss() 是内置的方法random模块。它用于返回具有高斯分布的随机浮点数。
#     inputdata.append(temp)

t = ottoeplitz.Toeplitz(inputdata, 14)  # 生成toeplitz矩阵
# plot_data(inputdata, 14) #绘制直方图
start = get_time()  # 程序运行时间计时
dist1 = t.hash(0)  # 利用toeplitz后提取,参数为是否将二进制转换为十进制，0为不转换
end = get_time()
dist = ''

for subdist in dist1:
    x = str(int(subdist))
    dist += x
# # plot_data(dist, 14)

runtime = end - start
print('Running time: %.4f Seconds\n' % runtime)
length = len(dist)
output = open(f'{fin_route}/{filename}/{filename}-后提取结果-数据：{scale}.txt', 'w')
output.write(dist)

start = get_time()
# 检测
test = ''
f = open(f"{fin_route}/{filename}/{filename}-后提取结果-数据：{scale}.txt")
for line in f.readlines():
    line = line.strip()
    test += line
nbits = [v for v in test]
bits = [int(x) for x in nbits]
results = list()
QRNGdetection.sp800_22.all(results, bits)
end = get_time()
testtime = end - start
print('**************************************************************************')
f = open(f'{fin_route}/{filename}/{filename}-检测结果-数据：{scale}.txt', "w")
for result in results:
    (summary_name, summary_p, summary_result) = result
    print(summary_name.ljust(40), summary_p.ljust(28), summary_result, file=f)
outpara = open(f'{fin_route}/{filename}/{filename}-后提取参数-数据：{scale}.txt', 'w+')
outpara.write('Running time: %.4f Seconds\n' % runtime)
outpara.write('Test time: %.4f Seconds\n' % testtime)
speed = length / (runtime * 1000)
outpara.write('Speed: %.2f kbps\n' % speed)
outpara.write('最小熵为： %.2f \n' % t.min_ent)

