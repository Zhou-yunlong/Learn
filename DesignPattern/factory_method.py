# -*- coding: UTF-8 -*-
# created by Long on 2022/8/10 13:51
# @Software : PyCharm
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print("花呗支付%d元" % money)
        else:
            print("支付宝余额支付%d元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)


class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AliPayFactory(PaymentFactory):
    def create_payment(self):
        return AliPay()


class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return AliPay(use_huabei=True)


pf = HuabeiFactory()
p = pf.create_payment()
p.pay(100)