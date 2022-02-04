# usr/bin/env python
# -*- coding:UTF-8 -*-
from web_service_log import *


def selection_sort(nLst):
    '''選擇排序'''
    for i in range(len(nLst)-1):
        index = i  # 最小值的索引
        for j in range(i+1, len(nLst)):  # 找出最小的索引
            if nLst[index] > nLst[j]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 資料對調
    return nLst


cars = ['honda', 'bmw', 'toyota', 'ford']
SYSTEM_logger.info("目前串列內容 = {}".format(cars))
SYSTEM_logger.info("使用selection_sort()由小到大排序")
selection_sort(cars)
SYSTEM_logger.info("排序串列結果 = {}".format(cars))
