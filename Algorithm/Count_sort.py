# -*- coding: UTF-8 -*-
# created by Long on 2021/12/8 22:22
# @Software : PyCharm
def count_sort(lists, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for value in lists:
        count[value] += 1
    lists.clear()
    for index, value in enumerate(count):
        for i in range(value):
            lists.append(index)


if __name__ == '__main__':
    lists = [1, 5, 2, 3, 7, 6, 9, 8, 4]
    count_sort(lists)
    print(lists)