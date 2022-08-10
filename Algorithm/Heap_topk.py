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
        if j + 1 <= high and lists[j+1] < lists[j]:  # 如果右枝有并且比较大
            j = j + 1  # j指向右枝
        if lists[j] < temp:
            lists[i] = lists[j]
            i = j  # 往下看一眼
            j = 2 * i + 1
        else:  # temp更大，把temp放到i的位置上
            break
        lists[i] = temp  # 把temp放到某一级分支节点位置


def topk(lists, k):
    # 1.建堆
    heap = lists[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    # 2.比较
    for i in range(k, len(lists)):
        if lists[i] > heap[0]:
            heap[0] = lists[i]
            sift(heap, 0, k-1)
    # 3.遍历输出
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    return heap


if __name__ == '__main__':
    lists = [1, 3, 2, 6, 5, 4]
    res = topk(lists, 3)
    print(res)
