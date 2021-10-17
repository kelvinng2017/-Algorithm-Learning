# /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
5_5.py 這是1_1.py 的改良，主要是在factorial() 函數内增加注解，讀者可以從函數看到遞迴呼叫的計算過程
"""


def factorial(n):
    global fact
    """計算n的階層, n必須是正整數"""
    if n == 1:
        print("factorial(%d)呼叫前 %d! = %d" % (n, n, fact))
        print("到達遞迴條件終止  n=1")
        fact = 1
        print("factorial(%d)返回後 %d! = %d" % (n, n, fact))
        return fact
    else:
        print("factorial(%d) 呼叫前 %d! = %d" % (n, n, fact))
        fact = n * factorial(n-1)
        print("factorial(%d)返回後 %d! = %d" % (n, n, fact))
        return fact


fact = 0

N = eval(input("請輸入階乘數:"))
print(N, " 的階乘結果是=", factorial(N))
