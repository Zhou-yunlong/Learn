# -*- coding: UTF-8 -*-
# created by Long on 2022/8/9 22:55
# @Software : PyCharm

# 创建一个抽象类Payment，内部定义一个pay方法，让后续继承此类都需要存在同样的Pay方法以达到统一接口参数的目的
# class Payment:
#     def pay(self, money):
#         raise NotImplementedError
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    pass


class WeChatPay(Payment):
    def pay(self, money):
        pass


a = WeChatPay()
# AliPay继承了Payment这个抽象类，但是没有写pay方法，所以会报错
p = AliPay()