def insert_sort(lists):
    for i in range(1, len(lists)):  # i表示摸到的牌的下标
        temp = lists[i]
        j = i - 1
        while j >= 0 and lists[j] > temp:
            lists[j+1] = lists[j]
            j -= 1
        lists[j+1] = temp


if __name__ == '__main__':
    lists = [1, 5, 2, 3, 7, 6, 9, 8, 4]
    insert_sort(lists)
    print(lists)