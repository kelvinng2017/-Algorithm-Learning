# usr/bin/env python
# -*- coding: UTF-8 -*-

"""
7_6.py: headreplace()應用，本程式會先列出執行前的堆積，然後執行headpreplace(),
程式會先列出傳回的值，最後列出堆積
"""

import heapq
h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("執行前 h = ", h)
x = heapq.heapreplace(h, 7)
print("取出值 = ", x)
print("執行後 h = ", h)
