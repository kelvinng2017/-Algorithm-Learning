# usr/bin/env python
# -*- coding:UTF-8 -*-

"""
8_2.py 使用字典建立Trump、 Lisa、Mike的電話號碼，
然後輸入人名，如果人名在通訊簿内則列印此名字，如果不在則輸出不在通訊簿内
"""
phone_book = {}
phone_book['Trump'] = '0912111111'
phone_book['Lisa'] = '0922222222'
phone_book['Mike'] = '0932333333'
name = input('請輸入名字:')
if name in phone_book:
    print('{}的電話號碼是{}'.format(name, phone_book[name]))
else:
    print('{}不在通訊簿内'.format(name))
