# -*- coding: UTF-8 -*-
# created by Long on 2022/5/21 22:08
# @Software : PyCharm
import numpy as np
# 创建一个一维数组，也就是Python的单元素List
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("x数组为：", x)
# 创建一个二维数组，也就是Python的嵌套List
X = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
)
print("X数组为：", X)
print("x的维度：", x.shape)
print("X的维度：", X.shape)
print("x的维数：", x.ndim)
print("X的维数：", X.ndim)
print("x的元素的数目：", x.size)
print("X的元素的数目：", X.size)
print("x的类型：", x.dtype)
print("X的类型：", X.dtype)
