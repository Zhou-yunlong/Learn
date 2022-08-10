# -*- coding: UTF-8 -*-
# created by Long on 2022/5/24 0:41
# @Software : PyCharm
import numpy as np
a = np.arange(6).reshape(2, 3)
b = np.random.randint(10, 20, size=(4, 3))
print("a数组为：", a)
print("b数组为：", b)

# 方法1
print(np.concatenate([a, b]))
# 方法2
print(np.vstack([a, b]))
# 方法3
print(np.row_stack([a, b]))

a = np.arange(6).reshape(3, 2)
b = np.random.randint(10, 20, size=(3, 4))
print("a数组为：", a)
print("b数组为：", b)
# 方法1
print(np.concatenate([a, b], axis=1))
# 方法2
print(np.hstack([a, b]))
# 方法3
print(np.column_stack([a, b]))