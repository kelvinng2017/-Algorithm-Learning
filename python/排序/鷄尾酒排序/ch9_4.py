# usr/bin/env python
# -*- coding:UTF-8 -*-

"""
使用9-3-1節的圖解演算法數據，執行鷄尾酒排序法，在這個程式筆者將列出每次的排序過程
"""


from web_service_log import SYSTEM_logger


def cocktail_sort(nLst):
    '''雞尾巴就排序發'''
    n = len(nLst)
    is_sorted = True
    start = 0  # 前端索引
    end = n - 1  # 末端索引
    while is_sorted:
        is_sorted = False  # 重置是否排序完成
        for i in range(start, end):  # 往右比較
            if (nLst[i] > nLst[i+1]):
                nLst[i], nLst[i+1] = nLst[i+1], nLst[i]
                is_sorted = True
        SYSTEM_logger.info("往後排序過程:{}".format(nLst))
        if not is_sorted:  # 如果沒有交換結果
            break
        end = end-1  # 末端索引左移一個索引
        for i in range(end-1, start-1, -1):  # 往左比較
            if (nLst[i] > nLst[i+1]):
                nLst[i], nLst[i+1] = nLst[i+1], nLst[i]
                is_sorted = True
        start = start + 1
        SYSTEM_logger.info("往前排序過程:{}".format(nLst))
    return nLst


data = [6, 1, 5, 7, 3]
SYSTEM_logger.info("原始串列:{}".format(data))
SYSTEM_logger.warning("排序結果:{}".format(cocktail_sort(data)))
