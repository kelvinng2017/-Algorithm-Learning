# /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
7_3.py:heappopp()方法的應用
"""

import heapq
h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("取出前面 h = ", h)
val = heapq.heappop(h)
print("取出元素 = ", val)
print("取出後的元素 = ", h)
