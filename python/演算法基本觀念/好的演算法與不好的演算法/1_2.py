# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
1_2.py:延續前面觀念，假設超級電腦每秒可以處理10兆個數列，運氣最差狀況
請計算需要多少年可以得到從小到大的數列。，
"""


def factorial(n):
    """
    計算n的階層,n必須是正整數
    """

    if n == 1:
        return 1
    else:
        return (n*factorial(n-1))


N = eval(input("請輸入階層數:"))
print(N, "的階層結果是=", factorial(N))
times = 0.0000000001  # 電腦每秒可以處理數列數目
day_secs = 60 * 60 * 24  # 一天秒數
yeae_secs = 365 * day_secs  # 一年秒數
combinations = factorial(N)  # 組合方式
years = combinations*times
print("資料個數 %d, 數列組合數 = %d " % (N, combinations))
print("需要 %d 年才可以獲得結果" % years)
