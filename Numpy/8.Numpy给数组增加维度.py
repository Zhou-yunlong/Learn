# -*- coding: UTF-8 -*-
# created by Long on 2022/5/23 22:56
# @Software : PyCharm
import numpy as np
arr = np.arange(5)
print("原数组为：", arr)

# 方法1：np.newaxis关键字
print(np.newaxis is None)
print(np.newaxis == None)

arr = np.arange(5)
print("原数组为：", arr)
print(arr[np.newaxis, :])
print(arr[np.newaxis, :].shape)

arr = np.arange(5)
print("原数组为：", arr)
print(arr[:, np.newaxis])
print(arr[:, np.newaxis].shape)

arr = np.arange(5)
print("原数组为：", arr)
print(np.expand_dims(arr, axis=0))
print(np.expand_dims(arr, axis=0).shape)

arr = np.arange(5)
print("原数组为：", arr)
print(np.expand_dims(arr, axis=1))
print(np.expand_dims(arr, axis=1).shape)

arr = np.arange(5)
print("原数组为：", arr)
print(np.reshape(arr, (1, 5)))
print(np.reshape(arr, (1, -1)))
print(np.reshape(arr, (1, -1)).shape)

arr = np.arange(5)
print("原数组为：", arr)
print(np.reshape(arr, (-1, 1)))
print(np.reshape(arr, (-1, 1)).shape)
