# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
6_3.py 建立二元樹的節點，由於只有一個節點所以這是根節點，然後列印此節點
"""


class Node():
    def __init__(self, data):
        '''建立二元樹的節點'''
        self.data = data
        self.left = None
        self.right = None

    def print_root(self):
        print(self.data)


root = Node(20)
root.print_root()
