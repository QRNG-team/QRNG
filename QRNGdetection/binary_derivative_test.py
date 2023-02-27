#!/usr/bin/python3
# -*- coding=utf-8 -*-

import math
import sys
import Tool.glo as glo

"""
二元推导检测

（1）原理：
检测第k次二元推导序列中0和1的个数是否接近一致
（2）不通过分析：
序列中0,1变化的过快或者过慢
（3）参数设置：
k = 3, 7
（4）参数要求：
n >= 100
"""


def binary_derivative_test(bits, k, a):
    """
    binary derivative test

    args:
        bits: bit stream
        a   : significance level
    rets:
        [n, k, S, V, a, p_value, p_value>=a]
    """

    n = len(bits)

    # 对待检测序列依次将初始序列中的相邻2bits作xor操作得到新序列，重复k次
    d = [int(v) for v in bits]
    for j in range(k):
        d = [d[i] ^ d[i + 1] for i in range(len(d) - 1)]

    # 将新的序列中的0和1分别转换成-1和1,然后对其累积求和
    S = sum([(2 * v - 1) for v in d])

    # 计算统计值
    V = abs(S) / math.sqrt(n - k)

    # 计算P-value
    p_value = math.erfc(abs(V) / math.sqrt(2))

    return [n, k, S, V, a, p_value, p_value >= a]


def binary_derivative_logs(n, k, S, V, a, p_value, result, out_path):
    try:
        sys.stdout = glo.Logger(out_path)
        print("\t\t\t       BINARY DERIVATIVE TEST")
        print("\t\t---------------------------------------------")
        print("\t\t COMPUTATIONAL INFORMATION:                  ")
        print("\t\t---------------------------------------------")
        print("\t\t(a) n                   = ", n)
        print("\t\t(b) k                   = ", k)
        print("\t\t(c) S                   = ", S)
        print("\t\t(d) V                   = ", V)
        print("\t\t(e) a                   = ", a)
        print("\t\t(f) p_value             = ", p_value)
        print("\t\t(g) pass                = ", result)
        print("\t\t---------------------------------------------")
    finally:
        sys.stdout.reset()


def binary_derivative(tt_path, out_path):
    test = ''
    f = open(tt_path)
    for line in f.readlines():
        line = line.strip()
        test += line
    nbits = [v for v in test]
    bits = [int(x) for x in nbits]
    ret = binary_derivative_test(bits, 3, 0.01)
    binary_derivative_logs(*ret, out_path)
    ret = binary_derivative_test(bits, 7, 0.01)
    binary_derivative_logs(*ret, out_path)


if __name__ == '__main__':
    test = ''
    tt_path = 'E:\Project\Python\实验\第二次预实验\实验结果\输入1.140dBm量程0.2V\输入1.140dBm量程0.2V-后提取结果-数据：1068576.txt'
    binary_derivative(tt_path,tt_path)
