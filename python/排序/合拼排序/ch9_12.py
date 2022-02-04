# usr/bin/env python
# -*- coding:UTF-8 -*-

"""
合拼排序
"""


from web_service_log import SYSTEM_logger


def merge(left, right):
    '''兩數列合拼'''
    output = []
    while left and right:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    if left:
        output += left
    if right:
        output += right
    return output


def merge_sort(nLst):
    '''合拼排序'''
    if len(nLst) <= 1:  # 剩下一個或0個元素直接返回
        return nLst
    mid = len(nLst) // 2  # 取中間索引
    # 切割(divide)數列
    left = nLst[:mid]  # 取左半段
    right = nLst[mid:]  # 取右半段
    # 處理左序列和右邊序列
    left = merge_sort(left)  # 左邊排序
    right = merge_sort(right)  # 右邊排序
    return merge(left, right)  # 傳回合拼


data = [6, 1, 5, 7, 3, 9, 4]
SYSTEM_logger.info("原始串列:{}".format(data))
SYSTEM_logger.info("排序結果:{}".format(merge_sort(data)))
