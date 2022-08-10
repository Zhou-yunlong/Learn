def check(num):
    if len(num) != 11:
        return "输入错误！"
    else:
        hide_num = num[3:-4]
        new = num.replace(hide_num, "****")
        return new
while True:
    tel = input("请输入手机号：")
    res = check(tel)
    print(res)