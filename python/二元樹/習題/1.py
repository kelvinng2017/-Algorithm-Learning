# /usr/bin/env python
# -*- coding:UTF-8 -*-

"""
6_5.py 使用10,21,5,9,13,28系列數字建立一個二元樹，然後使用前序方式列印
"""


from itertools import count


class Node():
    counting_function_execution = 0

    def __init__(self, data=None):
        '''建立二元樹的節點'''
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        '''建立二元樹'''
        if self.data:  # 如果根節點存在
            if data < self.data:  # 插入值小於目前節點值
                if self.left:

                    self.left.insert(data)  # 遞迴呼叫往下一層
                else:

                    self.left = Node(data)  # 建立新節點存放資料
            else:  # 插入值大於目前的節點
                if self.right:

                    self.right.insert(data)
                else:

                    self.right = Node(data)
        else:

            self.data = data  # 建立根節點

    def preorder(self):
        '''前序列印'''
        print(self.data)  # 列印
        if self.data == 10:
            test = 0
        else:
            test = 1

        if self.left:  # 如果左子節點存在
            # print(f"hi1:{self.data}")
            self.left.preorder()  # 遞迴呼叫下一層
            # print(f"hi2:{self.data}")

        if self.right:  # 如果右子節點存在
            # print(f"hi3:{self.data}")
            self.right.preorder()  # 遞迴呼叫下一層
            # print(f"hi4:{self.data}")
        if self.right == None and self.left == None:
            self.__class__.counting_function_execution += 1

      # 在 function定義完之後 初始化靜態變數


tree = Node()  # 建立二元樹物件
datas = [10, 21, 5, 9, 13, 28, 3, 4, 1, 17, 32]  # 建立二元樹數據
for d in datas:
    tree.insert(d)  # 分別插入數據
tree.preorder()  # 前序列印
print(Node.counting_function_execution)
