# usr/bin/env python
# -*- coding:UTF-8 -*-

"""
8_3.py 這個程式設計時用雜湊表建立選民名冊，鍵(key)是選民的名字，
值(value)全部先預設為None ,如果已經投票則將此名字的值設為True。
"""


def check_name(name):
    if voted[name]:
        print('你已經投過票了')
    else:
        print('歡迎投票')
        voted[name] = True


voted = {'Trump': None,
         'Lisa': None,
         'Mike': None}

name = input('請輸入名字:')
if name in voted:
    check_name(name)
else:
    print('你不是選民')
