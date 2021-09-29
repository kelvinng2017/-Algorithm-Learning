# /usr/bin/env python
# -*- coding: UTF-8 -*-
"""


2_4.py先建立陣列，然後在陣列未端插入100

"""
from array import *
x = array('i', [5, 15, 25, 35, 45])
x.append(100)
for data in x:
    print(data)
