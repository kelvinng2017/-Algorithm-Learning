# usr/bin/env python
# -*- coding:UTF-8 -*-
"""
9_2.py:Python內建的sort()方法實作數字與英文字串排序的應用
"""

cars = ['honda', 'bmw', 'toyota', 'ford']
print("目前的串列={}".format(cars))
print("使用sort()由小排到大")
cars.sort()
print("排序串列的結果=", cars)
nums = [5, 3, 9, 2]
print("目前串列內容={}".format(nums))
print("使用sort()由小排到大")
nums.sort()
print("排序串列的結果:{}".format(nums))
