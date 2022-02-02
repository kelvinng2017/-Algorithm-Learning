# usr/bin/env python
# -*- coding:UTF-8 -*-

"""
8_4.py:使用md5()方法列出英文字串'Ming-Chi Institute of Technology'的雜湊值，同時列出md5()物件與雜湊值的資料形態
"""
import hashlib

data = hashlib.md5()
data.update(b'Ming-Chi Institue of Technology')

print('Hash Value =', data.digest())
print('Hash Value =', data.hexdigest())
print(type(data))
print(type(data.hexdigest()))
