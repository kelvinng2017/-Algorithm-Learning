# /usr/bin/env python
# -*- coding:UTF-8 -*-

"""
ch9_5.py:選擇排序
"""
from web_service_log import *


def selection_sort(nLst):
    for i in range(len(nLst)-1):
        index = i  # 最小值的索引

        for j in range(i+1, len(nLst)):  # 找最小值的索引
            if nLst[index] > nLst[j]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 資料對調
        SYSTEM_logger.info("第{}次迴圈排序:{}".format(i+1, nLst))
    return nLst


data = [6, 1, 5, 7, 3]
SYSTEM_logger.info("原始串列:{}".format(data))
SYSTEM_logger.info("排序結果:{}".format(selection_sort(data)))
