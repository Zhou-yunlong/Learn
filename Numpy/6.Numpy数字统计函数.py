# -*- coding: UTF-8 -*-
# created by Long on 2022/5/23 13:45
# @Software : PyCharm
import numpy as np

arr = np.arange(12).reshape(3, 4)
print(arr)
a = np.sum(arr)
print(a)
a = np.prod(arr)
print(a)
a = np.cumsum(arr)
print(a)
a = np.cumprod(arr)
print(a)
a = np.min(arr)
print(a)
a = np.max(arr)
print(a)
a = np.percentile(arr, [25, 50, 75])
print(a)
a = np.quantile(arr, [0.25, 0.5, 0.75])
print(a)
a = np.median(arr)
print(a)
a = np.mean(arr)
print(a)
a = np.std(arr)
print(a)
a = np.var(arr)
print(a)
# 加权平均数
weights = np.random.rand(*arr.shape)
a = np.average(arr, weights=weights)
print(a)

arr = np.arange(12).reshape(3, 4)
print(arr)
a = arr.sum(axis=0)
print(a)
a = arr.sum(axis=1)
print(a)
a = arr.cumsum(axis=0)
print(a)
a = arr.cumsum(axis=1)
print(a)

arr = np.arange(12).reshape(3, 4)
print(arr)
# 计算每列的均值
mean = np.mean(arr, axis=0)
# 计算每列的方差
std = np.std(arr, axis=0)
# 计算分子，注意每列都会分别减去[4., 5., 6., 7.]，这叫做numpy的广播
numerator = arr-mean
result = numerator/std
print(result)
# 随机数据
arr2 = np.random.randint(1, 100, size=(3, 4))
print(arr2)
result = (arr2 - np.mean(arr2, axis=0)) / np.std(arr2, axis=0)
print(result)