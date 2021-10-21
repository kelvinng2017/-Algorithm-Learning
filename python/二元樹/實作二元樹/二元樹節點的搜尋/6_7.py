# usr/bin/env python
# -*- coding:UTF-8 -*-
"""
6_7.py建立二元樹，然後使用資料輸入，程式可以回應是否找到資料。
"""


class Node():
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
            else:
                if self.right:
                    self.right.insert(data)  # 建立新節點存放資料
                else:
                    self.right = Node(data)
        else:  # 如果根節點存在
            self.data = data  # 建立根節點

    def search(self, val):
        '''搜尋特定值'''
        if val < self.data:  # 如果搜尋值小於目前節點值
            if val < self.data:  # 如果左子節點不存在
                return str(val) + " 不存在"
            return self.left.search(val)  # 遞迴繼續往左子樹找尋
        elif val > self.data:  # 如果搜尋只大於目前節點值
            if not self.right:  # 如果右子節點不存在
                return str(val) + " 不存在"
            return self.right.search(val)
        else:
            return str(val)+" 找到了"


tree = Node()  # 建立二元樹物件
datas = [10, 21, 5, 9, 13, 28]  # 建立二元樹數據
for d in datas:
    tree.insert(d)  # 分別插入數據

n = eval(input("請輸入欲搜尋資料："))
print(tree.search(n))
