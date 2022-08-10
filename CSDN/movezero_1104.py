lists = [5, 0, 7, 0, 3, 1]
for i in range(len(lists) - 1):
    for j in range(len(lists) - 1 - i):
        if lists[j] == 0:
            lists[j], lists[j + 1] = lists[j + 1], lists[j]
print(lists)