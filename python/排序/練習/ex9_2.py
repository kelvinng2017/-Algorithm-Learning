# usr/bin/env python
# -*- coding:UTF-8 -*-

from web_service_log import *


def selection_sort(nLst):
    '''選擇排序'''
    for i in range(len(nLst)-1):
        index = i  # 最小的索引
        for j in range(i+1, len(nLst)):  # 找最小值的索引
            if nLst[index][1] < nLst[j][1]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不變動
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 資料對調
    return nLst


music = [('Python', 98789),
         ('C', 56532),
         ('C#', 88721),
         ('Java', 90397),
         ('C++', 63122),
         ('PHP', 58000)]

SYSTEM_logger.info("程式語言使用率排行")
selection_sort(music)
SYSTEM_logger.debug(music)
for i in range(len(music)):
    SYSTEM_logger.info("{}:{} -- 使用次數  {}".format(i+1,
                       music[i][0], music[i][1]))
