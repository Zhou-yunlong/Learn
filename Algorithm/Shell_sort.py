# -*- coding: UTF-8 -*-
# created by Long on 2021/12/8 21:21
# @Software : PyCharm
def insert_sort_gap(lists, gap):
    for i in range(gap, len(lists)):  # i表示摸到的牌的下标
        temp = lists[i]
        j = i - gap  # j指的是手里的牌的下标
        while j >= 0 and lists[j] > temp:
            lists[j+gap] = lists[j]
            j -= gap
        lists[j+gap] = temp


def shell_sort(lists):
    d = len(lists) // 2
    while d >= 1:
        insert_sort_gap(lists, d)
        d //= 2


if __name__ == '__main__':
    lists = [1, 5, 2, 3, 7, 6, 9, 8, 4]
    shell_sort(lists)
    print(lists)
