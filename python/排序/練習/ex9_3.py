# usr/bin/env python
# -*- coding:UTF-8 -*-

from web_service_log import *


def selection_sort(nLst):
    '''選擇排序'''
    for i in range(len(nLst)-1):
        index = i  # 最小的索引
        for j in range(i+1, len(nLst)):  # 找最小值的索引
            if nLst[index][1] > nLst[j][1]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不變動
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 資料對調
    return nLst


music = [('君悅酒店', 5560),
         ('東方酒店', 3540),
         ('北京大飯店', 4200),
         ('喜來登酒店', 5000),
         ('文華酒店', 5200)]

SYSTEM_logger.info("北京酒店定價排行")
selection_sort(music)
SYSTEM_logger.debug(music)
for i in range(len(music)):
    SYSTEM_logger.info("{} -- {}".format(
                       music[i][0], music[i][1]))
