# usr/bin/env python
# -*- coding:UTF-8 -*-

from web_service_log import *


def bubble_sort(nLst):
    length = len(nLst)
    for i in range(length-1):
        print("第{}次外圈排序".format(i+1))
        for j in range(length-1-i):
            if nLst[j] < nLst[j+1]:
                nLst[j], nLst[j+1] = nLst[j+1], nLst[j]
            print("第{}次內圈排序:{}".format((j+1), nLst))
    return nLst


data = [6, 1, 5, 7, 3]
SYSTEM_logger.info("原始串列:{}".format(data))
SYSTEM_logger.info("排序結果:{}".format(bubble_sort(data)))
