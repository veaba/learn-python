# pass 空语句，不做任何事情
for letter in "hello world":
    if letter == "o":
        pass
        print("执行pass块")
    print("当前字母：", letter)
print("bye")
