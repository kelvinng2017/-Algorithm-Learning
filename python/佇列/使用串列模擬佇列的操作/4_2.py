# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
4_2.py 擴充ch4_1.py讀取4次佇列並觀察執行結果
"""


class Queue():
    '''Queue佇列'''

    def __init__(self):
        self.queue = []  # 使用串列模擬

    def enqueue(self, data):
        '''data插入佇列'''
        self.queue.insert(0, data)

    def dequeue(self):
        '''讀取佇列'''
        if len(self.queue):
            return self.queue.pop()
        return "佇列是空的"

    def size(self):
        '''回傳佇列長度'''
        return len(self.queue)


q = Queue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
#print('佇列長度是:', q.size())
print("讀取佇列:", q.dequeue())
print("讀取佇列:", q.dequeue())
print("讀取佇列:", q.dequeue())
print("讀取佇列:", q.dequeue())
