# /usr/bin/env python
# -*- coding: UTF-8 -*-


"""
2_5:先建立陣列，然後刪除陣列元素25
"""
from array import *
x = array('i', [5, 15, 25, 45])
x.remove(25)
for data in x:
    print(data)
