# -*- coding: UTF-8 -*-
# created by Long on 2021/12/30 19:31
# @Software : PyCharm


alist = [('安提瓜', 4.04), ('圣卢西亚', 6.9), ('波兰', 4.09), ('墨西哥', 3.72), ('加拿大', 7.79), ('俄罗斯', 6.0), ('韩国', 8.4), ('西班牙', 5.69)]
res = {}
for part in alist:
    country, fare = part
    res[country] = fare
a = input("请输入国家：")
print("%s 运费 %s" % (a, res[a]))
