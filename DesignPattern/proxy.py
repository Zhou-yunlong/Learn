# -*- coding: UTF-8 -*-
# created by Long on 2022/8/15 18:27
# @Software : PyCharm

from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf-8')
        self.content = f.read()
        print("实例")
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()


class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


class ProtectedProxt(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError("无写入权限")


# subj = RealSubject("test.txt")  # 如果使用真实的函数去创建了一个实例，即使在
# print(subj.get_content())        # 后续不调用实例内部的方法，也会在创建时造成很大的资源浪费
subj1 = VirtualProxy("test.txt")
# print(subj1.get_content())        # 创建虚拟代理则可以在其真正调用方法使用时，才创建对象
subj2 = ProtectedProxt("test.txt")
print(subj2.get_content())
subj2.set_content("abc")