def draw(strs):
    width = len(strs.encode("gbk"))
    print(width)
    top = "+" + "-"*(40+width) + "+"
    middle = "|" + " "*(40+width) + "|"
    print(len(middle))
    word_line = "|" + " "*20 + strs + " "*20 + "|"
    print(len(word_line))
    bottom = "+" + "-"*(40+width) + "+"
    content = top + "\n" + middle + "\n" + "\n" + word_line + "\n" + "\n" + middle + "\n" + bottom
    return content
while True:
    strs = input("Please enter a sentence:")
    res = draw(strs)
    print(res)
