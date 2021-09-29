# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
2_8.py 更改索引2的内容為100
"""

from array import *
x = array('i', [5, 15, 25, 35, 45])

x[2] = 100
for data in x:
    print(data)
