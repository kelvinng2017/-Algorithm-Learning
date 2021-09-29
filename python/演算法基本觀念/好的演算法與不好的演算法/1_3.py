# /usr/bin/env python
# -*- coding: UTF-8 -*-


"""
1_3:列出串列元素1,2,3,所有的組合
"""
import itertools
x = ['a', 'b', 'c', 'd', 'e', 'f']
perm = itertools.permutations(x)
j = 0
for i in perm:
    print(i)
    j += 1

print(j)
