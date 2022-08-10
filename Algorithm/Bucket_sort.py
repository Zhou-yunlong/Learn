# -*- coding: UTF-8 -*-
# created by Long on 2021/12/9 9:50
# @Software : PyCharm
def bucket_sort(lists, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建桶
    for var in lists:
        i = min(var // (max_num // n), n-1)  # i表示bar放到几号桶里
        buckets[i].append(var)
        # 保持桶内的顺序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_lists = []
    for buc in buckets:
        sorted_lists.extend(buc)
    return sorted_lists
import random
lists = [random.randint(0, 10) for i in range(10)]
print(lists)
lists = bucket_sort(lists)
print(lists)