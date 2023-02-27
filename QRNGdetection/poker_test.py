#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
扑克检测

(1) 原理：
长度为m的子序列有2^m种。以此长度划分带检测序列，检测子序列的个数是否接近。统计值V
应该服从自由度为(2^m-1)的卡方(x^2)分布
(2) 不通过分析：
有某个或者某几个子序列的个数过多或者过少。
(3) 参数设置：
m = 4,8
(4) 参数要求：
floor(n/m) >= 5 * 2^m
"""

import math
from typing import List
import scipy.special as ss
import numpy as np
import Tool.glo as glo
import sys


def poker_test(bits, m, a):
    """
    poker test

    args:
        bits: bit stream
        m   : length of subsequences
        a   : significance level

    rets:
        [n, m, N, V, a, p_value, p_value>=a]
    """

    n = len(bits)
    print("n=", n)
    # 将带检测序列分为N个长度为m的非重叠子序列
    N = n // m
    print("非重叠子序列长度", N)
    # 统计第i种子序列模式出现的频数
    list_str = ''
    ni = [0] * (2 ** m)
    for i in range(N):
        list = bits[i * m: (i + 1) * m]
        list_str = [str(i) for i in list]
        #      print("list_str=",list_str)
        list_str1 = ''.join(list_str)
        #     print("list_str1=",list_str1)
        ni[int(list_str1, 2)] += 1
        list_str = ''
    # 计算统计值V
    V = 0
    for v in ni:
        V += v ** 2
    V = (2 ** m / N) * V - N

    # 计算P-value
    p_value = ss.gammaincc((2 ** m - 1) / 2, V / 2)

    return [n, m, N, V, a, p_value, p_value >= a]


def poker_logs(n, m, N, V, a, p_value, result, out_path):
    try:
        sys.stdout = glo.Logger(out_path)
        print("\t\t\t       POKER TEST")
        print("\t\t---------------------------------------------")
        print("\t\t COMPUTATIONAL INFORMATION:                  ")
        print("\t\t---------------------------------------------")
        print("\t\t(a) n                   = ", n)
        print("\t\t(b) m                   = ", m)
        print("\t\t(c) N                   = ", N)
        print("\t\t(d) V                   = ", V)
        print("\t\t(e) a                   = ", a)
        print("\t\t(f) p_value             = ", p_value)
        print("\t\t(g) pass                = ", result)
        print("\t\t---------------------------------------------")
    finally:
        sys.stdout.reset()


def poker(tt_path, out_path):
    test = ''
    f = open(tt_path)
    for line in f.readlines():
        line = line.strip()
        test += line
    nbits = [v for v in test]
    bits = [int(x) for x in nbits]

    ret = poker_test(bits, 4, 0.01)
    poker_logs(*ret, out_path)
    ret = poker_test(bits, 8, 0.01)
    poker_logs(*ret, out_path)


if __name__ == '__main__':
    # strs = file_to_bytes("./data/data.sha1")
    #  bits = bytes_to_base2string(strs)
    test = ''
    tt_path = 'E:\Project\Python\实验\第二次预实验\实验结果\输入1.140dBm量程0.2V\输入1.140dBm量程0.2V-后提取结果-数据：1068576.txt'
    poker(tt_path,tt_path)
