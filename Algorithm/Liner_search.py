def linear_search(lists, value):
    """顺序查找，时间复杂度O(n)"""
    for index, num in enumerate(lists):
        if num == value:
            return index
    else:
        return None

if __name__ == '__main__':
    lists = [1, 2, 3, 4, 5, 6, 7]
    value = 3
    res = linear_search(lists, value)
    print(res)
