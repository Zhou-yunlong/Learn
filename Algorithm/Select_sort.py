def select_sort(lists):
    for i in range(len(lists)-1):
        min_index = i
        for j in range(i, len(lists)):
            if lists[min_index] > lists[j]:
                min_index = j
        lists[i], lists[min_index] = lists[min_index], lists[i]


if __name__ == '__main__':
    lists = [1, 5, 2, 3, 7, 6, 9, 8, 4]
    select_sort(lists)
    print(lists)