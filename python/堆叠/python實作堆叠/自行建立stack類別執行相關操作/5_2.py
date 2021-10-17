# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
5_2.py: 將Grape、Mango、Apple 分別push入堆叠，然後輸出有多少種水果在堆叠内
"""


class Stack():
    def __init__(self):
        self.my_stack = []

    def my_push(self, data):
        self.my_stack.append(data)

    def my_pop(self):
        return self.my_stack.pop()

    def size(self):
        return len(self.my_stack)


stack = Stack()
fruits = ['Grape', 'Mango', 'Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print('將 %s 水果堆入堆叠' % fruit)

print('堆叠有%d 種水果' % stack.size())
