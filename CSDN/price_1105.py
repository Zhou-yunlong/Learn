def price(num):
    if num < 200:
        base_price = 0
        base_num = 0
        unit = 0.5
    elif 200 <= num < 400:
        base_price = 100
        base_num = 200
        unit = 0.65
    elif 400 <= num < 600:
        base_price = 230
        base_num = 400
        unit = 0.8
    else:
        base_price = 390
        base_num = 600
        unit = 1.0
    res = base_price + (num - base_num) * unit
    return res
meter = float(input("用电数量："))
pay_price = price(meter)
print(pay_price)
