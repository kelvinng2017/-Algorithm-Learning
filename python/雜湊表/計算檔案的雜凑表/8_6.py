# usr/bin/env python
# -*- coding:UTF-8 -*-

"""
8_6.py:在python領域最著名的學習格言是Tim Peters 所寫的Python之禪(The Zen of Python)， 筆者將此内容
放在data8_6.txt 此檔案内容如下，請計算此檔案的雜凑值。
"""

import hashlib

data = hashlib.md5()
filename = "D:\-Algorithm-Learning-1\python\雜湊表\計算檔案的雜凑表\data8_6.txt"

with open(filename, "rb") as fn:
    btxt = fn.read()
    data.update(btxt)

print('Has Value =', data.digest())
print('Hash Value(16進位)=', data.hexdigest())
print(type(data))
print(type(data.hexdigest()))
