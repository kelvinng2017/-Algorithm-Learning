# usr /bin/env puython
# -*- coding:UTF-8 -*-

"""
使用sha1()方法重新設計ch8_4.py
"""

import hashlib

data = hashlib.sha1()

data.update(b'Ming-Chi Institute of Technology')

print('Hash Value =', data.digest())
print('Hash Value(16進位)=', data.hexdigest())
print(type(data))
print(type(data.hexdigest()))
