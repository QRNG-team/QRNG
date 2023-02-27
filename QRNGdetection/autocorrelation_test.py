#!/usr/bin/python3
# -*- coding=utf-8 -*-

"""
自相关检测

（1）原理：
将序列逻辑左移d位后所得新序列与原序列的关联程度
（2）不通过分析：
序列中0,1变化的过慢
（3）参数设置:
d = 1,2,8
（4）参数要求：
1 <=d <=floor(n/2), (n-d)>10
"""
import sys
import Tool.glo as glo
import math

def autocorrelation_test(bits, d, a):
    """
    autocorrelation test

    args:
        bits: bit stream
        a   : significance level
    rets:
        [n, S, V, a, p_value, p_value >= a]
    """
    n = len(bits)
    m = [int(bits[i])^int(bits[i+d]) for i in range(n-d)]

    S = sum(m)

    V = 2*(S-((n-d)/2))/math.sqrt(n-d)

    p_value = math.erfc(abs(V)/math.sqrt(2))

    return [n, S, V, a, p_value, p_value >= a]

def autocorrelation_logs(n, S, V, a, p_value, result, out_path):
    try:
        sys.stdout = glo.Logger(out_path)
        print("\t\t\t       AUTOCORRELATION TEST")
        print("\t\t---------------------------------------------")
        print("\t\t COMPUTATIONAL INFORMATION:                  ")
        print("\t\t---------------------------------------------")
        print("\t\t(a) n                   = ", n)
        print("\t\t(b) S                   = ", S)
        print("\t\t(c) V                   = ", V)
        print("\t\t(d) a                   = ", a)
        print("\t\t(e) p_value             = ", p_value)
        print("\t\t(f) pass                = ", result)
        print("\t\t---------------------------------------------")
    finally:
        sys.stdout.reset()

def autocorrelation(tt_path, out_path):
    test = ''
    f = open(tt_path)
    for line in f.readlines():
        line = line.strip()
        test += line
    nbits = [v for v in test]
    bits = [int(x) for x in nbits]
    ret = autocorrelation_test(bits, 1, 0.01)
    autocorrelation_logs(*ret, out_path)
    ret = autocorrelation_test(bits, 2, 0.01)
    autocorrelation_logs(*ret, out_path)
    ret = autocorrelation_test(bits, 8, 0.01)
    autocorrelation_logs(*ret, out_path)
    ret = autocorrelation_test(bits, 16, 0.01)
    autocorrelation_logs(*ret, out_path)

if __name__ == '__main__':
    tt_path = 'E:\Project\Python\实验\第二次预实验\实验结果\输入1.140dBm量程0.2V\输入1.140dBm量程0.2V-后提取结果-数据：1068576.txt'
    autocorrelation(tt_path)
