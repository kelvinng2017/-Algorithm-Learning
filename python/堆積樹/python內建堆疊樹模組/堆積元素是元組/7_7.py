# /usr/bin/env python
# -*- coding: UTF-* -*-

"""
7_7.py:堆積元素是元祖資料的應用
"""

import heapq
h = []

heapq.heappush(h, (100, '牛肉麵'))
heapq.heappush(h, (60, '陽春麵'))
heapq.heappush(h, (80, '肉絲麵'))
heapq.heappush(h, (90, '大滷麵'))
heapq.heappush(h, (70, '家常面'))

print(h)
print(heapq.heappop(h))
