# /usr/bin/env python
# -*- coding:UTF-8 -*-


from web_service_log import SYSTEM_logger


def insertion_sort(nLst):
    '''插入排序'''
    n = len(nLst)
    if n == 1:  # 只有1筆資料
        SYSTEM_logger.info("第{}次迴圈排序 {}".format(n, nLst))
        return nLst
    SYSTEM_logger.info("第1次迴圈排序 {}".format(nLst))
    for i in range(1, n):  # 迴圈
        for j in range(i, 0, -1):
            if nLst[j] < nLst[j-1]:
                nLst[j], nLst[j-1] = nLst[j-1], nLst[j]
            else:
                break
        SYSTEM_logger.info("第{}次迴圈排序 {}".format((i+1), nLst))
    return nLst


data = [6, 1, 5, 7, 3]
SYSTEM_logger.info("原始串列:{}".format(data))
SYSTEM_logger.info("排序結果:{}".format(insertion_sort(data)))
