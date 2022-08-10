def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
lists = []
for i in range(50):
    num = fibonacci(i)
    lists.append(num)
print(lists)