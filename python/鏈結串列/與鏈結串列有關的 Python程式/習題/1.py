# /usr/bin/env python
# -*- coding: UTF-* -*-

class Node():
    """節點"""

    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 指標


class Linked_list():
    """鏈結串列"""

    def __init__(self):
        self.head = None  # 鏈結串列第一個節點

    def print_list(self):
        """列印串列鏈結"""
        ptr = self.head  # 指標指向鏈結串列第1個節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.next  # 移動指標到下一個節點

    def length(self):
        """計算串列的長度"""
        ptr = self.head  # 指標指向鏈結串列第1個節點
        count_ptr = 0
        while ptr:
            # print(ptr.data)  # 列印節點
            ptr = ptr.next  # 移動指標到下一個節點
            count_ptr = count_ptr+1
        print("鏈結串列長度是:"+str(count_ptr))


link = Linked_list()
link.head = Node(5)
n2 = Node(15)  # 節點2
n3 = Node(25)  # 節點3
link.head.next = n2  # 節點1指向節點2
n2.next = n3  # 節點2指向節點3
link.print_list()  # 列印鏈結串列link
link.length()
