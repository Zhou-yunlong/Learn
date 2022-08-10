# -*- coding: UTF-8 -*-
# created by Long on 2021/12/7 18:34
# @Software : PyCharm
def sift(lists, low, high):
    """
    :param lists: 列表
    :param low: 堆的根节点的位置
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j开始是左枝
    temp = lists[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and lists[j+1] > lists[j]:  # 如果右枝有并且比较大
            j = j + 1  # j指向右枝
        if lists[j] > temp:
            lists[i] = lists[j]
            i = j  # 往下看一眼
            j = 2 * i + 1
        else:  # temp更大，把temp放到i的位置上
            lists[i] = temp  # 把temp放到某一级分支节点位置
            break
    else:
        lists[i] = temp  # 把temp放到叶子节点上


def heap_sort(lists):
    n = len(lists)
    for i in range((n-2)//2, -1, -1):
        # i表示建堆的时候调整的部分的根的下标
        sift(lists, i, n-1)
    # 建堆完成了
    for i in range(n-1, -1, -1):
        # i指向当前堆的最后一个元素
        lists[0], lists[i] = lists[i], lists[0]
        sift(lists, 0, i-1)  # i-1是新的high


if __name__ == '__main__':
    lists = [1, 3, 2, 6, 5, 4]
    heap_sort(lists)
    print(lists)
