# usr/bin/env python
# -*- coding:UTF-8 -*-

import random

from web_service_log import *


def quick_sort(nLst):
    '''快速排序法'''
    if len(nLst) <= 1:
        return nLst

    left = []  # 左邊串列
    right = []  # 右邊串列
    piv = []  # 基準串列
    pivot = random.choice(nLst)  # 隨機設定基準
    for val in nLst:
        if val == pivot:
            piv.append(val)  # 加入基準串類
        elif val < pivot:  # 如果小於基準
            left.append(val)  # 加入左邊串列
        else:
            right.append(val)  # 加入右邊串列
    return quick_sort(left) + piv + quick_sort(right)


data = [6, 1, 5, 7, 3, 9, 4, 2, 8]

SYSTEM_logger.info("原始串列:{}".format(data))
SYSTEM_logger.info("排序就結果:{}".format(quick_sort(data)))
