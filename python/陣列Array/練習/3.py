# /usr/bin/env python
# -*- coding: UTF-8 -*-
x = [1, 11, 22, 33, 44, 55]
print("陣列如下:")
for data in x:
    print(data)


while True:
    need_insert_index = int(input("請輸入欲插入索引:"))
    need_insert_value = int(input("請輸入欲插入數值:"))
    if(need_insert_index >= 0 and need_insert_index <= 5):
        break
    else:
        print("輸入錯誤")

x.insert(need_insert_index, need_insert_value)
for data in x:
    print(data)
