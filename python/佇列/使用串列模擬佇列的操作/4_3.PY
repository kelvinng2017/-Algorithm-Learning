# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
4_3.py 建立于列印佇列
"""

from queue import Queue

q = Queue()
for i in range(3):
    q.put(i)

while not q.empty():
    print(q.get())
