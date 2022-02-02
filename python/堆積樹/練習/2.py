# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
7_9.py 重新設計ch7_1.py ,將普通串列改為堆積串列
"""
from web_service_log import *


class Heaptree():
    def __init__(self):
        self.heap = []  # 堆積樹串列
        self.size = []  # 堆積樹串列元素個數

    def data_down(self, i):
        """如果節點大於子節點值則資料與較小的子節點值對調"""
        while (i*2+2) <= self.size:  # 如果有子節點側繼續
            SYSTEM_logger.debug("i*2+2:{}".format(i*2+2))
            SYSTEM_logger.debug("self.size:{}".format(self.size))
            mi = self.get_min_index(i)  # 取得較小值的子節點
            SYSTEM_logger.error("mi:{}".format(mi))
            if self.heap[i] > self.heap[mi]:  # 如果目前節點大於子節點
                self.heap[i], self.heap[mi] = self.heap[mi], self.heap[i]
                i = mi

    def get_min_index(self, i):
        '''傳回較小值的子節點索引'''
        if i * 2 + 2 >= self.size:  # 只有一個左子節點
            return i * 2+1  # 傳回左子節點索引
        else:
            if self.heap[i*2+1] < self.heap[i*2+2]:  # 如果左子節點小於右子節點
                return i*2+1  # True 傳回左子節點
            else:
                return i*2+2  # False傳回右子節點索引

    def build_heap(self, mylist):
        """建立堆積樹"""
        i = (len(mylist)//2)-1  # 從有子節點的節點開始處理
        SYSTEM_logger.info("i:{}".format(i))
        SYSTEM_logger.info("i_list:{}".format(mylist[i]))
        self.size = len(mylist)  # 得到串列元素的個數
        SYSTEM_logger.debug("self_size:{}".format(self.size))
        self.heap = mylist  # 初步建立堆積樹串列
        SYSTEM_logger.debug("self_heap:{}".format(self.heap))
        while (i >= 0):
            SYSTEM_logger.warning("while_i:{}".format(i))
            self.data_down(i)
            i = i-1
        # SYSTEM_logger.debug("最小索引:{}".format(self.heap[0]))

    def get_small(self, head_list):
        ret_min = self.heap[0]
        SYSTEM_logger.debug("最小索引:{}".format(ret_min))
        # self.size -= 1
        # self.heap[0] = self.heap[self.size]
        # self.heap.pop()
        # self.data_down(0)


h = [10, 21, 5, 9, 13, 28, 3]
print("執行前普通串列 = ", h)
obj = Heaptree()
obj.build_heap(h)
print("執行後堆疊樹串列", obj.heap)
# my_list = obj.heap
# print(my_list)
# SYSTEM_logger.debug("最小值:{}".format(min(my_list)))
# my_list.remove(min(my_list))
# print(my_list)
# obj1 = Heaptree()
# obj1.build_heap(my_list)
# print("執行後堆疊樹串列", obj1.heap)
