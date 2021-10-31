# usr/bin/env python
# -*- coding: UTF-8 -*-

"""
7_2.py:擴充程式實例ch7_1.py分別插入11和2，同時列出結束。
"""

import heapq


h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("插入前  h = ", h)
heapq.heappush(h, 11)
print("第一次插入後 h = ", h)
heapq.heappush(h, 2)
print("第二次插入後 h = ", h)
