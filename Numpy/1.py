# -*- coding: UTF-8 -*-
# created by Long on 2022/6/6 23:43
# @Software : PyCharm
from SUM import Calc


class Math(object):
    def __init__(self):
        self.sum = Calc.sum(self)

    def show(self):
        print(self.sum)


a = Math()
a.show()