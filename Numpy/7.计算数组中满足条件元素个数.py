# -*- coding: UTF-8 -*-
# created by Long on 2022/5/23 15:13
# @Software : PyCharm
import time
import numpy as np

arr = np.random.randint(1, 10000, size=int(1e5))
print(arr[:10])
print(arr.size)


pyarr = list(arr)
start = time.time()
a = len([x for x in pyarr if x > 5000])
print(a)
end = time.time()
time1 = start - end
print("python原生语法用时时间为：", time1)

start = time.time()
print(arr[arr > 5000].size)
print((arr > 5000)[:10])
end = time.time()
time2 = start - end
print("numpy向量化语法用时时间为：", time2)

print("原生语句操作时间是numpy的：%s倍" % (time1/time2))