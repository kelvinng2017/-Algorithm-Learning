# usr/bin/env python
# -*- coding:UTF-8 -*-

from web_service_log import SYSTEM_logger


def selection_sort(nLst):
    '''選擇排序'''
    for i in range(len(nLst)-1):
        index = i  # 最小的索引
        for j in range(i+1, len(nLst)):  # 找最小值的索引
            if nLst[index][2] < nLst[j][2]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不變動
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 資料對調
    return nLst


music = [('李宗盛', '山丘', 24740000),
         ('趙傳', '我是一隻小小鳥', 8310000),
         ('五佰', ' 挪威森林', 34130000),
         ('林憶蓮', '聽說愛情回來過', 12710000)]

SYSTEM_logger.info("YouTube點播排行")
selection_sort(music)
for i in range(len(music)):
    SYSTEM_logger.info("{}:{}{} -- 點播次數  {}".format(i+1,
                       music[i][0], music[i][1], music[i][2]))
