# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
5_3.py: 擴充設計5_2.py 將資料push人堆叠後，輸出數量後，將資料pop出堆叠。在這個程式設計中為了
要了解是否所有資料已經pop出來，可以在Stack類別内增加設計isEmpty()方法
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

    def isEmpty(self):
        return self.my_stack == []

    def cls(self):
        self.my_stack.clear()
        print("程式結束")


stack = Stack()
fruits = ['Grape', 'Mango', 'Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print('將 %s 水果堆入堆叠' % fruit)

print(stack.size())
print('堆叠有%d 種水果' % stack.size())
stack.cls()
print(stack.size())
