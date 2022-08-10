# -*- coding: UTF-8 -*-
# created by Long on 2021/12/8 11:24
# @Software : PyCharm

import heapq  # q->queue 优先队列
import random

lists = list(range(100))
random.shuffle(lists)
print("原序列：", lists)
heapq.heapify(lists)  # 建堆,小根堆
n = len(lists)
print("排序后的序列：", end="")
for i in range(n):
    print(heapq.heappop(lists), end=",")
