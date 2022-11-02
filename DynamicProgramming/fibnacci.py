# -*- coding: UTF-8 -*-
# created by Long on 2022/10/2 16:14
# @Software : PyCharm

# 子问题的重复计算导致此递归方法效率低
def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)


def fibnacci_no_recurision(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n-2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


print(fibnacci_no_recurision(100))
