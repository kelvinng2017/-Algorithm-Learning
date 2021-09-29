# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
2_7.py 先建立陣列，然後找出陣列元素35的索引值
"""
from array import *
x = array('i', [5, 15, 25, 35, 45])

i = x.index(35)
print(i)
