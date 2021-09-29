# usr/bin/env python
# -*- coding: UTF-8 -*-
"""
2-6.py 先建立陣列然後第一次使用pop(), 第二次使用pop(2)回傳和刪除陣列元素
"""

from array import *
x = array('i', [5, 15, 25, 35, 45])
n = x.pop()
print('刪除 ', n)
for data in x:
    print(data)

n = x.pop(2)
print('刪除 ', n)
for data in x:
    print(data)
