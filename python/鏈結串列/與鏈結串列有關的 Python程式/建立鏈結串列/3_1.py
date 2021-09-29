# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
3_1.py 建立一個包含3個節點的鏈結串列，然後列印此鏈結串列
"""


class Node():
    """節點"""

    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 指標


n1 = Node(5)  # 節點1
n2 = Node(15)  # 節點2
n3 = Node(25)  # 節點3

n1.next = n2  # 節點1指向節點2
n2.next = n3  # 節點2指向節點3
ptr = n1  # 建立指標節點
while ptr:
    print(ptr.data)  # 列印節點
    ptr = ptr.next  # 移動指標到下一個節點
