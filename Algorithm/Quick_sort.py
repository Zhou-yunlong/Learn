def quick_sort(lists, start, end):
    if start >= end:
        return lists  # 递归退出的条件
    low = start
    high = end
    mid = lists[start]  # 初始的基准元素
    while low < high:
        while low < high and mid <= lists[high]:
            high -= 1
        lists[low] = lists[high]
        while low < high and mid >= lists[low]:
            low += 1
        lists[high] = lists[low]

    lists[high] = mid
    quick_sort(lists, start, low-1)
    quick_sort(lists, low+1, end)
    return lists


if __name__ == '__main__':
    lists = [1, 5, 2, 3, 7, 6, 9, 8, 4]
    quick_sort(lists, 0, len(lists)-1)
    print(lists)
