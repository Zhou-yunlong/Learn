# -*- coding: UTF-8 -*-
# created by Long on 2022/8/10 18:02
# @Software : PyCharm
from abc import ABCMeta, abstractmethod


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


a = MyClass(10)
b = MyClass(20)
print(a.a)
print(b.a)
print(id(a))
print(id(b))