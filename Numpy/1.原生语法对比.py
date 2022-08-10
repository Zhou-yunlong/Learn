# -*- coding: UTF-8 -*-
# created by Long on 2022/5/21 21:21
# @Software : PyCharm

import numpy as np
import pandas as pd


def python_sum(n):
    """
    python实现数组的加法
    :param n: 数组的长度
    :return: c
    """
    a = [i ** 2 for i in range(n)]
    b = [i ** 3 for i in range(n)]
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    return c


print(python_sum(10))


def numpy_sum(n):
    """
    numpy实现数组的加法
    :param n: 数组的长度
    :return: c
    """
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c


print(numpy_sum(10))
