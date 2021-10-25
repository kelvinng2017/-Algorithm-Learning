# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
使用10,5,21,9,13,28,3,4,1,17,32建立一個二元樹，請使用中序列印，然後刪除5，最後載用一次中序列印。
"""


class Node():
    def __init__(self, data=None):
        '''建立二元數據'''
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
                    self.left = Node(data)  # 建立新節點存放在資料
            else:  # 插入值大於目前節點資料
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:  # 如果根節點不存在
            self.data = data  # 建立根節點

    def postorder(self):
        '''後續列印'''
        if self.left:  # 如果左子節點存在
            self.left.postorder()  # 遞迴呼叫下一層

        if self.right:  # 如果右子節點存在
            self.right.postorder()  # 遞迴呼叫下一層
        print(self.data)  # 列印


class Delete_node():
    def deleteNode(self, root, key):
        if root is None:  # 二元樹不存在返回
            return None
        if key < root.data:  # 刪除值小於root值則往左
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.data:  # 刪除值大於root值則往右
            root.right = self.deleteNode(root.right, key)
            return root
        if root.left is None:  # 左邊節點不存在
            new_root = root.right
            return new_root
        if root.right is None:  # 右邊節點不存在
            new_root = root.left
            return new_root
        succ = self.min_node(root.right)  # 找左子樹中最大值的節點

        tmp = Node(succ.data)  # 用此最大值建立節點
        tmp.right = self.right_node(root.right)  # 串接原刪除節點的左子樹
        tmp.left = root.left  # 節點串接原刪除節點的右子樹

        return tmp

    def right_node(self, node):
        '''找出原刪除節點的右子樹'''
        if node.left is None:  # 左子節點不存在
            new_root = node.right  # 使用右節點
            return new_root
        node.left = self.right_node(node.left)  # 插入下一層
        return node

    def left_node(self, node):
        print("left1:"+str(node.data))
        '''找出原刪除節點左子樹'''
        if node.right is None:  # 右子節點不存在
            new_root = node.left  # 使用左子節點
            return new_root
        node.right = self.left_node(node.right)  # 插入下一層
        return node

    def min_node(self, node):
        '''找尋最小值節點'''
        while node.left:  # 如果是否則node是最大值節點
            node = node.left
        return node

    def max_node(self, node):
        '''找尋最大值節點'''
        print("max_node:"+str(node.data))
        while node.right:  # 如果是否則node是最大值節點
            print("max_node_while:"+str(node.data))
            node = node.right
            print("max_node_while:"+str(node.data))
        return node


tree = Node()  # 建立二元樹物件
datas = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]  # 建立二元樹數據
for d in datas:
    tree.insert(d)  # 分別插入數據
tree.postorder()  # 中序列印
del_data = 10
print("刪除 %d 資料後" % del_data)
delete_obj = Delete_node()  # 建立刪除節點物件
result = delete_obj.deleteNode(tree, del_data)  # 刪除操作
result.postorder()
