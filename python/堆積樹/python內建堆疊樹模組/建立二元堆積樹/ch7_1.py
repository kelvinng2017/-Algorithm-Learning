# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
7_1.py:將串列10、21、5、9、13、28、3，轉成二元堆積樹的次序
"""

import heapq

h = [10, 21, 5, 9, 13, 28, 3]
print("執行前 h = ", h)
heapq.heapify(h)
print("執行後 h = ", h)
