# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
7_5.py:nlargest() 和 nsmallest() 的應用，這個程式會傳回從大致小的
最大三個數目和從小到大的最小3個數
"""

# ch7_5.py
import heapq
h = [10, 21, 5, 9, 13, 28, 3]
print("最大3個:", heapq.nlargest(3, h))
print("最小3個:", heapq.nsmallest(3, h))
print("原先資料集:", h)
