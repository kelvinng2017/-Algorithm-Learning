# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
2_3.py 先建立陣列,然後在索引2位置插入100
"""
from array import*
x = array('i', [5, 15, 25, 35, 45])

x.insert(2, 100)
for data in x:
    print(data)
