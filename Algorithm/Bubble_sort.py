def bubble_sort(lists):
    for i in range(len(lists)-1):
        for j in range(len(lists)-1-i):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
    return lists


if __name__ == '__main__':
    lists = [1, 3, 2, 6, 5, 4]
    res = bubble_sort(lists)
    print(res)