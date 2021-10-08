# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
4_3.py 建立于列印佇列
"""

from queue import Queue

q = Queue()
food_list = ["漢堡", "薯條", "可樂"]
for i in food_list:
    q.put(i)
    print(f"成功插入 {i} 至佇列")
print("佇列輸出")
while not q.empty():
    print(q.get())
