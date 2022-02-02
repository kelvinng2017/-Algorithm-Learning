from web_service_log import *


def parent(i):
    return (i-1)//2


def add_value_in_heap(new_list, new_child_index):
    while True:
        father_index = (new_child_index-1)//2
        SYSTEM_logger.debug("new_child_index:{}".format(new_child_index))
        SYSTEM_logger.debug("new_child_value:{}".format(
            new_list[new_child_index]))
        if father_index >= 0:
            SYSTEM_logger.debug("father_index:{}".format(father_index))
            SYSTEM_logger.error(
                "father_value:{}".format(new_list[father_index]))
            if new_list[new_child_index] < new_list[father_index]:
                new_list[new_child_index], new_list[father_index] = new_list[father_index], new_list[new_child_index]
            SYSTEM_logger.error("afther_change_list:{}".format(new_list))

        else:
            break
        new_child_index = father_index


my_list = [3, 9, 5, 21, 13, 28, 10, 2]

add_value_in_heap(my_list, (len(my_list)-1))
