# usr/bin/env python
# -*- coding: UTF-8 -*-

"""
8_1.py 參考8-2-1節 建立 Refrigerator 、Television 、 Printer 項目，其中
Refrigerator 、Television 、 Printer是鍵(key)，售價是值(value)，最後列印各項目。
"""

product_list = {}
product_list['Refrigerator'] = 8000
product_list['Television'] = 12000
product_list['Printer'] = 8000
print("列印產品資料")
print(product_list)
print("列印 Refrigerator:", product_list['Refrigerator'])
print("列印Televison:", product_list['Television'])
print("列印 Printer:", product_list['Printer'])
