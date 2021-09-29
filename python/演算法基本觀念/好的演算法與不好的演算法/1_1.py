#/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
1_1.py:輸入階乘n，程式可以列出階乘的結果，這個程式相當於可以列出内容n個數的組合方式有多少種方式
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
print(N,"的階層結果是=",factorial(N))