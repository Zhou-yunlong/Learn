def change(num):
    hour = num / 3600
    minute = num % 3600 / 60
    second = num % 3600 % 60
    return hour, minute, second
while True:
    count = int(input("Input the number of seconds:"))
    hour, minute, second = change(count)
    print("%d:%d:%d" % (hour, minute, second))