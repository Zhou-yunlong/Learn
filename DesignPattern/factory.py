# -*- coding: UTF-8 -*-
# created by Long on 2022/8/10 12:05
# @Software : PyCharm
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    def __init__(self, use_hunbei=False):
        self.use_huabei = use_hunbei

    def pay(self, money):
        if self.use_huabei:
            print("花呗支付%d元" % money)
        else:
            print("支付宝余额支付%d元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)


class PaymentFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return AliPay()
        elif method == 'wechat':
            return WechatPay()
        elif method == 'huabei':
            return AliPay(use_hunbei=True)
        else:
            raise TypeError("No such payment named %s." % method)


# client
pf = PaymentFactory()
p = pf.create_payment("huabei")
p.pay(100)