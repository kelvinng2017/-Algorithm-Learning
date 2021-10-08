# /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
5_1.py 使用Python的append()模擬堆叠的push ,使用Python的pop()模擬堆叠的pop操作
"""
fruits = []
fruits.append('Grape')
fruits.append('Mango')
fruits.append("Apple")
print(f'列印 fruits = {fruits} ')
print(f'pop操作: {fruits.pop()}')
print(f'pop操作: {fruits.pop()}')
print(f'pop操作: {fruits.pop()}')
