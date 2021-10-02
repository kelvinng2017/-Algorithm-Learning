# /usr/bin/env python
# -*- coding: UTF-* -*-

class Node():
    """節點"""

    def __init__(self, data=None):
        self.data = data  # 資料
        self.next = None  # 指標


class Linked_list():
    """鏈結串列"""

    def __init__(self):
        self.head = None  # 鏈結串列第一個節點

    def print_list(self):
        """列印串列鏈結"""
        print("所建立的連接串列")
        ptr = self.head  # 指標指向鏈結串列第1個節點
        while ptr:
            print(ptr.data)  # 列印節點
            ptr = ptr.next  # 移動指標到下一個節點

    def serarch(self, serach_number):
        print("需要尋找的號碼"+str(serach_number))
        """計算串列的長度"""
        ptr = self.head  # 指標指向鏈結串列第1個節點
        count_ptr = 0
        count_number_one = 0
        count_number_two = 0
        count_number_three = 0
        while ptr:
            print("1:"+str(ptr.data))  # 列印節點

            if serach_number[0] == ptr.data:
                count_number_one = count_number_one+1
            elif serach_number[1] == ptr.data:
                count_number_two = count_number_two+1
            elif serach_number[2] == ptr.data:
                count_number_three = count_number_three+1
            ptr = ptr.next  # 移動指標到下一個節點
            count_ptr = count_ptr+1

        print(""+str(serach_number[0])+"出現"+str(count_number_one)+"次")
        print(""+str(serach_number[1])+"出現"+str(count_number_two)+"次")
        print(""+str(serach_number[2])+"出現"+str(count_number_three)+"次")


link = Linked_list()
link.head = Node(5)
n2 = Node(15)  # 節點2
n3 = Node(5)  # 節點3
link.head.next = n2  # 節點1指向節點2
n2.next = n3  # 節點2指向節點3
link.print_list()  # 列印鏈結串列link
search_list = [5, 15, 20]

link.serarch(search_list)
