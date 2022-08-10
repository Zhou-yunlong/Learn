# -*- coding: UTF-8 -*-
# created by Long on 2022/5/21 23:41
# @Software : PyCharm
import numpy as np

"""
 基础索引
"""
x = np.arange(10)
print("x数组为：", x)
print("x[2]为：", x[2])
print("x[2:4]为：", x[2:4])
print("x[2:-1]为：", x[2:-1])
print("x[-3:]为：", x[-3:])
print("x[:-3]为：", x[:-3])

X = np.arange(20).reshape(4, 5)
print("X数组为：", X)
print("X[-1, 2]为：", X[-1, 2])
print("X[-1]为：", X[-1])
print("X[:2, 2:4]为：", X[:2, 2:4])

"""
 神奇索引
"""
x = np.arange(10)
print("x数组为：", x)
print("x[[3, 4, 7]]为：", x[[3, 4, 7]])
index = np.array([[0, 2], [1, 3]])
print("x[index]为：", x[index])

# 实例：获取数组中最大的前N个数字
# 随机生成1到100之间的10个数字
arr = np.random.randint(1, 100, 10)
print(arr)
# arr.argsort()会返回排序后的索引index
index = arr.argsort()[-3:]
print("前三个最大值对应的下标：", index)
print("前三个最大值为：", arr[arr.argsort()[-3:]])

"""
 布尔索引
"""
# 一维数组
x = np.arange(10)
print("x数组为：", x)
print(x > 5)
print(x[x > 5])
# 实例：把一堆数组进行01化处理（值<=5为0，值>5为1）
x[x <= 5] = 0
x[x > 5] = 1
print(x)
x = np.arange(10)
x[x < 5] += 20
print(x)

# 二维数组
X = np.arange(20).reshape(4, 5)
print("X数组为：", X)
print(X > 5)
# X>5的是boolean数组，当为false的时候没法出结果，因此返回的是（行，列）一维数组
print(X[X > 5])
# 实例：如何把第3列大于5的行筛选出来
print(X[X[:, 3] > 5])
# 把第3列大于5的行筛选出来并赋值为666
X[X[:, 3] > 5] = 666
print(X)

# 条件的组合
x = np.arange(10)
print("x数组为：", x)
# 条件：x为偶数或者x>7
# 注意：每个条件都要加小括号
condition = (x % 2 == 0) | (x > 7)
print("筛选后数组为：", x[condition])
