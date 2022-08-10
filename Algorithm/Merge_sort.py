# -*- coding: UTF-8 -*-
# created by Long on 2021/12/8 12:26
# @Software : PyCharm
def merge(lists, low, mid, high):
    i = low
    j = mid + 1
    lists_temp = []
    while i <= mid and j <= high:  # 只要左右两边都有数
        if lists[i] < lists[j]:
            lists_temp.append(lists[i])
            i += 1
        else:
            lists_temp.append(lists[j])
            j += 1
    # while执行完，肯定有一部分没有数字了
    while i <= mid:
        lists_temp.append(lists[i])
        i += 1
    while j <= high:
        lists_temp.append(lists[j])
        j += 1
    lists[low:high + 1] = lists_temp


def merge_sort(lists, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(lists, low, mid)
        merge_sort(lists, mid+1, high)
        merge(lists, low, mid, high)


if __name__ == '__main__':
    lists = [1, 3, 2, 6, 5, 4]
    merge_sort(lists, 0, len(lists)-1)
    print(lists)