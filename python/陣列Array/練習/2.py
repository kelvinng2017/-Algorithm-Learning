# /usr/bin/env python
# -*- coding: UTF-8 -*-

x = [1, 11, 22, 33, 44, 55]
print("陣列如下:")
for data in x:
    print(data)


while True:
    need_deleted_index = int(input("請輸入欲刪除陣列:"))
    if(need_deleted_index >= 0 and need_deleted_index <= 5):
        break
    else:
        print("輸入錯誤")

n = x.pop(need_deleted_index)
for data in x:
    print(data)
