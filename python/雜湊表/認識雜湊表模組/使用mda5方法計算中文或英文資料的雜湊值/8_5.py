# usr/bin/env python
# -*- coding:UTF-8 -*-

import hashlib

data = hashlib.md5()
school = '明志科技大學'
data.update(school.encode('utf-8'))

print('Hash Value =', data.digest())
print('Hash Value(16進位) =', data.hexdigest())
print(type(data))
print(type(data.hexdigest()))
