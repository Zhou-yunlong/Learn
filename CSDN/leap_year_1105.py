def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return 1
    else:
        return 0

start_year = 2000
end_year = 3000
for i in range(start_year, end_year):
    res = leap_year(i)
    if res == 1:
        print(i)

