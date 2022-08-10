# -*- coding: UTF-8 -*-
# created by Long on 2022/5/22 1:40
# @Software : PyCharm
import numpy as np
# 使生成的随机数相同，不会随着时间的变化而变化
np.random.seed(666)

x = np.random.rand(5)
print(x)
x = np.random.rand(2, 3)
print(x)

x = np.random.randn(5)
print(x)
x = np.random.randn(2, 3)
print(x)

x = np.random.randint(3)
print(x)
x = np.random.randint(1, 10)
print(x)
x = np.random.randint(10, 30, size=(2,))
print(x)
x = np.random.randint(10, 30, size=(2, 3, 4))
print(x)

x = np.random.random(5)
print(x)
x = np.random.random(size=(3, 4))
print(x)
x = np.random.random(size=(2, 3, 4))
print(x)

print("-------------------------")
# choice(a[, size, replace, p])
# 这时候，a是数字，则从range(5)中生成size为3
x = np.random.choice(5, 3)
print(x)
# 多维
x = np.random.choice(5, (2, 3))
print(x)
# 这时候，a是数组，从里面随机取出数字
x = np.random.choice([2, 3, 4, 6, 7, 9], 3)
print(x)
x = np.random.choice([2, 3, 4, 6, 7, 9], (2, 3))
print(x)

# 一维数组
a = np.arange(10)
np.random.shuffle(a)
print(a)
# 如果数组是多维的，则只会在第一维度打散数据
a = np.arange(20).reshape(4, 5)
np.random.shuffle(a)
print(a)

# 这时候，生成range(10)的随机排列
a = np.random.permutation(10)
print(a)
arr = np.arange(9).reshape(3, 3)
# 如果数组是多维的，则只会在第一维度打散数据
# 注意，这里不糊更改原来的arr，会返回一个新的copy
arr2 = np.random.permutation(arr)
print("arr:", arr)
print("arr2:", arr2)

a = np.random.normal(1, 10, 10)
print(a)
a = np.random.normal(1, 10, (2, 3))
print(a)

a = np.random.uniform(1, 10, 10)
print(a)
a = np.random.uniform(1, 10, (2, 3))
print(a)

import matplotlib.pyplot as plt
# 绘制sin曲线
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
# 加入噪声
x = np.linspace(-10, 10, 100)
y = np.sin(x) + np.random.rand(len(x))
plt.plot(x, y)
plt.show()