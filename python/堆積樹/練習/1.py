# usr/bin/env python
# -*- coding: UTF-8 -*-

"""
7_2.py:擴充程式實例ch7_1.py分別插入11和2，同時列出結束。
"""

import heapq


h = [10, 21, 5, 9, 13, 28, 3]

y = []
heapq.heapify(y)
for h_list_index in h:
    heapq.heappush(y, h_list_index)
    print("插入{}的二元堆積樹 h={}".format(h_list_index, y))
