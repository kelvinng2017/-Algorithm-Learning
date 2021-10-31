# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
7_4.py : heappushpop()方法的應用
"""

import heapq

h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("推入和取出前 h = ", h)
val = heapq.heappushpop(h, 11)
print("取出元素 = ", val)
print("推入和取出元素後 h = ", h)
