def binary_search(lists, value):
    left = 0
    right = len(lists) - 1
    while left <= right:
        mid = (left + right) // 2
        if lists[mid] == value:
            return mid
        elif lists[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return None


if __name__ == '__main__':
    lists = [1, 2, 3, 4, 5, 6, 7]
    value = 3
    res = binary_search(lists, value)
    print(res)


